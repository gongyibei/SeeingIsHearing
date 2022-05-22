import numpy as np
from .modal import odf
from .modal.odf import SpectralDifferenceODF

class RTOnsetDetection(object):
    def __init__(self):
        self.prev_values = np.zeros(10)
        self.threshold = 0.1
        self.mean_weight = 2.0
        self.median_weight = 1.00
        self.median_window = 7
        self.largest_peak = 0.0
        self.noise_ratio = 0.05
        self.max_threshold = 0.05

    def is_onset(self, odf_value, max_value=0, return_threshold=False):
        result = False

        if ((self.prev_values[-1] > self.threshold) and
            (self.prev_values[-1] > odf_value) and
            (self.prev_values[-1] > self.prev_values[-2])):
            if max_value:
                if odf_value > self.max_threshold * max_value:
                    result = True
            else:
                result = True

        # update threshold
        self.threshold = ((self.median_weight * np.median(self.prev_values)) +
                          (self.mean_weight * np.mean(self.prev_values)) +
                          (self.noise_ratio * self.largest_peak))

        # update values
        self.prev_values = np.hstack((self.prev_values[1:], odf_value))
        if result:
            if self.prev_values[-2] > self.largest_peak:
                self.largest_peak = self.prev_values[-2]
        if return_threshold:
            return result, self.threshold
        else:
            return result

class OnsetDetector(RTOnsetDetection):
    def __init__(self, sample_rate=16000, frame_size=128):
        super().__init__()
        #  self.odf = SpectralDifferenceODF()
        #  self.odf = odf.EnergyODF()
        #  self.odf = odf.ComplexODF()
        self.odf = odf.EnergyODF()
        self.odf.set_frame_size(frame_size)

    def __call__(self, frame):
        odf_val = self.odf.process_frame(frame)
        return self.is_onset(odf_val)


if __name__ == '__main__':
    detector = RTOnsetDetection()
