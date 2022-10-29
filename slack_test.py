import os 
import requests
from dotenv import load_dotenv

load_dotenv()
myToken = os.environ.get('SLACK_API_TOKEN')

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={
#            "Content-type": "application/json",
            "Authorization": "Bearer "+token
        },
        json={
            "channel": channel,
            "blocks":[
           {
              "type":"section",
              "text":{
                 "type":"mrkdwn",
                 "text":text
              }
           }
        ]
#            "text":"왜안돼ㅜㅜ"
        }
    )
    print(response)

# 변화를 감지하면 Slack 알림을 보내는 함수
def catch_change(channel, contents, link):
    post_message(myToken, channel, f'{channel} 페이지에 새 공지사항이 올라왔어요!\n{contents}\n<{link}|바로가기>')

