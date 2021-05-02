import requests,json,random
import urllib.parse
from datetime import datetime
agent=[
"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
"Mozilla/5.0 (X11; FreeBSD i386) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2"
]

username=input("Username => ")
password=input("Password => ")
   
csrf="csrftoken="
hash1=""

time = int(datetime.now().timestamp())
not_following=[]

login_url = 'https://www.instagram.com/accounts/login/ajax/'
q1=f"https://www.instagram.com/graphql/query/?query_hash={hash1}&variables="

payload = {
    'username': username,
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{password}',
    'queryParams': {},
    'optIntoOneTap': 'false'
}
login_header = {
    "User-Agent": random.choice(agent),    
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/accounts/login/",
    "x-csrftoken": csrf
}

with requests.Session() as r:
   login_response = r.post(login_url, data=payload, headers=login_header)
   print(login_response.text+"\n\n")
   j=json.loads(login_response.text)
   id1=j["userId"]
   
   q2='{"id":"{id1}","include_reel":false,"fetch_mutual":false,"first":2000}'.replace('{id1}',id1)
   q3=urllib.parse.quote(q2)
   q4=q1+q3
   
   id_response=r.get(q4)
   json_data = json.loads(id_response.text)
   data_len=json_data["data"]["user"]["edge_follow"]["count"]
   
   for i in range(data_len):
    u1=json_data["data"]["user"]["edge_follow"]["edges"][i]["node"]["username"]
    f1=json_data["data"]["user"]["edge_follow"]["edges"][i]["node"]["follows_viewer"]
    if not f1:
      not_following.append(u1)
   print(f"\nFollowing => {data_len}\n\nNot Following \n {not_following}")
