import asyncio
import socketio
from aioconsole import ainput
sio = socketio.AsyncClient()


@sio.event
async def connect():
    print('connected to server')


@sio.event
async def disconnect():
    print('disconnected from server')

@sio.on("message")
async def user_message(data):
    print('message received with ', data)


@sio.event
def hello(a, b, c):
    print(a, b, c)


async def start_server():
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(sio.connect('ws://127.0.0.1:5000/socket.io/'))
    await sio.connect('http://127.0.0.1:5000/socket.io/')

    w = asyncio.create_task(sio.wait())  #background task to process the event
    u = asyncio.create_task(clientMsg())
    await asyncio.gather(u, w)
    await sio.disconnect() #release any resource in sio

    #await clientMsg()
    #loop.run_until_complete(sio.disconnect())


async def clientMsg():
    try:
        userinput = ''
        while userinput != "exit":
            userinput = await ainput("Enter some text:")
            await sio.emit('message', userinput)
            #sio.wait()
    except :
        pass
    finally:        
        await sio.disconnect() #trig wait task to end
        pass


if __name__ == '__main__':
    asyncio.run(start_server())
    #asyncio.get_event_loop().run_until_complete(asyncio.wait([start_server(),clientMsg()]))