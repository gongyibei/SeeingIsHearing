import sys
import time 
import os
import threading
import numpy as np
import random
import socket
import scipy.io.wavfile as wav
import imageio


# Music visualizer
class SuperMario():
    def __init__(self):
        self.sr = 16000
        self.frame_size = 128
        self.stream = os.fdopen(sys.stdin.fileno(), 'rb', buffering=0)

        # setup udp clinet
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self.addr = ('192.168.31.7', 1234)

        # onset detector

        # syncing the music stream
        threading.Thread(target=self.sync).start()
        self.imgs = self.get_imgs()
    
    def get_imgs(self):
        im = imageio.mimread('./8pic.gif')[0][:, :, :3]
        imgs = []
        for i in range(10):
            for j in range(10):
                width = 8
                row = 6 + i * 12
                col = 6 + j * 12 
                img = im[row*6:(row + width)*6, col*6:(col + width)*6][::6, ::6]
                img = img.transpose((1, 0, 2))
                img[1::2] = img[1::2][:, ::-1]
                img = img.reshape(-1)
                img = bytes(img)
                imgs.append(img)

        return imgs

    def sync(self):
        while 1:
            self.stream.read()

    def run(self):
        while 1:
            time.sleep(0.05)
            feat = self.stream.read(1)
            # print(feat)
            for _ in range(ord(feat)):
                i = random.randint(0 ,12)
                extra = bytes([0, 0, 0]*8*i*2)
                self.client.sendto(extra + self.imgs[0], self.addr)
            # feat = ord(feat)
            # print(feat)
            # for i in range(min(feat, 20)):
            #     extra = bytes([0, 0, 0]*8*i*2)
            #     self.client.sendto(extra + self.imgs[0], self.addr)
SuperMario().run()
