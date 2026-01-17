from TTS.api import TTS
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2",
    progress_bar=True
).to(device)

speaker_wavs = [
    "data/segments/seg_000.wav",
    "data/segments/seg_001.wav",
    "data/segments/seg_002.wav",
    "data/segments/seg_003.wav",
]

text = (
    "This is a test of my personal voice. "
    "If this sounds similar to me, then my text to speech system is working correctly."
)

tts.tts_to_file(
    text=text,
    speaker_wav=speaker_wavs,
    language="en",
    file_path="outputs/test_voice.wav",
)

print("Saved to outputs/test_voice.wav")
