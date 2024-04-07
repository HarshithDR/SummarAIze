import json
from moviepy.editor import *

# Load the video
video_clip = VideoFileClip("C:\\Users\\harsh\Desktop\\Python Projects\\SummarAIze\\Backend\\sample_data\\sample.mp4")

# Load the captions from JSON
with open("C:\\Users\\harsh\\Desktop\\Python Projects\\SummarAIze\\Backend\\sample_data\\output_json_file_final.json", "r") as f:
    captions_data = json.load(f)

# Extract start time, end time, and text from each caption data
captions = [(item["start"], item["end"], item["word"]) for item in captions_data]

# Create text clips for each caption
text_clips = []
for start_time, end_time, text in captions:
    text_clip = (
        TextClip(text, fontsize=50, color="white", bg_color="black")
        .set_position("bottom")
        .set_duration(end_time - start_time)
        .set_start(start_time)
    )
    text_clips.append(text_clip)

# Overlay the text clips onto the video
final_clip = video_clip.set_audio(video_clip.audio)  # Preserve original audio
for text_clip in text_clips:
    final_clip = CompositeVideoClip([final_clip, text_clip])

# Save the final video with captions
final_clip.write_videofile("output_video_with_captions.mp4")