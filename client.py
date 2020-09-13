from socketio import AsyncClient
import asyncio
import time
from json import dumps
from aioconsole import ainput
from colorama import Fore, Back, Style 
from os import system, name

def clear(): 
    if name == 'nt': 
        _ = system('cls')
        print(Fore.WHITE)
    else: 
        _ = system('clear')
        print(Fore.WHITE)


if __name__ == '__main__':
    clear()
    severInfo = input("Server Adress > ")
    IpAddress = severInfo[:-5]
    PORT = severInfo[-4:]
    #IpAddress = "192.168.1.110"
    #PORT = "8080"
    clientName = input("Username > ")
    #roomName = input("Room Name > ")
    roomName = "marvel"
    messageToSend = ''

    sio = AsyncClient()
    FullIp = 'http://'+IpAddress+':'+PORT

    @sio.event
    async def connect():
        print('Sent Join request')
        await sio.emit('join_chat', {'room': roomName,'name': clientName, })
    
    @sio.event
    async def get_message(message):
        if clientName != message['from']:
            print(Fore.CYAN + message['from']+' : '+message['message'] + Fore.GREEN)


    async def send_message():
        while True:
            await asyncio.sleep(0.01)
            messageToSend = await ainput(Fore.GREEN)
            if messageToSend == ":q":
                print(Fore.WHITE)
                clear()
                exit()
            elif messageToSend == ":c":
                clear()
            if messageToSend != "":
                await sio.emit('send_chat_room', {'message': messageToSend,'name': clientName, 'room': roomName})

    async def connectToServer():
        try:
            await sio.connect(FullIp)
        except:
            print("Request not accepted")
        await sio.wait()

    async def main(IpAddress):
        await asyncio.gather(
        connectToServer(),
        send_message()
        )
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(FullIp))