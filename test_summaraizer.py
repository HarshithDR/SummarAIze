from Backend.summaraize_app.summarize import summarizer

def load_all_the_models():
    summarizer.load_model
    # text_to_audio_converter.model_load()
    
def llm_summarizer(json_path):
    summary = summarizer.file_load(json_path)
    return summary

summary = llm_summarizer('Backend\summaraize_app\json_folder\El_Salvador_gained_84M_from_Bitcoin_holdings.json')
print(type(summary))