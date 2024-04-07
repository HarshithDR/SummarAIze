from Backend.summaraize_app.audio_convert import text_to_audio_converter, caption_creater_and_video_audio_merger


def final_video_creater():
    video_path = caption_creater_and_video_audio_merger.start()
    
video_path = final_video_creater()