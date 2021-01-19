from gtts import gTTS
f = open("a.txt")
a = f.read()
audio = gTTS(text=a, lang='en')
audio.save("1.wav")
