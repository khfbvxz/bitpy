import requests

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "5b5b0de382af2255b6ab71085b60dadf",
    "redirect_uri" : "https://localhost.com",
    "code" : "5fhGMlccKOirypcocR5ZJ3pTFncjCBsiNSSgFbVo59ZA3ye3AH_iOHtMSQs0IolrTl3hgopcSEAAAF64l6jYg"
}          # code 발급받은 코드를 입력하세요

response = requests.post(url,data=data) m

if response.status_code != 200:
    print("error because ", response.json())

else:
    tokens = response.json()
    print(tokens)