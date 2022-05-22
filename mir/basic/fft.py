import numpy as np

class RTFFT():
    def __init__(self, low_freq=200, high_freq=300, sample_rate=16000, frame_size=128, ration=0.5):

        self.sample_rate = sample_rate
        self.frame_size = frame_size

        self.low_freq = low_freq
        self.high_freq= high_freq
        self.low_idx = int(low_freq/(self.sample_rate/self.frame_size))
        self.high_idx = max(int(high_freq/(self.sample_rate/self.frame_size)), self.low_idx)

        self.ration=0.5
    
    def __call__(self, frame):
        feat = np.abs(np.fft.fft(frame))**2
        feat = sum(feat[self.low_idx:self.high_idx])/(self.high_idx - self.low_idx)
        feat = int(feat ** self.ration/100)
        feat = min(int(feat), 255)
        return feat
