import requests, sys
from datetime import datetime, timedelta

UUID = "8971ce71e31c4142bbf238785a4b82f7" #https://api.mojang.com/users/profiles/minecraft/<username>?at=0 <- to find out UUID
AccessToken = "" #bearer_token
Auth = "Bearer " + AccessToken
username = "3CE" #target IGN
password = "" #account password
dropTime = "15:05:07" #example of time format

while True:
    now = datetime.now()
    now = str(now)
    parts = now.split()
    parts1 = parts[1]
    exacTime = parts1.split(".")
    if (exacTime[0] == dropTime):
        s = requests.post(f'https://api.mojang.com/user/profile/{UUID}/name', headers = {'Authorization': Auth}, json = {"name": username,"password": password})
        if s.status_code == 204:
            print(username + " acquired!")
            sys.exit()
        else:
            print("Failure!")
            print(s.status_code)
            print(s.content)