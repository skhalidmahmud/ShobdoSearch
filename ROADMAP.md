# Project Roadmap

The goal of ShobdoSearch is to deliver a robust, high-accuracy, and frictionless Banglish-to-Bangla transliteration engine.

---

## 📍 Phase 1: Foundational Engine (Completed)
- [x] Longest-match phonetic splitting logic.
- [x] Recursive candidate generation.
- [x] Multi-tier dictionary validation across 464k+ words.
- [x] Modular object-oriented Python architecture (`converter.py`).

## 📍 Phase 2: Shorthand & Accuracy Optimization (Completed)
- [x] **Dynamic Vowel-Expansion Engine**: Algorithmic recovery for consonant-heavy chat slang (`tmi`, `vlo`, `kmn`, `apnr`, `bndhu`, `rsta`).
- [x] **2,770+ Core Vocabulary Seed Map**: Alphabetically sorted base dictionary covering 80%+ daily vocabulary.
- [x] **In-Memory Caching**: High-speed session caching (`b2b_cache`) with zero disk pollution.
- [x] **Orthographic Corrections**: Fixed leading dependent vowel diacritics and dangling hasantas.
- [x] **Standardized CSV Rulebook**: Aligned 111 phoneme rules into a strict 7-column matrix.

## 📍 Phase 3: Web Platform & API (Completed)
- [x] **Modern Glassmorphic UI**: Responsive web app with live transliteration.
- [x] **FastAPI Backend**: Fully operational `/convert` and `/stats` endpoints.
- [x] **Voice Typing Integration**: Web Speech API for voice-to-text input.
- [x] **PWA & Offline Ready**: Service Worker and Web Manifest for desktop/mobile installation.

## 📍 Phase 4: Future Enhancements (Planned)
- [ ] **Context-Aware Language Model**: Bigram / Trigram n-gram scoring for adjacent word context.
- [ ] **Browser Extension**: Chrome & Firefox extension for universal typing in web forms.
- [ ] **Mobile Keyboard Layouts**: Android and iOS keyboard SDK integration.
