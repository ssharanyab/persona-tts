from TTS.api import TTS
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2",
    progress_bar=True
).to(device)

speaker_wavs = [
    "data/segments/audio_1_000.wav",
    "data/segments/audio_1_001.wav",
    "data/segments/audio_1_002.wav",
    "data/segments/audio_1_003.wav",
    "data/segments/audio_1_004.wav",
    "data/segments/audio_1_005.wav",
    "data/segments/audio_1_006.wav",
    "data/segments/audio_1_007.wav",
    "data/segments/audio_1_008.wav",
    "data/segments/audio_1_009.wav",
    "data/segments/audio_1_010.wav",
    "data/segments/audio_1_011.wav",
    "data/segments/audio_1_012.wav",
    "data/segments/audio_1_013.wav",
    "data/segments/audio_1_014.wav",
    "data/segments/audio_1_015.wav",
    "data/segments/audio_1_016.wav",
    "data/segments/audio_1_017.wav",
    "data/segments/audio_1_018.wav",
    "data/segments/audio_1_019.wav",
    "data/segments/audio_1_020.wav",
    "data/segments/audio_1_021.wav",
    "data/segments/audio_1_022.wav",
    "data/segments/audio_1_023.wav",
    "data/segments/audio_1_024.wav",
    "data/segments/audio_1_025.wav",  
    #Audio 2
    "data/segments/audio_2_000.wav",
    "data/segments/audio_2_001.wav",
    "data/segments/audio_2_002.wav",
    "data/segments/audio_2_003.wav",
    "data/segments/audio_2_004.wav",
    "data/segments/audio_2_005.wav",
    "data/segments/audio_2_006.wav",
    "data/segments/audio_2_007.wav",
    "data/segments/audio_2_008.wav",
    "data/segments/audio_2_009.wav",
    "data/segments/audio_2_010.wav",
    "data/segments/audio_2_011.wav",
    "data/segments/audio_2_012.wav",
    "data/segments/audio_2_013.wav",
    "data/segments/audio_2_014.wav",
    "data/segments/audio_2_015.wav",
    "data/segments/audio_2_016.wav",
    "data/segments/audio_2_017.wav",
    "data/segments/audio_2_018.wav",
    "data/segments/audio_2_019.wav",
    "data/segments/audio_2_020.wav",
    "data/segments/audio_2_021.wav",
    "data/segments/audio_2_022.wav",
    "data/segments/audio_2_023.wav",
    "data/segments/audio_2_024.wav",
    "data/segments/audio_2_025.wav",  
    "data/segments/audio_2_026.wav",
    "data/segments/audio_2_027.wav",
    "data/segments/audio_2_028.wav",
    #Audio 3
    "data/segments/audio_3_000.wav",
    "data/segments/audio_3_001.wav",
    "data/segments/audio_3_002.wav",
    "data/segments/audio_3_003.wav",
    "data/segments/audio_3_004.wav",
    "data/segments/audio_3_005.wav",
    "data/segments/audio_3_006.wav",
    "data/segments/audio_3_007.wav",
    "data/segments/audio_3_008.wav",
    "data/segments/audio_3_009.wav",
    "data/segments/audio_3_010.wav",
    "data/segments/audio_3_011.wav",
    "data/segments/audio_3_012.wav",
    "data/segments/audio_3_013.wav",
    "data/segments/audio_3_014.wav",
    "data/segments/audio_3_015.wav",
    "data/segments/audio_3_016.wav",
    "data/segments/audio_3_017.wav",
    "data/segments/audio_3_018.wav",
    "data/segments/audio_3_019.wav",
    "data/segments/audio_3_020.wav",
    "data/segments/audio_3_021.wav",
    "data/segments/audio_3_022.wav",
]

text = (
    "This is a test of my personal voice. "
    "If this sounds similar to me, then my text to speech system is working correctly."
)

tts.tts_to_file(
    text=text,
    speaker_wav=speaker_wavs,
    language="en",
    file_path="outputs/baseline.wav",
)

print("Saved to outputs/baseline.wav")
