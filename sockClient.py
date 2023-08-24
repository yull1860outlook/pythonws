import asyncio
import aiohttp
import socketio

sio = socketio.AsyncClient()
ut = "1"


@sio.event
async def connect():
    print('connection established')


# 监听服务端推送消息
@sio.event
async def user_message(data):
    print('user_message received with ', data)
    # sio.emit('my response', {'response': 'my response'})

@sio.on("message")
async def user_message(data):
    print('message received with ', data)
    #await sio.emit('json', {'response': 'my response'})


@sio.event
async def disconnect():
    print('disconnected from server')


async def clientMsg():
    userinput = ''
    while userinput != "exit":
        userinput = input("Enter some text:")
        await sio.emit('message', userinput)


async def main():
    # 连接服务端 IP+端口
    await sio.connect('http://127.0.0.1:5000/socket.io/')
    print("000")

    # 向服务端发送消息
    #await sio.emit('message', ut)
    await clientMsg()

    await sio.wait()
    await sio.disconnect()

    # userinput = ''
    # while userinput != "exit":
    #     userinput = input("Enter some text:")
    #     await sio.emit('message', userinput)



if __name__ == '__main__':
    asyncio.run(main())
