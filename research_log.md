## Core Hypothesis
A usable, speaker-consistent neural TTS voice can be obtained with ≤45 minutes
of single-speaker English data using pretrained models on consumer hardware,
with acceptable quality degradation at lower data regimes.

## Preprocessing v1
- Silence trimming: yes
- Normalization: RMS
- Denoising: no
- Sample rate: 22050 Hz

Reason: establish minimal preprocessing baseline

Recording protocol:
Audio was recorded across three sessions on separate days.
Each session consisted of multiple short recordings ranging
from approximately 30 seconds to 2 minutes.
This approach improved segmentation and preprocessing stability.

Recording format:
Audio was recorded in M4A format using a laptop microphone.
All files were later converted to WAV during preprocessing.

## Experiment E0 – Pipeline Validation

- Data duration: ~5 minutes
- Recording format: M4A
- Recording style: continuous
- Noise level: low
- Preprocessing: ffmpeg conversion + silence-based segmentation

Goal:
Validate full preprocessing and inference pipeline before collecting more data.

E0 preprocessing:
- Input format: M4A (AAC, 48kHz stereo)
- Converted to: WAV (22,050 Hz, mono)
- Tool: FFmpeg

E0 inference result:
- Output intelligible
- Strong AI timbre
- Low speaker similarity
- Expected outcome for conditioning-only setup

## Experiment E1 – Data Augmentation

