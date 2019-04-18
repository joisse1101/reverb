import soundfile as sf
import pyloudnorm as pyln

"""
data, rate = sf.read("/home/pi/Desktop/419698__14fvaltrovat__short-horn.wav") # load audio (with shape (samples, channels))
meter = pyln.Meter(rate) # create BS.1770 meter
loudness = meter.integrated_loudness(data) # measure loudness
print(loudness)
"""

def detect_loudness(file_name):

    data, rate = sf.read(file_name) # load audio

    # peak normalize audio to -1 dB
    peak_normalized_audio = pyln.normalize.peak(data, -1.0)

    # measure the loudness first 
    meter = pyln.Meter(rate) # create BS.1770 meter
    loudness = meter.integrated_loudness(data)
    print("loundness: " + str(loudness))
    return loudness

    # loudness normalize audio to -12 dB LUFS
    #loudness_normalized_audio = pyln.normalize.loudness(data, loudness, -12.0)
    #loudness = meter.integrated_loudness(loudness_normalized_audio)
    #print(loudness)