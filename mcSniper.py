import aiohttp
import asyncio, sys
from datetime import datetime, timedelta

class playerInfo:
    def __init__(self, UUID, Bearer_Key, Target_IGN, Password, dropTime):
        self.UUID = UUID
        self.Bearer_Key = Bearer_Key
        self.Target_IGN = Target_IGN
        self.Password = Password
        self.dropTime = dropTime

def conformation():
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

async def main():
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
            if __name__ == '__main__':
                loop = asyncio.get_event_loop()
                loop.run_until_complete(main())

elif choice.lower() == "n":
    sys.exit()
