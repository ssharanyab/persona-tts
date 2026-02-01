# 🎙️ Persona TTS — Phase 1  
**Data-Centric Speaker Conditioning with XTTS**


## ✅ Final Result

**Speaker similarity score:** **0.762 (cosine similarity)**

Measured between real voice and generated speech using a pretrained speaker verification model.

This indicates **moderate-to-strong speaker identity alignment achieved without any model training**, using only multi-reference conditioning.

![Speaker verification result](assets/speaker_similarity_result.png)


## 📘 Overview

Persona TTS — Phase 1 explores **speaker conditioning** using XTTS under limited voice data.

No model training or fine-tuning is performed.

The goal is to understand how far voice similarity can be improved using **data selection, reference composition, and objective evaluation** alone.


## 🎯 Objectives

- Study voice cloning behavior without training  
- Improve speaker identity using reference audio selection  
- Build a clean conditioning pipeline  
- Evaluate similarity objectively instead of relying only on listening  

## 📂 Repository Structure

```bash
persona-tts/
├── inference/
├── algorithms/
├── evaluation/
├── docs/
├── assets/
└── README.md
```

Audio data and generated outputs are excluded for privacy.


## ⚙️ Pipeline

Recording
→ Preprocessing
→ Segmentation
→ Clip Selection (ASCS)
→ Reference Bucketing
→ Multi-Reference Conditioning
→ Speaker Verification


## 🔧 Key Components

### Adaptive Speaker Clip Selection (ASCS)

Reference clips are ranked using:
- duration  
- RMS energy  
- silence ratio  

Only high-quality clips are retained to improve embedding stability.


### Automatic Reference Bucketing

Clips are grouped into approximate speaking styles:
- neutral  
- expressive  
- energetic  
- slow  

This enables controlled conditioning experiments.


### Conditioning-Based Inference

XTTS v2 is used strictly in **reference conditioning mode**:

- no weight updates  
- no fine-tuning  
- no dataset training  

Speaker identity is injected using multiple reference clips.



### Objective Evaluation

A pretrained speaker verification model is used to:

- extract speaker embeddings  
- compute cosine similarity  
- compare baseline vs improved outputs  

This provides measurable identity comparison beyond subjective listening.



## 📊 Observations

**Worked well**
- multi-reference conditioning  
- clean short reference clips  
- data quality over quantity  
- objective verification aligned with perception  

**Did not**
- long-form stability  
- emotional expressiveness  
- full identity consistency  

---

## ⚠️ Limitations

- no model training  
- no gradient updates  
- identity drift in long narration  
- limited expressive control  

These are expected limitations of conditioning-based approaches.


## 🔮 Future Scope

Phase 2 will focus on **training-based approaches under Linux**, including:

- gradient-based speaker adaptation  
- alignment-aware learning  
- research-level experimentation  
- paper-oriented evaluation  

Phase 1 serves as the foundation.


