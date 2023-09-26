import asyncio
import aiohttp
import socketio
#from threading import Thread

sio = socketio.Client() # 创建客户端实例
ut = "1"
#loop = asyncio.new_event_loop()

@sio.event
def connect():
    print('connection established')


# 监听服务端推送消息
@sio.event
def user_message(data):
    print('user_message received with ', data)
    # sio.emit('my response', {'response': 'my response'})

@sio.on("message")
def user_message(data):
    print('message received with ', data)
    #await sio.emit('json', {'response': 'my response'})


@sio.event
def disconnect():
    print('disconnected from server')


def clientMsg():
    userinput = ''
    while userinput != "exit":
        userinput = input("Enter some text:")
        sio.emit('message', userinput)
        #sio.wait()


def task(loop):
    # block for a moment
    asyncio.set_event_loop(loop)
    loop.run_until_complete(sio.wait())
    #await sio.wait()
    #await sio.disconnect()
    # display a message
    print('This is from another thread')

def main():
    # 连接服务端 IP+端口
    sio.connect('http://127.0.0.1:5000/socket.io/')
    print("000")

    #thread = Thread(target=task,args=(loop,))
    #thread.start()


    # 向服务端发送消息
    sio.emit('message', ut)
    #sio.wait()
    clientMsg()

    #sio.wait()
    sio.disconnect()

    # userinput = ''
    # while userinput != "exit":
    #     userinput = input("Enter some text:")
    #     await sio.emit('message', userinput)



if __name__ == '__main__':
    #asyncio.run(main())
    main()
