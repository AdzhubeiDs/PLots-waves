import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

E=2.71828

types = {
    1: np.int8,
    2: np.int16,
    4: np.int32
}

def format_time(x, pos=None):
    global duration, nframes, k
    progress = int(x / float(nframes) * duration * k)
    mins, secs = divmod(progress, 60)
    hours, mins = divmod(mins, 60)
    out = "%d:%02d" % (mins, secs)
    if hours > 0:
        out = "%d:" % hours
    return out

def format_db(x, pos=None):
    if pos == 0:
        return ""
    global peak
    if x == 0:
        return "0"

    db = 20 * math.log10( (peak+x)/float(peak))
    return int(db)

for file in ['1.wav', '2.wav', '3.wav', '4.wav', '5.wav']:
    wav = wave.open(file, mode="r")
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    print(nchannels, sampwidth, framerate, nframes, comptype, compname)
    duration = nframes / framerate
    w, h = 1500, 8000
    k = int(nframes/w/32)
    DPI = 72
    peak = 256 ** sampwidth / 2

    content = wav.readframes(nframes)
    samples = np.fromstring(content, dtype=types[sampwidth])

    # plt.figure(1, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)
    plt.subplots_adjust(wspace=0, hspace=10)


    max_index = np.argmax(samples)
    channel = samples[max_index:300000:nchannels]

    fig, axes = plt.subplots(2, 1, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI)
    axes[0].plot(channel, "b")
    print(np.where(channel==-100000))

    # A2=int(channel[0]/E)
    # print (A2)

    # index_other=np.where(channel==A2)[0][0]



    # axes[0].scatter(1, channel[0])
    # axes[0].scatter(index_other, channel[0]/E)

    #y2 = np.exp([i for i in range(1, len(channel))])
    axes[0].yaxis.set_major_formatter(ticker.FuncFormatter(format_db))
    plt.grid(True, color="w")
    axes[0].xaxis.set_major_formatter(ticker.NullFormatter())

    #сетка основная и второстепенная
    axes[0].grid(which='major', color = 'k')
    axes[0].minorticks_on()
    axes[0].grid(which='minor', color = 'gray', linestyle = ':')
    axes[0].xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
    axes[0].set_xlabel(r"$Time, s$", fontsize=20)


    from scipy.fft import rfft, rfftfreq

    yf = rfft(channel)
    yf=yf/yf[np.argmax(yf)]
    xf = rfftfreq(len(channel), 1/framerate)

    axes[1].text(np.argmax(yf), np.argmax(yf), "533 Hz", fontsize=20)

    print(len(xf),xf[np.argmax(yf)])
    axes[1].plot(xf[np.argmax(yf) - 1000:np.argmax(yf) + 1000], np.abs(yf)[np.argmax(yf) - 1000:np.argmax(yf) + 1000])
    axes[1].grid(which='major', color = 'k')
    axes[1].minorticks_on()
    axes[1].grid(which='minor', color = 'gray', linestyle = ':')

    axes[1].set_xlabel(r"$Frequency, Hz$", fontsize=20)

plt.show()
