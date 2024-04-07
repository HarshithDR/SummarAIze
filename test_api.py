from Backend.summaraize_app.text_collection_and_summarizer import newsapi
from Backend.summaraize_app.summarize import summarizer
from Backend.summaraize_app.video_generation import video_generator
from Backend.summaraize_app.audio_convert import text_to_audio_converter, caption_creater_and_video_audio_merger


def api_and_json_extraction(interests):
    list_of_all_the_json_filepaths = newsapi.newsapi_fun(interests)
    return list_of_all_the_json_filepaths

print(list_of_all_json_filepaths = api_and_json_extraction('soccer'))
