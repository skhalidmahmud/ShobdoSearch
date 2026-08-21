# Changelog

All notable changes to this project are documented in this file.

---

## [2.0.1] - 2026-08-22

### Changed
- Updated PyPI package documentation with official download/version badges and pip usage guide.
- Bumped version to `2.0.1` for PyPI release parity.

---

## [2.0.0] - 2026-08-22

### Added
- **Dynamic Vowel-Expansion Engine**: Algorithmic recovery for consonant-heavy chat shorthand and abbreviations (`tmi`, `vlo`, `kmn`, `amr`, `tmr`, `apnr`, `bndhu`, `rsta`, `khbr`).
- **Comprehensive Base Vocabulary**: Expanded and alphabetically sorted [`data/ben2bn.csv`](file:///c:/Users/Khalid/OneDrive/Desktop/Git%20clone/Antigravity/ShobdoSearch/data/ben2bn.csv) to **2,770+** high-frequency words covering 80%+ daily conversational Bengali.
- **Extended Phonetic Rules**: Added missing phonemes (`v`, `f`, `w`, `x`, `z`, `q`) and digraph conjuncts (`bd`, `bdh`, `kt`, `st`) to `data/banGenerator.csv`.
- **Comprehensive Test Suite**: Added [`verify.py`](file:///c:/Users/Khalid/OneDrive/Desktop/Git%20clone/Antigravity/ShobdoSearch/verify.py) with 41 core test cases (100% pass rate).

### Changed
- **In-Memory Cache Architecture**: Replaced disk-writing in `converter.py` with in-memory `self.b2b_cache` to prevent dataset pollution during runtime.
- **CSV Standardization**: Cleaned and standardized `data/banGenerator.csv` to an exact 7-column matrix across all 111 phoneme rows.
- **Dictionary Priority Scoring**: Refined `get_word_priority` with trailing hasanta and 1-letter word penalties, removing detrimental length tie-breakers.

### Fixed
- **Leading Dependent Vowels**: Fixed bug causing vowel signs (kars like `া`, `ে`, `ি`) to attach at the beginning of words (e.g. `eta` → `এটা` instead of `েটা`).
- **Implicit Vowel Dangling Hasanta**: Fixed implicit vowel suppression to preserve explicit hasanta endings.
- **API Stats Endpoint**: Fixed dictionary size calculation in `/stats` to accurately return the 464,411 loaded dictionary words instead of 0.

---

## [0.2.0] - 2026-05-09
### Changed
- Refactored logic from Jupyter Notebook to modular `converter.py`.
- Implemented recursive candidate generation.
- Replaced linear dictionary search with set-based lookups.

### Fixed
- Windows UTF-8 terminal encoding support.
- Longest-match phoneme splitting for `kh`, `sh`.

---

## [0.1.0] - 2026-05-09
### Added
- Initial project structure with `data/` and basic phoneme mappings.
