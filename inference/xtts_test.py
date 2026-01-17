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
    "data/segments/seg_004.wav",
    "data/segments/seg_005.wav",
    "data/segments/seg_006.wav",
    "data/segments/seg_007.wav",
    "data/segments/seg_008.wav",
    "data/segments/seg_009.wav",
    "data/segments/seg_010.wav",
    "data/segments/seg_011.wav",
    "data/segments/seg_012.wav",
    "data/segments/seg_013.wav",
    "data/segments/seg_014.wav",
    "data/segments/seg_015.wav",
    "data/segments/seg_016.wav",
    "data/segments/seg_017.wav",
    "data/segments/seg_018.wav",
    "data/segments/seg_019.wav",
    "data/segments/seg_020.wav",
    "data/segments/seg_021.wav",
    "data/segments/seg_022.wav",
    "data/segments/seg_023.wav",
    "data/segments/seg_024.wav",
    "data/segments/seg_025.wav",  
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
