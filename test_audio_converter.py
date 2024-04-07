from Backend.summaraize_app.audio_convert import text_to_audio_converter, caption_creater_and_video_audio_merger

def audio_conv(summary):
    text_to_audio_converter.converter(summary)
 
summary = 'Your max_length is set to 100, but your input_length is only 9. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually'    
audio_conv(summary)