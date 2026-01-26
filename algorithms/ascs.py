import os
import shutil
import librosa
import numpy as np

SRC_FOLDER = "data/segments"
DST_FOLDER = "data/final_segments"


def analyze_clip(path):
    y, sr = librosa.load(path, sr=22050)

    duration = librosa.get_duration(y=y, sr=sr)
    rms = np.mean(librosa.feature.rms(y=y))
    silence_ratio = np.mean(np.abs(y) < 0.01)

    return {
        "path": path,
        "duration": duration,
        "rms": rms,
        "silence_ratio": silence_ratio
    }


def score_clip(features):
    duration_score = min(features["duration"] / 12.0, 1.0)
    rms_score = min(features["rms"] / 0.05, 1.0)
    silence_penalty = features["silence_ratio"]

    score = (
        0.4 * duration_score +
        0.4 * rms_score -
        0.2 * silence_penalty
    )

    return score


def select_and_copy(keep_ratio=0.8):
    os.makedirs(DST_FOLDER, exist_ok=True)

    clips = []

    for f in os.listdir(SRC_FOLDER):
        if f.endswith(".wav"):
            path = os.path.join(SRC_FOLDER, f)
            feat = analyze_clip(path)
            feat["score"] = score_clip(feat)
            clips.append(feat)

    clips.sort(key=lambda x: x["score"], reverse=True)

    keep_n = int(len(clips) * keep_ratio)
    selected = clips[:keep_n]

    for c in selected:
        shutil.copy(c["path"], DST_FOLDER)

    print(f"Total clips: {len(clips)}")
    print(f"Selected clips: {len(selected)}")
    print("Copied to data/final_segments/")


if __name__ == "__main__":
    select_and_copy()
