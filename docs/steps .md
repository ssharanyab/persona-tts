# Steps I used
1. Convert m4a to wav using ffmpeg
   ```bash
   ffmpeg -i data/raw/audio_1.m4a -ar 22050 -ac 1 data/wav/audio_1.wav 
   ```
2. Segment (fixed length)
   ```bash
   ffmpeg -i data/wav/audio_1.wav -f segment -segment_time 12 -c copy data/segments/audio_1_%03d.wav
   ```
