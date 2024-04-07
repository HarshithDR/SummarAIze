from transformers import pipeline
import json
# import tensorflow as tf

class load_model:
    summarizer_model = pipeline("summarization", model="t5-small")

def summarize_model_text(text, max_length=100):
  """
  Summarizes a text using a lightweight LLM (t5-small).

  Args:
      text: The text to be summarized.
      max_length: The maximum length of the summary (default 100 words).

  Returns:
      A string containing the summarized text.
  """
  summary = load_model.summarizer_model(text, max_length=max_length, truncation=True)
  return summary[0]["summary_text"]

def file_load():
    with open('Backend\summaraize_app\json_folder\Adobes_new_GenStudio_platform_is_an_AI_factory_for_advertisers.json', 'r', encoding='utf-8') as f:
        captions_data = json.load(f)

    summary = summarize_model_text(captions_data['content'])
    print(summary)