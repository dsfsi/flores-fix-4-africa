import os
import sys
import argparse
import pandas as pd
from comet import load_from_checkpoint
from utils import compute_metrics, compute_token_counts, compute_token_divergence

METADATA = {
  'hau': ['dev', 'devtest'],
  'nso': ['dev', 'devtest'],
  'tso': ['devtest'],
  'zul': ['dev', 'devtest'],
}
COMET_MODEL = '../comet_model'

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-l', '--lang_code', choices=METADATA.keys(), required=True)
  parser.add_argument('-s', '--split', choices=set(value for values in METADATA.values() for value in values), required=True)
  return parser.parse_args()

def main():
  args = get_args()
  lang_code = args.lang_code
  split = args.split

  if not os.path.exists(COMET_MODEL):
    sys.exit(f'COMET model not found at {COMET_MODEL}. Please use the download_comet.py script to download the model.')
  if split not in METADATA[lang_code]:
    sys.exit(f'{lang_code} does not have the split {split}.')

  print(f'Language: {lang_code}')
  print(f'Split: {split}')

  model = load_from_checkpoint(COMET_MODEL)

  src_path = f'../data/original/{split}/eng_Latn.{split}'
  ref_path = f'../data/original/{split}/{lang_code}_Latn.{split}'
  pred_path = f'../data/corrected/{split}/{lang_code}_Latn.{split}'

  src = open(src_path).read().splitlines()
  ref = open(ref_path).read().splitlines()
  pred = open(pred_path).read().splitlines()

  bleu_score, ter_score, comet_score = compute_metrics(src, ref, pred, model)

  corrected_sentences = [[r, p] for r, p in zip(ref, pred) if r != p]
  print(f'Number of corrected sentences: {len(corrected_sentences)}')
  print(f'Token counts in original data: {compute_token_counts([l[0] for l in corrected_sentences])}')
  print(f'Token counts in corrected data: {compute_token_counts([l[1] for l in corrected_sentences])}')
  print(f'Token divergence: {compute_token_divergence([l[0] for l in corrected_sentences], [l[1] for l in corrected_sentences])}%')
  
  print(f'BLEU: {bleu_score}')
  print(f'TER: {ter_score}')
  print(f'COMET: {comet_score}')

if __name__ == '__main__':
  main()