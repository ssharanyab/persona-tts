from TTS.api import TTS
import torch
import os

device = "cuda" if torch.cuda.is_available() else "cpu"

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2"
).to(device)

def generate(reference_dir, output_name):
    refs = [
        os.path.join(reference_dir, f)
        for f in os.listdir(reference_dir)
        if f.endswith(".wav")
    ]

    text = (
        "This experiment evaluates how reference audio selection "
        "affects speaker identity in conditioning-based voice synthesis."
    )

    tts.tts_to_file(
        text=text,
        speaker_wav=refs,
        language="en",
        file_path=f"outputs/{output_name}.wav"
    )

generate("data/buckets_auto/neutral", "conditioned_neutral")
generate("data/buckets_auto/slow", "conditioned_slow")
generate("data/buckets_auto/expressive", "conditioned_expressive")
generate("data/buckets_auto/energetic", "conditioned_energetic")
