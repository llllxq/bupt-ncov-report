import html
import json
import os
import re
import traceback
from typing import Dict

import requests

# 存储从环境变量中获取到的值
envs = {
    'BUPT_SSO_USER': None,
    'BUPT_SSO_PASS': None,
    'TG_BOT_TOKEN': '',
    'TG_CHAT_ID': '',
}

LOGIN_API = 'https://app.bupt.edu.cn/uc/wap/login/check'
REPORT_PAGE = 'https://app.bupt.edu.cn/ncov/wap/default/index'
REPORT_API = 'https://app.bupt.edu.cn/ncov/wap/default/save'


def check_user_info() -> None:
    """
    检查环境变量是否已经设置，并将其存入 envs 变量中。
    或已经在 envs 中设置。
    :return: None
    """
    
    # check whether username & pwd is set in script or in PATH
    if envs['BUPT_SSO_USER'] is not None and envs['BUPT_SSO_PASS'] is not None:
        return
    for key in ('BUPT_SSO_USER', 'BUPT_SSO_PASS'):
        if key not in os.environ:
            raise ValueError(f'未设置环境变量 `{key}`，无法登录页面。')

        envs[key] = os.environ[key]
        
def check_tg_info() -> None:
    """
    检查TG的环境变量是否已经设置，并将其存入 envs 变量中。
    或已经在 envs 中设置。
    :return: None
    """
    
    # check whether tg info is set
    if envs['TG_BOT_TOKEN'] != '' and envs['TG_CHAT_ID'] != '':
        return
    # check whether 
    if ('TG_BOT_TOKEN' in os.environ) != ('TG_CHAT_ID' in os.environ):
        raise ValueError('TG_BOT_TOKEN 和 TG_CHAT_ID 必须同时设置。')

    if 'TG_BOT_TOKEN' in os.environ:
        envs['TG_BOT_TOKEN'] = os.environ['TG_BOT_TOKEN']
        envs['TG_CHAT_ID'] = os.environ['TG_CHAT_ID']
    

def check_env() -> None:
    """
    检查环境变量是否已经设置，并将其存入 envs 变量中。
    :return: None
    """

    check_user_info()
    check_tg_info()


def match_re_group1(re_str: str, text: str) -> str:
    """
    在 text 中匹配正则表达式 re_str，返回第 1 个捕获组（即首个用括号包住的捕获组）
    :param re_str: 正则表达式（字符串）
    :param text: 要被匹配的文本
    :return: 第 1 个捕获组
    """
    match = re.search(re_str, text)
    if match is None:
        raise ValueError(f'在文本中匹配 {re_str} 失败，没找到任何东西。')

    return match.group(1)


def extract_post_data(html: str) -> Dict[str, str]:
    """
    从上报页面的 HTML 中，提取出上报 API 所需要填写的参数。
    :return: 最终 POST 的参数（使用 dict 表示）
    """
    new_data = match_re_group1(r'var def = (\{.+\});', html)
    old_data = match_re_group1(r'oldInfo: (\{.+\}),', html)
    old_data, new_data = json.loads(old_data), json.loads(new_data)

    # 用原页面的“def”变量的值，覆盖掉“oldInfo”变量的值
    old_data.update(new_data)
    return old_data


def do_ncov_report() -> str:
    """
    进行信息上报的工作函数，包含本脚本主要逻辑。
    :return: 上报 API 的返回内容。
    """
    # 填写环境变量
    check_env()

    # 初始化 session
    session = requests.Session()
    session.timeout = 10

    # 登录北邮 nCoV 上报网站
    login_res = session.post(LOGIN_API, data={
        'username': envs['BUPT_SSO_USER'],
        'password': envs['BUPT_SSO_PASS'],
    })
    if login_res.status_code != 200:
        raise RuntimeError('登录 API 返回的 HTTP 状态码不是 200。')

    # 获取上报页面的数据
    report_page_res = session.get(REPORT_PAGE)
    if report_page_res.status_code != 200:
        raise RuntimeError('上报页面的 HTTP 状态码不是 200。')
    page_html = report_page_res.text
    if '每日上报' not in page_html:
        raise RuntimeError('上报页面的 HTML 中没有找到“每日上报”。')

    # 从上报页面中提取 POST 的参数
    post_data = extract_post_data(page_html)

    # 最终 POST
    report_api_res = session.post(REPORT_API, post_data)
    if report_api_res.status_code != 200:
        raise RuntimeError('上报 API 返回的 HTTP 状态码不是 200。')

    return report_api_res.text


def main(*wtf, **kwwtf) -> None:
    """
    入口函数。可提供给 GCP Cloud Function/AWS Lambda 使用，也可以自行运行。
    :return: None
    """

    # 运行工作函数
    success = True
    try:
        res = do_ncov_report()
    except:
        success = False
        res = traceback.format_exc()

    # 生成消息并打印到控制台
    if success:
        msg = f'[bupt-ncov-report] <b>成功：</b>服务器的返回是：\n\n' \
              f'<pre>{html.escape(res)}</pre>'
    else:
        msg = f'[bupt-ncov-report] <b>失败：</b>发生如下异常：\n\n' \
              f'<pre>{html.escape(res)}</pre>'
    print(msg)

    # 如果用户指定了 Telegram 相关信息，就把消息通过 Telegram 发送给用户
    if envs['TG_BOT_TOKEN'] != '':
        requests.post(f'https://api.telegram.org/bot{envs["TG_BOT_TOKEN"]}/sendMessage', json={
            'chat_id': envs['TG_CHAT_ID'],
            'text': msg,
            'parse_mode': 'HTML',
        })


if __name__ == '__main__':
    main()
