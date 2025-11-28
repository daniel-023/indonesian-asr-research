# Indonesian ASR @ NTU Speech & Language Lab
Large-scale crawling and processing Southeast Asian speech into ASR training datasets for downstream model training.

## Project Components:
- YouTube crawling with [yt-dlp](https://github.com/yt-dlp/yt-dlp) on Google Colab
- Large-scale audio processing on NSCC ASPIRE 2A
- Automatic transcription / segmentation via:
  - [GigaSpeech2](https://github.com/SpeechColab/GigaSpeech2)
  - [NeMo SDP (Granary)](https://github.com/NVIDIA/NeMo-speech-data-processor/tree/main/dataset_configs/multilingual/granary)
- Segment normalisation, filtering, and dataset export for ASR training

## Goals
1. Collect large-scale speech data from YouTube
   - Covering Bahasa Indonesia, Indonesian–English code-switching, and Southeast Asian English accents (Indonesian, Filipino).
3. Run scalable ASR processing on NSCC
   - Reproduce and adapt the GigaSpeech2 and NeMo SDP / Granary pipelines for Indonesian and SEA data.
5. Produce high-quality ASR training datasets for low-resource settings
   - Generate segmented audio + transcripts with consistent normalisation, filtering, and manifests ready for downstream ASR training.
   
## High-Level Pipeline
1. Crawl audio & metadata on Google Colab using yt-dlp (with rate limiting / VPN or cookie handling as needed).
2. Sync crawled data to NSCC via `scp` / `rsync` into `/scratch` directory.
3. Run speech processing pipelines:
   - GigaSpeech2
   - NeMo SDP / Granary
4. Apply text normalisation and filtering (language, numbers/dates, etc.)
5. Export manifests (JSONL/TXT) listing audio paths, timestamps, durations, and cleaned transcripts.

## Data Overview
Raw hours crawled:
| Category                    | Hours (approx.) |
|-----------------------------|-----------------|
| Indonesian (mono + CS)      | ~2,900          |
| English – Indonesian accent | ~763            |
| English – Filipino accent   | ~787            |

## Internship Timeline
- **Weeks 1–2 – GigaSpeech2 pipeline & crawling setup**  
  - Implemented GigaSpeech2 pipeline in the NSCC with a small Indonesian channel 
  - Set up YouTube crawling (yt-dlp, VPN, cookie handling)  
  - Refined filters: Reduce confidence threshold and allow LID `ms` and `id`
  - Use WER to calculate data loss at force alignment stage

- **Weeks 3–4 – Large-scale processing and test Granary pipeline**  
  - Identify Indonesian speech data sources (e.g. news channels, vlogs, etc.)
  - Scale up Indonesian crawling and processing (~1.3k hours)
  - Set up NeMo SDP / Granary pipeline: modify config processors for ASR training
  - Generate Granary manifest and tarred dataset 

- **Weeks 5–6 – Scaling up & quality control**  
  - Implemented batching and parallel processing for GigaSpeech2 pipeline
  - Compared GigaSpeech2 vs Granary pipelines: processing speed, segment length/quality 
  - Investigated Granary segmentation (boundary word loss, chunking, hallucination)

- **Weeks 7–8 – SEA English accents & normalisation**  
  - Shifted focus to SEA-accented English
  - Tested Indonesian text normalisation (numbers, currency, time)  
  - Decided to drop utterances with numbers/dates due to speech-transcript mismatch
  - Implemented punctuation-based segmentation for Granary outputs

- **Weeks 9–10 – Segmentation strategies & repo cleanup**  
  - Implemented punctuation-based segmentation and number removal post-processing  
  - Regrouped segments by video and aligned manifests more closely to GigaSpeech2 format  
  - Prepared this repository (code organisation, configs, and documentation)

- **Weeks 11–12 – Segmentation strategies & repo cleanup**
  - Update yt-dlp crawling script with deno

