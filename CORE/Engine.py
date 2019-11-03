import random
from subprocess import PIPE, STDOUT, Popen
from time import sleep
import cv2


class Log:
    @staticmethod
    def record(mes: str):
        print(mes)


class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Region:
    def __init__(self, point1: Point, point2: Point):
        self._point1 = point1
        self._point2 = point2

    @property
    def random_point(self) -> Point:
        """
        :return: 返回一个区域内的随机点
        """
        pos_x = random.random() * (self._point2.x - self._point1.x) + self._point1.x
        pos_y = random.random() * (self._point1.y - self._point2.y) + self._point2.y
        print(pos_x, pos_y)
        return Point(pos_x, pos_y)

    @property
    def pos_list(self) -> list:
        res = [self._point1.y, self._point2.y, self._point1.x, self._point2.x]
        return res


class AdbServer:
    ServerNumber = ''

    @staticmethod
    def start_server():
        mes_string = 'adb start-server'
        ShellServer.processor(mes_string)
        mes_string = 'adb devices'
        ShellServer.processor(mes_string, callback_message=True)
        AdbServer.SeverNumber = input(ShellServer.message[:-2] + '\nServerNumber(Enter To Default):')
        if AdbServer.ServerNumber != '':
            AdbServer.ServerNumber = '-s {0}'.format(AdbServer.ServerNumber)

    @staticmethod
    def kill_server():
        mes_string = 'adb kill-server'
        ShellServer.processor(mes_string)

    @staticmethod
    def tap(point: Point):
        mes_string = 'adb {0} shell input tap {1} {2}'.format(AdbServer.ServerNumber, point.x, point.y)
        ShellServer.processor(mes_string)

    @staticmethod
    def screen_cap():
        mes_string = 'adb {0} shell screencap -p /sdcard/buf.png'.format(AdbServer.ServerNumber)
        ShellServer.processor(mes_string)
        mes_string = 'adb {0} pull /sdcard/buf.png buf.png'.format(AdbServer.ServerNumber)
        ShellServer.processor(mes_string)

    @staticmethod
    def wait_second(sleep_time: float):
        sleep(sleep_time)


class ShellServer:
    message = ''

    @staticmethod
    def processor(order_string: str, callback_message=False):
        p = Popen(order_string, stdout=PIPE, stderr=STDOUT, shell=True)
        Popen.wait(p)
        if callback_message:
            ShellServer.message = p.stdout.read().decode('utf-8')


class BaseButton:
    def __init__(self, point1: Point, point2: Point):
        self._region = Region(point1, point2)

    @property
    def random_point(self) -> Point:
        return self._region.random_point


class BaseAsset:
    def __init__(self, point_1: Point, point_2: Point, hash_str: str):
        self._region = Region(point_1, point_2)
        self._hash_str = hash_str

    def match(self, limit: int = 10) -> bool:
        hash1 = self._hash_str
        hash2 = BaseAsset.hash(self.cut_img)
        n = 0
        for i in range(len(hash1)):
            if hash1[i] != hash2[i]:
                n = n + 1
        return n < limit

    @staticmethod
    def hash(image) -> str:
        image = cv2.resize(image, (8, 8), interpolation=cv2.INTER_CUBIC)
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        hash_str = ''
        for i in range(8):
            for j in range(7):
                if gray[i, j] > gray[i, j + 1]:
                    hash_str = hash_str + '1'
                else:
                    hash_str = hash_str + '0'
        return hash_str

    @property
    def cut_img(self):
        pos = self._region.pos_list
        img = cv2.imread('buf.png')[pos[0]:pos[1], pos[2]:pos[3]]
        return img


if __name__ == '__main__':
    AdbServer.start_server()
    AdbServer.screen_cap()
    asset = BaseAsset(Point(990, 290), Point(1150, 440),
                             '11101001101011111011010010110001011010001101001110001101')
    print('OK')
    print(BaseAsset.hash(asset.cut_img))
