import threading

global_vars = {}

global mutex

'''
访问全局变量的过程不能并行，也就是说同一时间只能有有一个访问的线程
'''

#初始化设备锁
def globalvars_init():
    global mutex
    mutex = threading.Lock()

#set a var as a global var
def setGlobalVar(key, value):
    global mutex
    mutex.acquire()
    global_vars[key] = value
    mutex.release()


#read a global var
def readGlobalVar(key):
    global mutex
    try:
        mutex.acquire()
        data = global_vars[key]
        mutex.release()

    except:
        #这里如果不加变量锁在第二次读取时候会出错
        mutex.release()
        return None

    return data

#read a global var
def readAllGlobalVar():
    global mutex
    try:
        mutex.acquire()
        data = global_vars
        mutex.release()

    except:
        #这里如果不加变量锁在第二次读取时候会出错
        mutex.release()
        return None

    return data





