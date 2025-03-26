# transcript.py 
# Using openai-whisper to transcript audio recordings
# @skereboi

# Libraries 
import torch
import whisper 

# MPS for Apple Silicon
device = "cpu" #"mps" if torch.backends.mps.is_available() else 
print(f"Using device: {device}")

# Model settings
model = whisper.load_model("turbo", device=device)
result = model.transcribe("/Users/skereboi/Documents/SmartLanguageSchool/Smart Language School, first meeting record_.m4a", language="es")

transcription = result["text"]

# Write the file 
with open("transcripcion.txt", "w", encoding="utf-8") as f:
    f.write(transcription)
