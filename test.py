
import json

def split_text_into_lines(data):
    MaxChars = 80 
    MaxDuration = 3.0
    MaxGap = 1.5

    subtitles = []
    line = []
    line_duration = 0
    line_chars = 0

    for result_data in data:
        if "result" not in result_data:
            print("Warning: Missing 'result' key in dictionary")
            continue

        result_list = result_data["result"]

        for idx, word_data in enumerate(result_list):
            if "start" not in word_data or "end" not in word_data or "word" not in word_data:
                print(f"Warning: Missing key in dictionary at index {idx}")
                continue

            word = word_data["word"]
            start = word_data["start"]
            end = word_data["end"]

            line.append(word_data)
            line_duration += end - start
            
            temp = " ".join(item["word"] for item in line)

            new_line_chars = len(temp)

            duration_exceeded = line_duration > MaxDuration 
            chars_exceeded = new_line_chars > MaxChars 
            if idx > 0:
                gap = start - result_list[idx - 1]['end']
                maxgap_exceeded = gap > MaxGap
            else:
                maxgap_exceeded = False

            if duration_exceeded or chars_exceeded or maxgap_exceeded:
                if line:
                    subtitle_line = {
                        "text": " ".join(item["word"] for item in line),
                        "start": line[0]["start"],
                        "end": line[-1]["end"],
                        "textcontents": line
                    }
                    subtitles.append(subtitle_line)
                    line = []
                    line_duration = 0
                    line_chars = 0

        if line:
            subtitle_line = {
                "text": " ".join(item["word"] for item in line),
                "start": line[0]["start"],
                "end": line[-1]["end"],
                "textcontents": line
            }
            subtitles.append(subtitle_line)
            line = []
            line_duration = 0
            line_chars = 0

    return subtitles

# Load word-level timestamps JSON from a file
with open("C:\\Users\\harsh\\Desktop\\Python Projects\\SummarAIze\\Backend\\sample_data\\recognized_speech.json", "r") as file:
    wordlevel_info_modified = json.load(file)

linelevel_subtitles = split_text_into_lines(wordlevel_info_modified)
print(linelevel_subtitles)


# Write results to JSON file
with open('output_json_file.json', 'w') as f:
    json.dump(linelevel_subtitles, f, indent=4)
    
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

with open('output_json_file_final_now.json', 'w') as f:
    json.dump(all_text_contents, f, indent=4)
    
    
