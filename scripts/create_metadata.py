import os
import csv

AUDIO_DIR = "data/final_segments"
OUTPUT_CSV = "data/metadata.csv"

SPEAKER_NAME = "speaker"
DUMMY_TEXT = "dummy"

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="|")

    # header
    writer.writerow(["audio_file", "text", "speaker_name"])

    for filename in sorted(os.listdir(AUDIO_DIR)):
        if filename.endswith(".wav"):
            relative_path = f"final_segments/{filename}"
            writer.writerow([relative_path, DUMMY_TEXT, SPEAKER_NAME])

print("metadata.csv created successfully.")
