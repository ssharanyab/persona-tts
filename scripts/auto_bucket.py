import os
import librosa
import numpy as np
import shutil

SRC = "data/final_segments"
DST = "data/buckets_auto"

os.makedirs(DST, exist_ok=True)

BUCKETS = {
    "neutral": [],
    "energetic": [],
    "slow": [],
    "expressive": []
}

def analyze(path):
    y, sr = librosa.load(path, sr=22050)

    rms = np.mean(librosa.feature.rms(y=y))
    pitch = librosa.yin(y, fmin=50, fmax=300)
    pitch_var = np.nanstd(pitch)
    silence = np.mean(np.abs(y) < 0.01)

    return rms, pitch_var, silence


stats = []

for f in os.listdir(SRC):
    if f.endswith(".wav"):
        path = os.path.join(SRC, f)
        rms, pitch_var, silence = analyze(path)
        stats.append((f, rms, pitch_var, silence))

# normalize
rms_vals = [s[1] for s in stats]
pitch_vals = [s[2] for s in stats]
silence_vals = [s[3] for s in stats]

rms_thr = np.median(rms_vals)
pitch_thr = np.median(pitch_vals)
silence_thr = np.median(silence_vals)

for f, rms, pitch_var, silence in stats:

    if rms > rms_thr and pitch_var > pitch_thr:
        bucket = "energetic"
    elif pitch_var > pitch_thr:
        bucket = "expressive"
    elif silence > silence_thr:
        bucket = "slow"
    else:
        bucket = "neutral"

    BUCKETS[bucket].append(f)

    os.makedirs(os.path.join(DST, bucket), exist_ok=True)
    shutil.copy(
        os.path.join(SRC, f),
        os.path.join(DST, bucket, f)
    )

print("Auto-bucketing complete.")
for k, v in BUCKETS.items():
    print(k, ":", len(v))
