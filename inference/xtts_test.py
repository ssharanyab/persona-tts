from pathlib import Path
from TTS.api import TTS
import torch

PROJECT_ROOT = Path(__file__).resolve().parent.parent

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2",
    progress_bar=True
).to(device)

speaker_wavs = [
    PROJECT_ROOT / "data" / "segments" / f"audio_1_{i:03d}.wav"
    for i in range(26)
]

speaker_wavs += [
    PROJECT_ROOT / "data" / "segments" / f"audio_2_{i:03d}.wav"
    for i in range(29)
]

speaker_wavs += [
    PROJECT_ROOT / "data" / "segments" / f"audio_3_{i:03d}.wav"
    for i in range(23)
]

# Validate all reference files before inference
missing = [str(p) for p in speaker_wavs if not p.is_file()]

if missing:
    raise FileNotFoundError(
        f"Missing {len(missing)} reference files:\n" +
        "\n".join(missing)
    )

print(f"Found {len(speaker_wavs)} reference clips.")

text = (
    "This is a test of my personal voice. "
    "If this sounds similar to me, then my text to speech system "
    "is working correctly."
)

output_dir = PROJECT_ROOT / "outputs"
output_dir.mkdir(parents=True, exist_ok=True)

tts.tts_to_file(
    text=text,
    speaker_wav=[str(p) for p in speaker_wavs],
    language="en",
    file_path=str(output_dir / "baseline.wav"),
)

print("Saved baseline.wav")