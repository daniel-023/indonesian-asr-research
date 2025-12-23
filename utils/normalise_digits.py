"""
Remove transcript lines with numbers

Example usage:
python remove_number_lines.py --corpus-dir /scratch/users/ntu/daniel02/Granary/gsp2_prep/clips
"""

import argparse
import re
from pathlib import Path

def remove_number_lines(corpus_dir: Path):
    txt_files = list(corpus_dir.glob("*.txt"))
    print(f"Found {len(txt_files)} text files in {corpus_dir}")

    num_pattern = re.compile(r"\d")  # matches any digit

    for txt_file in txt_files:
        lines = txt_file.read_text(encoding="utf-8").splitlines()
        # keep only lines WITHOUT any digits
        cleaned = [line for line in lines if not num_pattern.search(line)]

        if len(cleaned) < len(lines):
            txt_file.write_text("\n".join(cleaned) + "\n", encoding="utf-8")

    print("Removed lines containing numbers from text files.")

def main():
    parser = argparse.ArgumentParser(description="Remove lines containing numbers from corpus .txt files.")
    parser.add_argument("--corpus-dir", required=True, help="Path to corpus directory containing .wav and .txt pairs")
    args = parser.parse_args()

    corpus_dir = Path(args.corpus_dir).resolve()
    if not corpus_dir.exists():
        raise FileNotFoundError(f"Corpus directory not found: {corpus_dir}")

    remove_number_lines(corpus_dir)

if __name__ == "__main__":
    main()