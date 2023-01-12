import wave
import numpy as np
import matplotlib.pyplot as plt


types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}
i=0
DPI = 72
w, h = 1500, 8000
plt.subplots_adjust(wspace=0, hspace=10)
fig, axes = plt.subplots(1, 5, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)


for file in ['1.wav', '2.wav', '3.wav', '4.wav', '5.wav']:
    wav = wave.open(file, mode="r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    #print(nchannels, sampwidth, framerate, nframes, comptype, compname)

    duration = nframes / framerate

    content = wav.readframes(nframes)
    samples = np.fromstring(content, dtype=types[sampwidth])

    max_index = np.argmax(samples)
    channel = samples[max_index:250000:nchannels]
    from scipy.fft import rfft, rfftfreq

    yf = rfft(channel)
    yf = yf / yf[np.argmax(yf)]
    xf = rfftfreq(len(channel), 1 / framerate)

    print(len(xf), xf[np.argmax(yf)])

    axes[i].plot(xf[np.argmax(yf) - 1000:np.argmax(yf) + 1000], np.abs(yf)[np.argmax(yf) - 1000:np.argmax(yf) + 1000])
    axes[i].grid(which='major', color='k')
    axes[i].minorticks_on()
    axes[i].grid(which='minor', color='gray', linestyle=':')
    axes[i].set_xlabel(r"$Frequency, Hz$", fontsize=12)
    i += 1

plt.show()