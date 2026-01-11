# PersonaTTS

PersonaTTS is a personalized neural text-to-speech system that learns a user's vocal persona from a short speech sample and generates natural-sounding speech for arbitrary input text.

## Motivation
Most text-to-speech systems rely on large speaker datasets or pre-defined voices. PersonaTTS explores how minimal speaker data (2–3 short recordings) can be used to adapt a neural TTS model to a new voice while maintaining intelligibility and naturalness.

## High-Level Pipeline
1. User voice recording (2–3 paragraphs)
2. Audio preprocessing and validation
3. Speaker representation extraction
4. Speaker-conditioned text-to-speech generation
5. Audio output
