# from TTS.api import TTS

# # class model_load:
# #     tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
    
# def converter(text):
#     tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)
#     tts.tts_to_file(text=text,
#                 file_path="Backend/summaraize_app/audio_convert/temp_files/output_audio.mp4",
#                 speaker_wav="Backend\\summaraize_app\\audio_convert\\reference_voice.wav",
#                 language="en")
#     return True


import os
import uuid
from gtts import gTTS 
from datetime import datetime
 
def text_to_speech(text):
    try:
        if not os.path.exists('audio_files'):
            os.makedirs('audio_files')
    
        unique_filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex}.mp3"
        file_path = os.path.join('audio_files',unique_filename)
        
        tts_model = gTTS(text=text, lang='en', slow=True) # Change to false if faster version is needed
        
        tts_model.save(file_path)
        
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    audio_text = "This is a demo text adn replace this thing with the output from summarized chatbot"
    text_to_speech(audio_text)



