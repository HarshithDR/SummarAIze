from text_collection_and_summarizer import newsapi
from summarize import summarizer
from video_generation import video_generator
from dataclasses import dataclass
from audio_convert import text_to_audio_converter, caption_creater_and_video_audio_merger


'''This class definition creates a data object 
with attributes json_url and video_url.'''
@dataclass
class DataObject:
    def __init__(self,json_url,video_url):
        self.json_url = json_url
        self.video_url = video_url

# DataObjectList = []


def load_all_the_models():
    summarizer.load_model
    # text_to_audio_converter.model_load()

def api_and_json_extraction(interests):
    list_of_all_the_json_filepaths = newsapi.newsapi_fun(interests)
    return list_of_all_the_json_filepaths
    # for filePath in list_of_all_the_json_filepaths:
    #     DataObjectList.append(DataObject(filePath,None))
    
def llm_summarizer(json_path):
    summary = summarizer.file_load(json_path)
    return summary
    
def audio_conv(summary):
    text_to_audio_converter.converter(summary)
    
def video_gen(summary):
    video_generator.video_gen_fun(summary)
    
def final_video_creater():
    video_path = caption_creater_and_video_audio_merger.start()
    
def start():
    list_of_all_json_filepaths = api_and_json_extraction('soccer')
    for filepath in list_of_all_json_filepaths:
        summary = llm_summarizer(filepath)
        print(type(summary))
        # try:
        audio_conv(summary)

        video_gen(summary)
        video_path = final_video_creater()\
        
        
start()