from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

encoder = VoiceEncoder()

# Real voice reference
real_voice = preprocess_wav("data/buckets_auto/neutral/audio_1_001.wav")
real_embed = encoder.embed_utterance(real_voice)

# Generated voice
generated_voice = preprocess_wav("outputs/conditioned_neutral.wav")
gen_embed = encoder.embed_utterance(generated_voice)

similarity = cosine_similarity(
    [real_embed],
    [gen_embed]
)[0][0]

print("Speaker similarity score:", round(similarity, 3))
