from text_collection_and_summarizer import newsapi
from summarize import summarizer
from audio_convert import audio_converter


def load_all_the_models():
    summarizer.load_model
    audio_converter.model_load

def api_and_json_extraction(interests):
    list_of_all_the_json_filepaths = newsapi.newsapi_fun(interests)
    
    
# def 
# summarizer.file_load()

# audio_converter.converter(text)
