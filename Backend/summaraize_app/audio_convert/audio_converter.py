from TTS.api import TTS

class model_load:
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    
def converter(text):
    model_load.tts.tts_to_file(text="Nischal says we will win and I believe it",
                file_path="output.wav",
                speaker_wav="reference_voice.wav",
                language="en")
    return "reference_voice.wav"