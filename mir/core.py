import sys
import time 
import os
import threading
import numpy as np
import random
import socket
import math

class MIR():
    def __init__(self, Proceccer, sample_rate=16000, frame_size=128, dtype='int16'): 
        # basic config
        self.sample_rate = sample_rate
        self.frame_size = frame_size
        self.dtype = dtype
        self.dtype_size = np.dtype(self.dtype).itemsize
        self.music_stream = os.fdopen(sys.stdin.fileno(), 'rb', buffering=0)
        self.feature_stream = os.fdopen(sys.stdout.fileno(), 'wb', buffering=0)

        # init frame proceccer
        self.precess = Proceccer

        # syncing the music stream
        threading.Thread(target=self.sync).start()

    def sync(self):
        while 1:
            self.music_stream.read()

    def data_to_frame(self, data):
        data = data[:len(data)//self.dtype_size*self.dtype_size]
        data = np.frombuffer(data, dtype=self.dtype)
        #  frame = np.zeros((self.frame_size), dtype=self.dtype)
        #  frame[:len(data)] = data
        frame = np.pad(data, (0, self.frame_size - len(data)))
        return frame

    def run(self):
        while 1:
            data = self.music_stream.read(self.frame_size*self.dtype_size)
            frame = self.data_to_frame(data)
            feature = self.precess(frame)
            self.feature_stream.write(bytes([feature]))