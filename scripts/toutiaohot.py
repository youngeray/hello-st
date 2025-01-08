import requests
import json

def get_toutiao_hot():
    url = 'https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc'  # 替换为你的URL
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Cookie': '__ac_signature=_02B4Z6wo00f01zSQQ-AAAIDC9rl8kb4y.Cc0oUdAAKpX33; ttwid=1%7CfGy6hSABREzjEKAR-9H01ZLaRrB0TKut5beeQIzG_Pc%7C1736304488%7C7bc809dd37e724b818a0bc148af4d52b67ff712533066aaeaaf7161175de7d3b; tt_webid=7451509075462931980; local_city_cache=%E5%BC%A0%E5%AE%B6%E5%8F%A3; ttcid=9ca5798799a842699871f0fc1e7424cc67; s_v_web_id=verify_m50qajhj_VqamBwGs_RWal_4jUa_BG1Q_fsEv2NqjMpDt; csrftoken=ebf12c363d4d8d3c52a35f4c99baadd4; gfkadpd=24,6457; tt_scid=IXeCE.yfS3393dbhpn6c8zQcYbvSIOhzUXF7nouhY0W2eTkPw0Mr.TKgg7Vt7pO5d617',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0',

    }
    response = requests.get(url,headers=headers)

    if response.json()['status'] == 'success':
        data = response.json()['data']
        # realtime_json = json.dumps(realtime,ensure_ascii=False, indent=4)
        new_data = [{"Title": item["Title"], "HotValue": item["HotValue"], "LabelUrl": item["LabelUrl"], "Url": item["Url"]} for item in data]
        # new_json = json.dumps(new_data, ensure_ascii=False, indent=4)
        # print(new_data)
        return new_data

    else:
        print("请求失败")