import os
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import speech_recognition as sr

# Setting up FFmpeg Path
ffmpeg_bin_path = 'C:\\ffmpeg\\bin'  # Replace with your actual FFmpeg path
os.environ["PATH"] += os.pathsep + ffmpeg_bin_path

# Determining Device and Data Type
device_type = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_data_type = torch.float16 if torch.cuda.is_available() else torch.float32

# Whisper Model Configuration
whisper_model_id = "openai/whisper-large-v3"
whisper_model = AutoModelForSpeechSeq2Seq.from_pretrained(
    whisper_model_id, 
    torch_dtype=torch_data_type, 
    low_cpu_mem_usage=True, 
    use_safetensors=True
)
whisper_model.to(device_type)

whisper_processor = AutoProcessor.from_pretrained(whisper_model_id)

# Setting up Whisper Pipeline
whisper_pipeline = pipeline(
    "automatic-speech-recognition",
    model=whisper_model,
    tokenizer=whisper_processor.tokenizer,
    feature_extractor=whisper_processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_data_type,
    device=device_type,
)

# Configuring Speech Recognition
speech_recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Start speaking...")
    # Modify the timeout and phrase_time_limit as needed
    recorded_audio = speech_recognizer.listen(source, timeout=10, phrase_time_limit=30)
    print("Processing speech...")

# Converting Audio to Bytes
audio_bytes = recorded_audio.get_wav_data()

# Transcribing Speech
transcription_result = whisper_pipeline(audio_bytes)
print(transcription_result["text"])
