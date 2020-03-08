REPORT_PAGE_HTML = r'''
<!DOCTYPE html>
<html lang="zh-CN">

<head>
<title>每日上报</title>
</head>

<body class="">

<script type="text/javascript">
  var def = {"id":"810810","uid":"93111","date":"20200303","tw":"3","sfcxtz":"0","sfyyjc":"0","jcjgqr":"0","jcjg":"","sfjcbh":"0","sfcxzysx":"0","qksm":"","remark":"","address":"","area":"","province":"\u4e0a\u6d77\u5e02","city":"","geo_api_info":"{\"type\":\"complete\",\"position\":{\"P\":31.22847357856,\"O\":121.47822401258702,\"lng\":121.478224,\"lat\":31.228474},\"location_type\":\"html5\",\"message\":\"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":150,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"021\",\"adcode\":\"310101\",\"businessAreas\":[{\"name\":\" \u65b0\u5929\u5730(\u81ea\u5fe0\u8def)\",\"id\":\"310101\",\"location\":{\"P\":31.220028,\"O\":121.47492399999999,\"lng\":121.474924,\"lat\":31.220028}},{\"name\":\"\u57ce\u968d\u5e99\",\"id\":\"310101\",\"location\":{\"P\":31.225435,\"O\":121.492975,\"lng\":121.492975,\"lat\":31.225435}}],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"\u5ef6\u5b89\u4e1c\u8def\",\"streetNumber\":\"630\u53f7\",\"province\":\"\u4e0a\u6d77\u5e02\",\"city\":\"\",\"district\":\"\u9ec4\u6d66\u533a\",\"township\":\"\u5357\u4eac\u4e1c\u8def\u8857\u9053\"},\"formattedAddress\":\"\u4e0a\u6d77\u5e02\u9ec4\u6d66\u533a\u5357\u4eac\u4e1c\u8def\u8857\u9053\u5ef6\u5b89\u4e1c\u8def\u51ef\u8fea\u62c9\u514b\u00b7\u4e0a\u6d77 \u97f3\u4e50\u5385(\u88c5\u4fee\u4e2d)\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}","created":"2331919931","sfzx":"0","sfjcwhry":"0","sfcyglq":"0","gllx":"","glksrq":"","jcbhlx":"","jcbhrq":"","sftjwh":"0","sftjhb":"0","fxyy":"","bztcyy":"","fjsj":"0","sfjchbry":"0","sfjcqz":"","jcqzrq":"","jcwhryfs":"","jchbryfs":"","xjzd":"","szgj":"","sfsfbh":"0","jhfjrq":"","jhfjjtgj":"","jhfjhbcc":"","jhfjsftjwh":"0","jhfjsftjhb":"0","szsqsfybl":0,"sfygtjzzfj":0,"gtjzzfjsj":"","sfsqhzjkk":"","sqhzjkkys":"","gwszdd":"","sfyqjzgc":"","jrsfqzys":"","jrsfqzfy":"","jrdqtlqk":[],"jrdqjcqk":[]};
  var vm = new Vue({
    el: '.form-detail2',
    data: {
      info: $.extend({
            ismoved: 0,
            jhfjrq: '',
            jhfjjtgj: '',
            jhfjhbcc: '',
            sfxk: 0,
            xkqq: ''
        }, def),
      oldInfo: {"id":"114514","uid":"1919","date":"20200303","tw":"3","sfcxtz":"0","sfyyjc":"0","jcjgqr":"0","jcjg":"","sfjcbh":"0","sfcxzysx":"0","qksm":"","remark":"","address":"\u4e0a\u6d77\u5e02\u9ec4\u6d66\u533a\u5357\u4eac\u4e1c\u8def\u8857\u9053\u5ef6\u5b89\u4e1c\u8def\u51ef\u8fea\u62c9\u514b\u00b7\u4e0a\u6d77\u97f3\u4e50\u5385(\u88c5\u4fee\u4e2d)","area":"\u4e0a\u6d77\u5e02  \u9ec4\u6d66\u533a","province":"\u4e0a\u6d77\u5e02","city":"\u4e0a\u6d77\u5e02","geo_api_info":"{\"type\":\"complete\",\"position\":{\"P\":31.22847357856,\"O\":121.47822401258702,\"lng\":121.478224,\"lat\":31.228474},\"location_type\":\"html5\",\"message\":\"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":150,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"021\",\"adcode\":\"310101\",\"businessAreas\":[{\"name\":\" \u65b0\u5929\u5730(\u81ea\u5fe0\u8def)\",\"id\":\"310101\",\"location\":{\"P\":31.220028,\"O\":121.47492399999999,\"lng\":121.474924,\"lat\":31.220028}},{\"name\":\"\u57ce\u968d\u5e99\",\"id\":\"310101\",\"location\":{\"P\":31.225435,\"O\":121.492975,\"lng\":121.492975,\"lat\":31.225435}}],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"\u5ef6\u5b89\u4e1c\u8def\",\"streetNumber\":\"630\u53f7\",\"province\":\"\u4e0a\u6d77\u5e02\",\"city\":\"\",\"district\":\"\u9ec4\u6d66\u533a\",\"township\":\"\u5357\u4eac\u4e1c\u8def\u8857\u9053\"},\"formattedAddress\":\"\u4e0a\u6d77\u5e02\u9ec4\u6d66\u533a\u5357\u4eac\u4e1c\u8def\u8857\u9053\u5ef6\u5b89\u4e1c\u8def\u51ef\u8fea\u62c9\u514b\u00b7\u4e0a\u6d77 \u97f3\u4e50\u5385(\u88c5\u4fee\u4e2d)\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}","created":"1145141919","sfzx":"0","sfjcwhry":"0","sfcyglq":"0","gllx":"","glksrq":"","jcbhlx":"","jcbhrq":"","sftjwh":"0","sftjhb":"0","fxyy":"","bztcyy":"","ismoved":"0","fjsj":"0","created_uid":"0","sfjchbry":"0","sfjcqz":"","jcqzrq":null,"jcwhryfs":"","jchbryfs":"","xjzd":"","szgj":"","sfsfbh":"0","jhfjrq":"","jhfjjtgj":"","jhfjhbcc":"","jhfjsftjwh":"0","jhfjsftjhb":"0","szsqsfybl":"0","sfygtjzzfj":"0","gtjzzfjsj":"","sfsqhzjkk":"0","sqhzjkkys":""},
    }
  });

</script>
</body>

</html>
'''

REPORT_PAGE_HTML_OF_SICK_PEOPLE = r'''
<!DOCTYPE html>
<html lang="zh-CN">

<head>
<title>每日上报</title>
</head>

<body class="">

<script type="text/javascript">
  var def = {"id":"810810","uid":"93111","date":"20200303","tw":"3","sfcxtz":"0","sfyyjc":"0","jcjgqr":"0","jcjg":"","sfjcbh":"0","sfcxzysx":"0","qksm":"","remark":"","address":"","area":"","province":"\u4e0a\u6d77\u5e02","city":"","geo_api_info":"{\"type\":\"complete\",\"position\":{\"P\":31.22847357856,\"O\":121.47822401258702,\"lng\":121.478224,\"lat\":31.228474},\"location_type\":\"html5\",\"message\":\"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":150,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"021\",\"adcode\":\"310101\",\"businessAreas\":[{\"name\":\" \u65b0\u5929\u5730(\u81ea\u5fe0\u8def)\",\"id\":\"310101\",\"location\":{\"P\":31.220028,\"O\":121.47492399999999,\"lng\":121.474924,\"lat\":31.220028}},{\"name\":\"\u57ce\u968d\u5e99\",\"id\":\"310101\",\"location\":{\"P\":31.225435,\"O\":121.492975,\"lng\":121.492975,\"lat\":31.225435}}],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"\u5ef6\u5b89\u4e1c\u8def\",\"streetNumber\":\"630\u53f7\",\"province\":\"\u4e0a\u6d77\u5e02\",\"city\":\"\",\"district\":\"\u9ec4\u6d66\u533a\",\"township\":\"\u5357\u4eac\u4e1c\u8def\u8857\u9053\"},\"formattedAddress\":\"\u4e0a\u6d77\u5e02\u9ec4\u6d66\u533a\u5357\u4eac\u4e1c\u8def\u8857\u9053\u5ef6\u5b89\u4e1c\u8def\u51ef\u8fea\u62c9\u514b\u00b7\u4e0a\u6d77 \u97f3\u4e50\u5385(\u88c5\u4fee\u4e2d)\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}","created":"2331919931","sfzx":"0","sfjcwhry":"0","sfcyglq":"0","gllx":"","glksrq":"","jcbhlx":"","jcbhrq":"","sftjwh":"0","sftjhb":"0","fxyy":"","bztcyy":"","fjsj":"0","sfjchbry":"0","sfjcqz":"","jcqzrq":"","jcwhryfs":"","jchbryfs":"","xjzd":"","szgj":"","sfsfbh":"0","jhfjrq":"","jhfjjtgj":"","jhfjhbcc":"","jhfjsftjwh":"0","jhfjsftjhb":"0","szsqsfybl":0,"sfygtjzzfj":0,"gtjzzfjsj":"","sfsqhzjkk":"","sqhzjkkys":"","gwszdd":"","sfyqjzgc":"","jrsfqzys":"","jrsfqzfy":"","jrdqtlqk":[],"jrdqjcqk":[]};
  var vm = new Vue({
    el: '.form-detail2',
    data: {
      info: $.extend({
            ismoved: 0,
            jhfjrq: '',
            jhfjjtgj: '',
            jhfjhbcc: '',
            sfxk: 0,
            xkqq: ''
        }, def),
      oldInfo: {"id":"114514","uid":"1919","date":"20200303","tw":"3","sfcxtz":"1","sfyyjc":"0","jcjgqr":"0","jcjg":"","sfjcbh":"0","sfcxzysx":"0","qksm":"","remark":"","address":"\u4e0a\u6d77\u5e02\u9ec4\u6d66\u533a\u5357\u4eac\u4e1c\u8def\u8857\u9053\u5ef6\u5b89\u4e1c\u8def\u51ef\u8fea\u62c9\u514b\u00b7\u4e0a\u6d77\u97f3\u4e50\u5385(\u88c5\u4fee\u4e2d)","area":"\u4e0a\u6d77\u5e02  \u9ec4\u6d66\u533a","province":"\u4e0a\u6d77\u5e02","city":"\u4e0a\u6d77\u5e02","geo_api_info":"{\"type\":\"complete\",\"position\":{\"P\":31.22847357856,\"O\":121.47822401258702,\"lng\":121.478224,\"lat\":31.228474},\"location_type\":\"html5\",\"message\":\"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.\",\"accuracy\":150,\"isConverted\":true,\"status\":1,\"addressComponent\":{\"citycode\":\"021\",\"adcode\":\"310101\",\"businessAreas\":[{\"name\":\" \u65b0\u5929\u5730(\u81ea\u5fe0\u8def)\",\"id\":\"310101\",\"location\":{\"P\":31.220028,\"O\":121.47492399999999,\"lng\":121.474924,\"lat\":31.220028}},{\"name\":\"\u57ce\u968d\u5e99\",\"id\":\"310101\",\"location\":{\"P\":31.225435,\"O\":121.492975,\"lng\":121.492975,\"lat\":31.225435}}],\"neighborhoodType\":\"\",\"neighborhood\":\"\",\"building\":\"\",\"buildingType\":\"\",\"street\":\"\u5ef6\u5b89\u4e1c\u8def\",\"streetNumber\":\"630\u53f7\",\"province\":\"\u4e0a\u6d77\u5e02\",\"city\":\"\",\"district\":\"\u9ec4\u6d66\u533a\",\"township\":\"\u5357\u4eac\u4e1c\u8def\u8857\u9053\"},\"formattedAddress\":\"\u4e0a\u6d77\u5e02\u9ec4\u6d66\u533a\u5357\u4eac\u4e1c\u8def\u8857\u9053\u5ef6\u5b89\u4e1c\u8def\u51ef\u8fea\u62c9\u514b\u00b7\u4e0a\u6d77 \u97f3\u4e50\u5385(\u88c5\u4fee\u4e2d)\",\"roads\":[],\"crosses\":[],\"pois\":[],\"info\":\"SUCCESS\"}","created":"1145141919","sfzx":"0","sfjcwhry":"0","sfcyglq":"0","gllx":"","glksrq":"","jcbhlx":"","jcbhrq":"","sftjwh":"0","sftjhb":"0","fxyy":"","bztcyy":"","ismoved":"0","fjsj":"0","created_uid":"0","sfjchbry":"0","sfjcqz":"","jcqzrq":null,"jcwhryfs":"","jchbryfs":"","xjzd":"","szgj":"","sfsfbh":"0","jhfjrq":"","jhfjjtgj":"","jhfjhbcc":"","jhfjsftjwh":"0","jhfjsftjhb":"0","szsqsfybl":"0","sfygtjzzfj":"0","gtjzzfjsj":"","sfsqhzjkk":"0","sqhzjkkys":""},
    }
  });

</script>
</body>

</html>
'''

POST_DATA_OLD = {
    'address': '上海市黄浦区南京东路街道延安东路凯迪拉克·上海音乐厅(装修中)',
    'area': '上海市  黄浦区',
    'bztcyy': '',
    'city': '上海市',
    'created': '1145141919',
    'created_uid': '0',
    'date': '20200303',
    'fjsj': '0',
    'fxyy': '',
    'geo_api_info': '{"type":"complete","position":{"P":31.22847357856,"O":121.47822401258702,"lng":121.478224,"lat":31.228474},"location_type":"html5","message":"Get '
                    'ipLocation failed.Get geolocation success.Convert '
                    'Success.Get address '
                    'success.","accuracy":150,"isConverted":true,"status":1,"addressComponent":{"citycode":"021","adcode":"310101","businessAreas":[{"name":" '
                    '新天地(自忠路)","id":"310101","location":{"P":31.220028,"O":121.47492399999999,"lng":121.474924,"lat":31.220028}},{"name":"城隍庙","id":"310101","location":{"P":31.225435,"O":121.492975,"lng":121.492975,"lat":31.225435}}],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"延安东路","streetNumber":"630号","province":"上海市","city":"","district":"黄浦区","township":"南京东路街道"},"formattedAddress":"上海市黄浦区南京东路街道延安东路凯迪拉克·上海 '
                    '音乐厅(装修中)","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
    'glksrq': '',
    'gllx': '',
    'gtjzzfjsj': '',
    'id': '114514',
    'ismoved': '0',
    'jcbhlx': '',
    'jcbhrq': '',
    'jchbryfs': '',
    'jcjg': '',
    'jcjgqr': '0',
    'jcqzrq': None,
    'jcwhryfs': '',
    'jhfjhbcc': '',
    'jhfjjtgj': '',
    'jhfjrq': '',
    'jhfjsftjhb': '0',
    'jhfjsftjwh': '0',
    'province': '上海市',
    'qksm': '',
    'remark': '',
    'sfcxtz': '0',
    'sfcxzysx': '0',
    'sfcyglq': '0',
    'sfjcbh': '0',
    'sfjchbry': '0',
    'sfjcqz': '',
    'sfjcwhry': '0',
    'sfsfbh': '0',
    'sfsqhzjkk': '0',
    'sftjhb': '0',
    'sftjwh': '0',
    'sfygtjzzfj': '0',
    'sfyyjc': '0',
    'sfzx': '0',
    'sqhzjkkys': '',
    'szgj': '',
    'szsqsfybl': '0',
    'tw': '3',
    'uid': '1919',
    'xjzd': '',
}

POST_DATA_NEW = {
    'address': '',
    'area': '',
    'bztcyy': '',
    'city': '',
    'created': '2331919931',
    'date': '20200303',
    'fjsj': '0',
    'fxyy': '',
    'geo_api_info': '{"type":"complete","position":{"P":31.22847357856,"O":121.47822401258702,"lng":121.478224,"lat":31.228474},"location_type":"html5","message":"Get '
                    'ipLocation failed.Get geolocation success.Convert '
                    'Success.Get address '
                    'success.","accuracy":150,"isConverted":true,"status":1,"addressComponent":{"citycode":"021","adcode":"310101","businessAreas":[{"name":" '
                    '新天地(自忠路)","id":"310101","location":{"P":31.220028,"O":121.47492399999999,"lng":121.474924,"lat":31.220028}},{"name":"城隍庙","id":"310101","location":{"P":31.225435,"O":121.492975,"lng":121.492975,"lat":31.225435}}],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"延安东路","streetNumber":"630号","province":"上海市","city":"","district":"黄浦区","township":"南京东路街道"},"formattedAddress":"上海市黄浦区南京东路街道延安东路凯迪拉克·上海 '
                    '音乐厅(装修中)","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
    'glksrq': '',
    'gllx': '',
    'gtjzzfjsj': '',
    'gwszdd': '',
    'id': '810810',
    'jcbhlx': '',
    'jcbhrq': '',
    'jchbryfs': '',
    'jcjg': '',
    'jcjgqr': '0',
    'jcqzrq': '',
    'jcwhryfs': '',
    'jhfjhbcc': '',
    'jhfjjtgj': '',
    'jhfjrq': '',
    'jhfjsftjhb': '0',
    'jhfjsftjwh': '0',
    'jrdqjcqk': [],
    'jrdqtlqk': [],
    'jrsfqzfy': '',
    'jrsfqzys': '',
    'province': '上海市',
    'qksm': '',
    'remark': '',
    'sfcxtz': '0',
    'sfcxzysx': '0',
    'sfcyglq': '0',
    'sfjcbh': '0',
    'sfjchbry': '0',
    'sfjcqz': '',
    'sfjcwhry': '0',
    'sfsfbh': '0',
    'sfsqhzjkk': '',
    'sftjhb': '0',
    'sftjwh': '0',
    'sfygtjzzfj': 0,
    'sfyqjzgc': '',
    'sfyyjc': '0',
    'sfzx': '0',
    'sqhzjkkys': '',
    'szgj': '',
    'szsqsfybl': 0,
    'tw': '3',
    'uid': '93111',
    'xjzd': '',
}

POST_DATA_FINAL = {
    'address': '上海市黄浦区南京东路街道延安东路凯迪拉克·上海音乐厅(装修中)',
    'area': '上海市  黄浦区',
    'bztcyy': '',
    'city': '上海市',
    'created': '2331919931',
    'created_uid': '0',
    'date': '20200303',
    'fjsj': '0',
    'fxyy': '',
    'geo_api_info': '{"type":"complete","position":{"P":31.22847357856,"O":121.47822401258702,"lng":121.478224,"lat":31.228474},"location_type":"html5","message":"Get '
                    'ipLocation failed.Get geolocation success.Convert '
                    'Success.Get address '
                    'success.","accuracy":150,"isConverted":true,"status":1,"addressComponent":{"citycode":"021","adcode":"310101","businessAreas":[{"name":" '
                    '新天地(自忠路)","id":"310101","location":{"P":31.220028,"O":121.47492399999999,"lng":121.474924,"lat":31.220028}},{"name":"城隍庙","id":"310101","location":{"P":31.225435,"O":121.492975,"lng":121.492975,"lat":31.225435}}],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"延安东路","streetNumber":"630号","province":"上海市","city":"","district":"黄浦区","township":"南京东路街道"},"formattedAddress":"上海市黄浦区南京东路街道延安东路凯迪拉克·上海 '
                    '音乐厅(装修中)","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
    'glksrq': '',
    'gllx': '',
    'gtjzzfjsj': '',
    'id': '810810',
    'ismoved': '0',
    'jcbhlx': '',
    'jcbhrq': '',
    'jchbryfs': '',
    'jcjg': '',
    'jcjgqr': '0',
    'jcqzrq': None,
    'jcwhryfs': '',
    'jhfjhbcc': '',
    'jhfjjtgj': '',
    'jhfjrq': '',
    'jhfjsftjhb': '0',
    'jhfjsftjwh': '0',
    'province': '上海市',
    'qksm': '',
    'remark': '',
    'sfcxtz': '0',
    'sfcxzysx': '0',
    'sfcyglq': '0',
    'sfjcbh': '0',
    'sfjchbry': '0',
    'sfjcqz': '',
    'sfjcwhry': '0',
    'sfsfbh': '0',
    'sfsqhzjkk': '0',
    'sftjhb': '0',
    'sftjwh': '0',
    'sfygtjzzfj': '0',
    'sfyyjc': '0',
    'sfzx': '0',
    'sqhzjkkys': '',
    'szgj': '',
    'szsqsfybl': '0',
    'tw': '3',
    'uid': '93111',
    'xjzd': '',
}

POST_DATA_SICK_ITEMS = {
    'jcjgqr': 1,
    'remark': '噔 噔 咚',
    'sfcxtz': 1,
    'sfcxzysx': 1,
    'sfcyglq': 1,
    'sfjcbh': 1,
    'ismoved': 1,
    'sfjchbry': 1,
    'sfjcwhry': 1,
    'sftjhb': 1,
    'sftjwh': 1,
    'sfyyjc': 1,
    'sfsfbh': 1,
    'tw': 6,
    'jcbhlx': '野兽',
    'jcbhrq': '114514年',
    'gllx': '居家（指野兽邸）',
    'glksrq': '114514年',
    'jcjg': '昏睡',
    'qksm': '二 人 幸 终',
}
