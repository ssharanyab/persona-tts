# Persona TTS

A personalized Text-to-Speech system for creating custom voice models.

PersonaTTS is a personalized neural text-to-speech system that learns a user's vocal persona from a short speech sample and generates natural-sounding speech for arbitrary input text.

This project explores low-resource speaker adaptation for text-to-speech systems under realistic creator-grade constraints.

Instead of building a new speech model from scratch, the project focuses on:
designing an end-to-end TTS pipeline collecting real-world voice data evaluating progressive improvement with increasing data studying the limitations of voice cloning under limited resources

The final goal is to build a usable personal narration voice while maintaining research transparency and reproducibility.

## Motivation
Most text-to-speech systems rely on large speaker datasets or pre-defined voices. PersonaTTS explores how minimal speaker data (2–3 short recordings) can be used to adapt a neural TTS model to a new voice while maintaining intelligibility and naturalness.

## High-Level Pipeline
1. User voice recording (2–3 paragraphs)
2. Audio preprocessing and validation
3. Speaker representation extraction
4. Speaker-conditioned text-to-speech generation
5. Audio output

## Project Structure

```
persona-tts/
│
├── data/
│   ├── raw/              # Original audio recordings
│   ├── processed/        # Trimmed and normalized audio
│   └── metadata.csv      # Audio file metadata
│
├── training/
│   ├── config.yaml       # Training configuration
│   └── train.py          # Training script
│
├── inference/
│   ├── generate.py       # Speech generation
│   └── model_loader.py   # Model loading utilities
│
├── api/
│   └── main.py           # FastAPI server
│
├── flutter_app/          # Desktop UI (planned)
│
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- PyTorch
- FastAPI (for API server)
- Flutter (for desktop app)

### Installation

```bash
# Install dependencies
pip install torch torchaudio
pip install fastapi uvicorn pydantic
pip install pyyaml
```

### Usage

#### Training

1. Place your audio recordings in `data/raw/`
2. Update `data/metadata.csv` with file information
3. Configure training parameters in `training/config.yaml`
4. Run training:

```bash
cd training
python train.py
```

#### Inference

Generate speech from text:

```bash
cd inference
python generate.py
```

#### API Server

Start the FastAPI server:

```bash
cd api
python main.py
```
The API will be available at `http://localhost:8000`

#### Inference

Evaluation is primarily empirical and perceptual:
- subjective similarity assessment
- intelligibility
- long-form listening comfort
- consistency across paragraphs

Optional:
- speaker embedding cosine similarity
- qualitative before/after comparison

#### Research Focus
This project studies:

- low-resource speaker adaptation
- real-world recording conditions
- diminishing returns with increased data
- trade-offs between quality and practicality

It does not aim to outperform commercial systems, but to understand feasibility and limitations.

## Development Roadmap

- [x] Implement data preprocessing pipeline
- [x] Train initial TTS model
- [ ] Complete inference pipeline
- [ ] Build FastAPI endpoints
- [ ] Create Flutter desktop application

