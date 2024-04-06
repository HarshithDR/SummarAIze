import json

with open("C:\\Users\\harsh\\Desktop\\Python Projects\\SummarAIze\\output_json_file.json", "r") as f:
    captions = json.load(f)
dic_list = []
print(len(captions))
# for text_contents in captions[0]
# for i in range(0,len(captions)):
#     for text_contents in captions[i]:
#         dic_list.append(text_contents.value())
        
        
# print(dic_list)

# text_contents = captions[0]['textcontents']

# # Extracting words and confidence scores
# words_with_confidence = [(item['word'], item['conf']) for item in text_contents]

# print(words_with_confidence)

all_text_contents = []

# Loop through each item in the data list
for item in captions:
    # Extract textcontents from the current item
    text_contents = item['textcontents']
    # Extend the all_text_contents list with the textcontents of the current item
    all_text_contents.extend(text_contents)

print(all_text_contents)
# Extracting words and confidence scores
# words_with_confidence = [(item['word'], item['start'],item['end']) for item in all_text_contents]

# print(words_with_confidence)

with open('output_json_file_final.json', 'w') as f:
    json.dump(all_text_contents, f, indent=4)