import requests
import streamlit as st
import json

def get_weibo_hot():
    url = st.secrets['weibo_url']  # 替换为你的URL
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Cookie': 'SINAGLOBAL=2128193978488.887.1660469474909; ULV=1732111908174:12:2:1:939865974759.3496.1732111908143:1730876945182; SCF=AgQwxuDH5oSKeJjeGvfSzkKyl-XqpTLxAf5L_PrnX5UriOJp7GNYg2KBU7A_9DQLKNvF7B3uliP5eRTSIEniLd4.; UOR=,,www.baidu.com; SUB=_2AkMQP01Lf8NxqwFRmfsWy2rra4VywgHEieKmY7yQJRMxHRl-yT9kqlMktRB6O79jpBGUm9zq7doRncoPEfcLjGBnebQJ; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFVozIhiCSbo_lWRnTSksT6; WBPSESS=gJ7ElPMf_3q2cdj5JUfmvJ5R3yudaCqeqPFtWIYxbCkZKqmLs2U-cOAXqYqRv4SqbSAT6KkFnyoLk0UaahBzkd0o3tWK0AtDmSdoU5k1bEmO32uOOiHAMvnVk8ztVAX0KpRd-UVYtfHZkIRNlDvCSpL7NJ_oU9ta0CCVa-mcdpM=; XSRF-TOKEN=tCtSIElsejzTCc6xBoO5lN6J',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0',

    }
    response = requests.get(url,headers=headers)

    if response.ok == 1:
        realtime = response.json()['data']['realtime']
        # realtime_json = json.dumps(realtime,ensure_ascii=False, indent=4)
        new_data = [{"word": item["word"], "num": item["num"]} for item in realtime]
        # new_json = json.dumps(new_data, ensure_ascii=False, indent=4)
        # print(new_data)
        return new_data

    else:
        print("请求失败")