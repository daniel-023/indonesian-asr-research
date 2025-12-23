"""
Extract per-video TXT transcripts from filtered manifests.

This script searches all:
    WORK_ROOT/<mode>/<channel>/batch_*/output_filter/filtered_*.jsonl

and writes sentence-level lines to:
    OUT_ROOT/<mode>/<channel>/<video>.txt

Each line is formatted as:
    <basename>-<start>-<end>    <text>

Batches are handled automatically; segments from the same video
are merged into one TXT file.

Usage:
    Set WORK_ROOT and OUT_ROOT, then run:
        python extract_txt_segments.py
"""

import os, json, glob
from collections import defaultdict
from pathlib import Path

# Root of your work dir
WORK_ROOT = "/scratch/users/ntu/daniel02/GigaSpeech2/id/work"
OUT_ROOT = "/scratch/users/ntu/daniel02/GigaSpeech2/id/txt_segments"

for manifest in glob.glob(f"{WORK_ROOT}/**/output_filter/filtered_*_manifest.jsonl", recursive=True):
    # Extract channel name (e.g. mono/Idntimes)
    parts = Path(manifest).parts
    # parts looks like [..., "work", "mono", "Idntimes", "batch_022", "output_filter", "filtered_...jsonl"]
    try:
        idx = parts.index("work")
        mode, channel = parts[idx+1], parts[idx+2]
    except ValueError:
        raise RuntimeError(f"'work' not found in manifest path: {manifest}")
    
    out_dir = Path(OUT_ROOT) / mode / channel
    out_dir.mkdir(parents=True, exist_ok=True)
    
    with open(manifest, "r", encoding="utf-8") as f:
        for line in f:
            ex = json.loads(line)
            
            basename = Path(ex["audio_filepath"]).stem
            start = float(ex["audio_start_sec"])
            end = start + float(ex["duration"])
            text = ex["text"].strip()

            # build utterance ID
            uttid = f"{basename}-{start:.3f}-{end:.3f}"
            out_line = "{}\t{}\n".format(uttid, text.strip())

            # append to the per-video file
            out_file = out_dir / f"{basename}.txt"
            with open(out_file, "a", encoding="utf-8") as outf:
                outf.write(out_line)