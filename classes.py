import aiohttp
import asyncio, sys, time, requests
from datetime import datetime, timedelta

class playerInfo: #class to store data
    def __init__(self, UUID, Bearer_Key, Target_IGN, Password, dropTime):
        self.UUID = UUID
        self.Bearer_Key = Bearer_Key
        self.Target_IGN = Target_IGN
        self.Password = Password
        self.dropTime = dropTime

def nameReserveConformation(): #getting user info
    global Target_IGNR
    global bearerKey
    global auth
    global dropTimeR
    bearerKey = input("Enter Bearer Key: ")
    Target_IGNR = input("Enter your desired IGN: ")
    dropTimeR = input("Enter the time of IGN release: ")
    auth = "Bearer " + bearerKey

def conformation(): #getting user info
    global Target_IGN
    global dropTime
    global Bearer_Key
    global Password
    global playerInfo1
    UUID = input("Enter your UUID: ")
    Bearer_Key = input("Enter your Bearer_Key: ")
    Target_IGN = input("Enter your desired IGN: ")
    Password = input("Enter your account password: ")
    dropTime = input("Enter the time of drop: ")
    playerInfo1 = playerInfo(UUID, Bearer_Key, Target_IGN, Password, dropTime)
    print(f"UUID: [{playerInfo1.UUID}]\nBearer Key: [{playerInfo1.Bearer_Key}]\nDesired IGN: [{playerInfo1.Target_IGN}]\nPassword: [{playerInfo1.Password}]\nDrop Time: [{playerInfo1.dropTime}]")

def login():
    print("[*] Login...")
    time.sleep(1)
    user = input("[*] Enter Username: ")
    url = f"https://api.mojang.com/users/profiles/minecraft/{user}?at=0"
    req = requests.get(url)
    print(req.content)
    correct = input("[*] Does this UUID match yours? Y/n: ")
    if correct.lower() == "y":
        print("[*] Success")
    if correct.lower() == "n":
        sys.exit()

async def main(): #sniping function
    global auth
    auth = "Bearer " + playerInfo1.Bearer_Key
    async with aiohttp.ClientSession() as session:
        async with session.post(f'https://api.mojang.com/user/profile/{playerInfo1.UUID}/name', headers = {'Authorization': auth}, json = {"name": playerInfo1.Target_IGN,"password": playerInfo1.Password}) as resp:
            print(await resp.text())
            x = resp.status
    if x == 204:
        print(f"{Target_IGN} Acquired!")
    else:
        print(x)
        print("Failure!")

async def reserve():
    global origin
    origin = "https://www.checkout.minecraft.net"
    async with aiohttp.ClientSession() as session:
        async with session.put(f"https://api.mojang.com/user/profile/agent/minecraft/name/{Target_IGNR}", headers = {"Authorization": auth,"Origin": origin}) as resp:
            print(await resp.text())
            x = resp.status
        if x == 204:
            print(f"{Target_IGNR} Reserved!")
        else:
            print(x)
            print("Failiure!")

if __name__ == '__main__':
    login()
    choice = input("Would you like to use the IGN Sniper? Y/n: ")
    if choice.lower() == "y":
        conformation()
        print(f"Sniping {Target_IGN} at {dropTime}...")
        while True:
            now = datetime.now()
            now = str(now)
            parts = now.split()
            parts1 = parts[1]
            exacTime = parts1.split(".")
            time = exacTime[0]
            if time != dropTime:
                pass        
            elif time == dropTime:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(main())

    elif choice.lower() == "n":
        choice1 = input("Would you like to use the name reserver? Y/n: ")
        if choice1.lower() == "y":
            nameReserveConformation()
            print(f"Reserving {Target_IGNR} at {dropTimeR}...")
            while True:
                now = datetime.now()
                now = str(now)
                parts = now.split()
                parts1 = parts[1]
                exacTime = parts1.split(".")
                time = exacTime[0]
                if time != dropTimeR:
                    pass        
                elif time == dropTimeR:
                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(reserve())