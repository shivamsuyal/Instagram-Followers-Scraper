import requests,json
import urllib.parse
from datetime import datetime

username=input("Username => ")
password=input("Password => ")
if username=="":
   username="crazy_timepasser"
if password=="":
   password="*blAck07ice#"

csrf="csrftoken=syX1Uw4CvWZdzoFXu06u549hTFuX4Ghm"
hash1="3dec7e2c57367ef3da3d987d89f9dbc8"

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
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",    
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
   print(f"(*) Followers \n")
   for i in range(data_len):
      u1=json_data["data"]["user"]["edge_follow"]["edges"][i]["node"]["username"]
      f1=json_data["data"]["user"]["edge_follow"]["edges"][i]["node"]["follows_viewer"]
      if not f1:
         not_following.append(u1)
      print(u1)
      print(f1)
      print("")
   print(f"Not Following \n {not_following}")

   
