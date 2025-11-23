# Indonesian ASR @ NTU Speech & Language Lab

Project Components:
- YouTube crawling with [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Large-scale audio processing on National Supercomputing Centre (NSCC) ASPIRE 2A
- Automatic Transcription/Segmentation pipelines:
  - [GigaSpeech2](https://github.com/SpeechColab/GigaSpeech2)
  - [NeMo SDP/Granary](https://github.com/NVIDIA/NeMo-speech-data-processor/tree/main/dataset_configs/multilingual/granary)
- Segment normalisation, filtering, and dataset export

## Project Overview
Crawl and process large-scale Southeast Asian speech data into a clean ASR training set for downstream model training.

### Goals:
1. Large-scale crawling of speech data from YouTube
  - Bahasa Indonesia
  - Indonesian-English code-switching
  - Southeast Asian English Accents (Indonesian, Filipino, Indian)
3. Reproduce and adapt the GigaSpeech2 and NeMo SDP pipelines on the NSCC HPC cluster
4. Process raw audio into trainable ASR segments, with
   - Automatic transcription
   - Forced alignment
   - Segmentation
   - Normalisation and filtering
     
### High-Level Pipeline
1. Crawl audio & metadata (Google Colab, yt-dlp)
2. Sync data to NSCC (SCP/Rsync)
3. Run speech data processing via:
  - GigaSpeech2
  - Nemo SDP Granary
4. Normalise and filter text (language, numbers, dates)
5. Export manifests/segments as JSONL/TXT transcripts for ASR training

## Repository Structure
