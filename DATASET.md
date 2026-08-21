# Dataset Documentation: ShobdoSearch

This document describes the datasets and corpora used by the ShobdoSearch transliteration engine.

---

## 1. Phonetic Rules Matrix (`banGenerator.csv`)
The foundational phonetic mapping matrix. Maps Romanized character sequences to corresponding Bengali characters in order of phonetic likelihood.
- **Structure**: Exactly 7 columns (`EngLit, Ben1, Ben2, Ben3, Ben4, Ben5, Ben6`).
- **Total Rules**: 111 rules covering vowels, consonants, digraphs (`kh`, `sh`, `th`, `ch`, `gh`, `dh`, `bh`, `ph`, `ng`, `nd`), and conjuncts (`kt`, `bd`, `bdh`, `st`, etc.).

---

## 2. High-Frequency Baseline Dictionary (`ben2bn.csv`)
A curated, pre-indexed mapping of high-frequency Banglish words to accurate Bangla Unicode text.
- **Total Words**: **2,770+ unique mappings**.
- **Organization**: Alphabetically sorted from A to Z (`a` through `z`).
- **Coverage**: Top 80%+ of everyday spoken, written, and chat-shorthand vocabulary (pronouns, tenses, question words, numbers, adjectives, common nouns).

---

## 3. Weighted Dictionary Corpora (`BengaliWordList_*.txt`)
Used for candidate validation and frequency-based ranking across **464,411 words**:

| File Name | Word Count | Tier / Weight | Description |
| :--- | :--- | :---: | :--- |
| `BengaliWordList_40.txt` | ~40,000 | Weight 1 | Highest-frequency core vocabulary |
| `BengaliWordList_48.txt` | ~48,000 | Weight 2 | Common everyday conversational words |
| `BengaliWordList_112.txt` | ~112,000 | Weight 3 | Intermediate and domain-specific terms |
| `BengaliWordList_439.txt` | ~439,000 | Weight 4 | Comprehensive Bengali lexicon & inflections |

---

## 4. In-Memory Session Cache (`b2b_cache`)
Dynamic in-memory cache managed at runtime by `BanglishConverter`. Stores dynamically transliterated shorthand words for instantaneous $O(1)$ repeated access without modifying files on disk.

---

## 5. Sources & Acknowledgments
Word lists are sourced, normalized, and compiled from open-source Bengali linguistic corpora and the [BengaliDictionary](https://github.com/MinhasKamal/BengaliDictionary) repository.
