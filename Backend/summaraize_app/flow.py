from text_collection_and_summarizer import newsapi
from summarize import summarizer
from audio_convert import audio_converter
from video_generation import video_generator
from dataclasses import dataclass


'''This class definition creates a data object 
with attributes json_url and video_url.'''
@dataclass
class DataObject:
    def __init__(self,json_url,video_url):
        self.json_url = json_url
        self.video_url = video_url

DataObjectList = []


def start():
    pass

def load_all_the_models():
    summarizer.load_model
    audio_converter.model_load

def api_and_json_extraction(interests):
    list_of_all_the_json_filepaths = newsapi.newsapi_fun(interests)

    for filePath in list_of_all_the_json_filepaths:
        DataObjectList.append(DataObject(filePath,None))

summarizer.file_load()
# audio_converter.converter(text)
# prompt = "bitcoin"
# print(video_generator.video_gen_fun(prompt))