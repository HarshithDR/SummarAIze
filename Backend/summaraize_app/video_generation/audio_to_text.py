from vosk import Model, KaldiRecognizer
import os
import wave
import json 

def a_t_t(audio_file_path):
    # Specify the path to the Vosk model you downloaded
    vosk_model_path = "Backend\\summaraize_app\\Captions_video_generation\\vosk_model\\vosk-model-small-en-us-0.15"
    audio_file = audio_file_path


    if not os.path.exists(vosk_model_path):
        print("Model path is incorrect. Please adjust it.")
        exit(1)

    # Load the audio file
    wf = wave.open(audio_file, "rb")

    # Load the Vosk model
    model = Model(vosk_model_path)

    # Create a recognizer with the model
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    # Recognize speech
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(rec.Result())

    results.append(rec.FinalResult())

    # Print results with word-level timestamps
    for result in results:
        result_json = json.loads(result)
        if 'result' in result_json:
            for word_info in result_json['result']:
                print(f"{word_info['word']} - start: {word_info['start']}, end: {word_info['end']}")

    wf.close()
