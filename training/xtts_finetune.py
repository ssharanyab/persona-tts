import os
import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

print("Using device:", device)

# Load XTTS model
tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2",
    progress_bar=True
).to(device)

# Directory containing selected clips
speaker_wav_dir = "data/final_segments"

# Output model folder
output_path = "trained_models/xtts_speaker"

os.makedirs(output_path, exist_ok=True)

# Fine-tune (speaker adaptation)
tts.finetune(
    speaker_wav_dir=speaker_wav_dir,
    output_path=output_path,
    epochs=15,
    batch_size=2,
    learning_rate=5e-6,
)
