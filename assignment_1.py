from transformers import pipeline

transcriber = pipeline("automatic-speech-recognition", model = "openai/whisper-large-v2")
res = transcriber("https://ia801603.us.archive.org/35/items/DoNotGoGentleIntoThatGoodNight/gentle_64kb.mp3")

print(res)
