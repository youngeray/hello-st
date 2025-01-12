import requests
import json

def get_thepaper_hot():
    url = 'https://cache.thepaper.cn/contentapi/wwwIndex/rightSidebar'  # 替换为你的URL
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Cookie': 'ariaDefaultTheme=undefined',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0',

    }
    response = requests.get(url,headers=headers)

    if response.json()['resultMsg'] == '操作成功':
        data = response.json()['data']['hotNews']
        # realtime_json = json.dumps(realtime,ensure_ascii=False, indent=4)
        new_data = [{
            "name": item["name"], 
            "smallPic": item["smallPic"], 
            "url": item.get('videos',{}).get('url',''),
            "tagList":[i['tag'] for i in item.get('tagList',{})]
        
        } for item in data]
        # new_json = json.dumps(new_data, ensure_ascii=False, indent=4)
        print(new_data)
        return new_data

    else:
        return("请求失败")

