from TTS.api import TTS
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

tts = TTS(
    model_path="trained_models/xtts_speaker/model.pth",
    config_path="trained_models/xtts_speaker/config.json",
).to(device)

text = (
    "This is my fine tuned voice model. "
    "It should sound closer to my real voice compared to before."
)

tts.tts_to_file(
    text=text,
    language="en",
    file_path="outputs/finetuned_voice.wav"
)

print("Saved outputs/finetuned_voice.wav")
