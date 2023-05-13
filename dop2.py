from pydub import AudioSegment


s = AudioSegment.from_file("music.wav")
sf = s.speedup(1.5)
sf.export('music1.wav' , format= "wav")