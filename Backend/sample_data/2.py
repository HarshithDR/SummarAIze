from transformers import pipeline
import json
import tensorflow as tf

# Replace tf.losses.sparse_softmax_cross_entropy with tf.compat.v1.losses.sparse_softmax_cross_entropy
# loss = tf.compat.v1.losses.sparse_softmax_cross_entropy(labels, logits)

summarizer = pipeline("summarization", model="t5-small")

def summarize_text(text, max_length=100):
  """
  Summarizes a text using a lightweight LLM (t5-small).

  Args:
      text: The text to be summarized.
      max_length: The maximum length of the summary (default 100 words).

  Returns:
      A string containing the summarized text.
  """
  summary = summarizer(text, max_length=max_length, truncation=True)
  return summary[0]["summary_text"]

with open('Whats_Behind_the_Bitcoin_Price_Surge_Vibes_Mostly.json', 'r', encoding='utf-8') as f:
    captions_data = json.load(f)

# with open("Whats_Behind_the_Bitcoin_Price_Surge_Vibes_Mostly.json", "r") as f:
#     captions_data = json.load(f)
# text = json.load('/content/Whats_Behind_the_Bitcoin_Price_Surge_Vibes_Mostly.json')
summary = summarize_text(captions_data['content'])
print(summary)