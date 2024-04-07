from Backend.summaraize_app.text_collection_and_summarizer import newsapi

def api_and_json_extraction(interests):
    list_of_all_the_json_filepaths = newsapi.newsapi_fun(interests)
    return list_of_all_the_json_filepaths

print(list_of_all_json_filepaths = api_and_json_extraction('soccer'))