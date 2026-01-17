# Audio Preprocessing Pipeline

This document describes the preprocessing steps used to prepare
raw voice recordings for speaker adaptation experiments.

All audio data is excluded from version control due to size
and privacy considerations.

---

## Recording Setup

- Device: Laptop microphone
- Environment: Quiet indoor room
- Format: M4A (AAC)
- Sample rate: 48 kHz
- Channels: Stereo
- Recording style: Continuous narration
- Duration (E0): ~5 minutes

---

## Conversion

Raw recordings are converted to WAV format using FFmpeg.

Command used:

ffmpeg -i data/raw/day1_audio.m4a -ar 22050 -ac 1 data/wav/day1_audio.wav

- Output format: WAV
- Sample rate: 22,050 Hz
- Channels: Mono

---

## Segmentation

Silence-based segmentation was attempted but produced a single segment
due to continuous speech and low background noise.

Fixed-length segmentation was therefore used.

Command:

ffmpeg -i data/wav/day1_audio.wav -f segment -segment_time 12 -c copy data/segments/seg_%03d.wav

- Segment length: ~12 seconds
- Purpose: Improve stability during speaker adaptation

---

## Rationale

Short audio segments improve:
- training stability
- batching efficiency
- memory usage
- alignment robustness

This approach reflects real-world recording conditions where silence
may not be clearly detectable.

---

## Output

The preprocessing pipeline produces:
- multiple short WAV files
- consistent sampling rate
- uniform audio format

These files are used for inference and later training experiments.
