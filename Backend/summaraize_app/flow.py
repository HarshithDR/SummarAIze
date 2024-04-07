from text_collection_and_summarizer import newsapi
from summarize import summarizer
from audio_convert import audio_converter
from video_generation import video_generator

def start():
    pass

def load_all_the_models():
    summarizer.load_model
    audio_converter.model_load

def api_and_json_extraction(interests):
    list_of_all_the_json_filepaths = newsapi.newsapi_fun(interests)


summarizer.file_load()
audio_converter.converter(text)
# prompt = "bitcoin"
print(video_generator.video_gen_fun(prompt))