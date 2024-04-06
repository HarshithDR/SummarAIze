from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# generate speech by cloning a voice using default settings
tts.tts_to_file(text="Nischal says we will win and I believe it",
                file_path="output.wav",
                speaker_wav="speaker.wav",
                language="en")