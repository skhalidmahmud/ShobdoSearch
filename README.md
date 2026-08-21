# 🇧🇩 Banglish-to-Bangla: Phonetic Smart Converter

[![PyPI version](https://img.shields.io/pypi/v/shobdosearch.svg)](https://pypi.org/project/shobdosearch/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/shobdosearch.svg)](https://pypi.org/project/shobdosearch/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://img.shields.io/badge/Tests-41%2F41%20Passing-brightgreen.svg)](#testing--verification)

An intelligent, rule-based, and dictionary-validated NLP engine designed to convert Romanized Bengali (Banglish) into authentic Bangla Unicode script. Features dynamic vowel-expansion for informal texting/chat shorthand, weighted multi-dictionary validation across **464,000+ words**, and an alphabetically sorted curated base dictionary of **2,770+ words** covering 80%+ of daily conversational Bengali.

---

## 🚀 Key Features

- **Dynamic Vowel-Expansion & Shorthand Recovery**: Seamlessly transliterates informal chat shorthand (e.g., `tmi` → **তুমি**, `vlo` → **ভালো**, `kmn` → **কেমন**, `amr` → **আমার**, `bndhu` → **বন্ধু**, `rsta` → **রাস্তা**).
- **Curated 2,770+ Baseline Dictionary**: Pre-indexed and alphabetically sorted mapping in [`data/ben2bn.csv`](https://github.com/skhalidmahmud/ShobdoSearch/blob/main/data/ben2bn.csv) covering top 80%+ everyday Bengali vocabulary.
- **Weighted Multi-Tier Dictionary**: Validates candidates against 464,411 words across 4 frequency tiers for maximum accuracy.
- **Modern Glassmorphic Web UI**: Responsive web app with live transliteration, history, voice typing, and clipboard utilities.
- **FastAPI Backend**: Clean RESTful endpoints (`/convert`, `/stats`) for integration into web, mobile, and desktop applications.
- **In-Memory Cache**: High-speed session caching (`b2b_cache`) without disk pollution.
- **PWA & Offline Ready**: Service Worker and Web Manifest support for mobile/desktop installability.

---

## 💻 Installation & Usage

### 1. Install via pip (Recommended)
```bash
pip install shobdosearch
```

**Python Usage:**
```python
from converter import BanglishConverter

conv = BanglishConverter()
print(conv.convert_sentence("tmi kmn aso? amr vlo lagse."))
# আউটপুট: তুমি কেমন আছো? আমার ভালো লাগছে.
```

### 2. Clone the Repository
```bash
git clone https://github.com/skhalidmahmud/ShobdoSearch.git
cd ShobdoSearch
```

### 2. Start the Web App (Recommended)
This installs required dependencies and launches the local dev server:
```bash
python run.py
```
Open your browser at **http://localhost:8080**.

### 3. Using Docker
```bash
docker build -t banglish-converter .
docker run -p 8080:8080 banglish-converter
```

### 4. Interactive CLI Mode
```bash
python converter.py
```

---

## 🧪 Testing & Verification

Run the built-in test suite to verify phonetic accuracy, edge cases, and chat shorthand recovery:
```bash
python verify.py
```

Output:
```text
===========================================
      SHOBDOSEARCH CONVERSION TESTS       
===========================================
 [PASS] ka           -> কা
 [PASS] kha          -> খা
 [PASS] eta          -> এটা
 [PASS] kemon        -> কেমন
 [PASS] ami          -> আমি
 [PASS] tumi         -> তুমি
 [PASS] valo         -> ভালো
 [PASS] shundor      -> সুন্দর
 [PASS] manush       -> মানুষ
 [PASS] ghor         -> ঘর
 ...
-------------------------------------------
Total: 41 | Passed: 41 | Failed: 0
 ALL TESTS PASSED SUCCESSFULLY!
```

---

## 🛠️ API Reference

- **Interactive Documentation**: `http://localhost:8080/docs`
- **Transliterate Endpoint**:
  ```http
  POST /convert
  Content-Type: application/json

  {
    "text": "tmi kmn aso? amr khub vlo lagse."
  }
  ```
  **Response**:
  ```json
  {
    "original": "tmi kmn aso? amr khub vlo lagse.",
    "converted": "তুমি কেমন আছো? আমার খুব ভালো লাগছে."
  }
  ```
- **Stats Endpoint**:
  ```http
  GET /stats
  ```
  Returns dictionary size, active rules, and baseline mappings count.

---

## 📄 License
Distributed under the MIT License. See `LICENSE` for details.
