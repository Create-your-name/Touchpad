from pynput import mouse
from pynput import keyboard
import time

import serial
import serial.tools.list_ports

import os

from lock import *
from cv import *
import threading

# os.system('osascript -e \'display notification "保持勇气，君子不器，不可被器" with title "KEEP BRAVE" subtitle "Jay MA" \'')

class CONTROL():
    def __init__(self):
        self.m = mouse.Controller()
        self.k = keyboard.Controller()
    def leftSpace2left(self):
        now = self.m.position
        self.m.position = (100, 100)
        self.k.press(keyboard.Key.ctrl)
        self.k.press('i')
        self.k.release('i')
        self.k.release(keyboard.Key.ctrl)
        time.sleep(0.1)
        self.m.position = now

    def leftSpace2right(self):
        now = self.m.position
        self.m.position = (100, 100)
        self.k.press(keyboard.Key.ctrl)
        self.k.press('o')
        self.k.release('o')
        self.k.release(keyboard.Key.ctrl)
        time.sleep(0.1)
        self.m.position = now

    def rightSpace2left(self):
        now = self.m.position
        self.m.position = (2000, 800)
        self.k.press(keyboard.Key.ctrl)
        self.k.press('i')
        self.k.release('i')
        self.k.release(keyboard.Key.ctrl)
        time.sleep(0.1)
        self.m.position = now

    def rightSpace2right(self):
        now = self.m.position
        self.m.position = (2000, 800)
        self.k.press(keyboard.Key.ctrl)
        self.k.press('o')
        self.k.release('o')
        self.k.release(keyboard.Key.ctrl)
        time.sleep(0.1)
        self.m.position = now

    def clear(self):
        self.k.press(keyboard.Key.ctrl_l)
        self.k.press('u')
        self.k.release('u')
        self.k.release(keyboard.Key.ctrl_l)

    def copy(self):
        self.k.press(keyboard.Key.cmd_l)
        self.k.press('c')
        self.k.release('c')
        self.k.release(keyboard.Key.cmd_l)
        os.system(
            'osascript -e \'display notification "复制成功" with title "Jazz提示" subtitle "" \'')

    def paste(self):
        self.k.press(keyboard.Key.cmd_l)
        self.k.press('v')
        self.k.release('v')
        self.k.release(keyboard.Key.cmd_l)


if __name__ == '__main__':

    globalvars_init()

    threading.Thread(target=camera).start()

    controler = CONTROL()

    ports_list = list(serial.tools.list_ports.comports())
    print("可用的串口", ports_list)

    ser = serial.Serial("/dev/tty.usbserial-14220", 115200)
    if ser.isOpen():  # 判断串口是否成功打开
        print("打开串口成功。")
        print(ser.name)  # 输出串口号
    else:
        print("打开串口失败。")

    com_input = b""

    rec_time = 300
    while True:
        try:
            start = time.time()
            com_input += ser.read(1)

            print(com_input)

            if com_input[-1] == 111:  # 如果读取结果非空，则输出
                com_input = com_input[:-1]
                print(com_input)

                # jama 旧的
                '''
                if com_input == b"12" or com_input == b"123":
                    controler.leftSpace2left()
                elif com_input == b"21" or com_input == b"321":
                    controler.leftSpace2right()
                elif com_input == b"34" or com_input == b"234":
                    controler.rightSpace2left()
                elif com_input == b"43" or com_input == b"432":
                    controler.rightSpace2right()
                elif com_input == b"1234":
                    controler.clear()
                # elif com_input == b"3" or com_input == b"4":
                #     controler.paste()
                '''
                # jama 旧的 over

                result = int(com_input[0]) - int(com_input[-1])
                which = readGlobalVar("which")

                if result < 0: # 右滑
                    if which == 'l':
                        controler.leftSpace2left()
                    elif which == 'r':
                        controler.rightSpace2left()
                else:
                    if which == 'l':
                        controler.leftSpace2right()
                    elif which == 'r':
                        controler.rightSpace2right()




                com_input = b''
        except KeyError:
            os.system(
                'osascript -e \'display notification "出现一个错误" with title "ERROR" subtitle "Jazz" \'')
            com_input = b""

    # ser.close()
    # ser.close()    # ser.close()    # ser.close()    # ser.close()    # ser.close()    # ser.close()












