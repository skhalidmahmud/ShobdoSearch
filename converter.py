import csv
import os
import sys

# Force UTF-8 for the terminal so Bangla characters don't crash the script
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

class BanglishConverter:
    def __init__(self, data_dir=None):
        if data_dir is None:
            # Get the directory where converter.py is located
            current_dir = os.path.dirname(os.path.abspath(__file__))
            self.data_dir = os.path.join(current_dir, 'data')
        else:
            self.data_dir = data_dir
        self.b2b_map = {}
        self.generator_map = {}
        self.word_lists = []
        # Bengali Vowels (phonetic keys)
        self.vowels = {'a', 'aa', 'i', 'ii', 'u', 'uu', 'oo', 'ri', 'e', 'oi', 'o', 'ou'}
        self.hasanta = '্'
        self.dependent_vowels = {'া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ে', 'ৈ', 'ো', 'ৌ', 'ং', 'ঃ', 'ঁ'}
        self.load_data()

    def load_data(self):
        # 1. Load ben2bn.csv (The "known" mappings)
        b2b_path = os.path.join(self.data_dir, 'ben2bn.csv')
        if os.path.exists(b2b_path):
            with open(b2b_path, encoding='utf-8-sig') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 2:
                        self.b2b_map[row[0].lower()] = row[1]

        # 2. Load banGenerator.csv (The phoneme rules)
        gen_path = os.path.join(self.data_dir, 'banGenerator.csv')
        with open(gen_path, encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            next(reader) # skip header
            for row in reader:
                if not row or not row[0]: continue
                eng = row[0].lower()
                bangla_options = [x.strip() for x in row[1:] if x.strip() and x.strip() != '""']
                if eng in self.generator_map:
                    self.generator_map[eng].extend(bangla_options)
                else:
                    self.generator_map[eng] = bangla_options

        # 3. Load Word Lists (The "dictionaries")
        self.word_weights = {} # word -> weight (lower is more common)
        
        dict_files = [
            ('BengaliWordList_40.txt', 1),
            ('BengaliWordList_48.txt', 2),
            ('BengaliWordList_112.txt', 3),
            ('BengaliWordList_439.txt', 4)
        ]

        for list_name, weight in dict_files:
            path = os.path.join(self.data_dir, list_name)
            if os.path.exists(path):
                with open(path, encoding='utf-8-sig') as f:
                    for word in f.read().splitlines():
                        word = word.strip()
                        if not word: continue
                        # Only update if new weight is lower (more common)
                        if word not in self.word_weights or weight < self.word_weights[word]:
                            self.word_weights[word] = weight

    def split_banglish(self, word):
        """Splits banglish word into the longest possible phonemes found in map."""
        word = word.lower()
        parts = []
        i = 0
        # Sort keys by length so we find 'sh' before 's'
        sorted_keys = sorted(self.generator_map.keys(), key=len, reverse=True)
        
        while i < len(word):
            found = False
            for key in sorted_keys:
                if word.startswith(key, i):
                    parts.append(key)
                    i += len(key)
                    found = True
                    break
            if not found:
                # If we don't know the letter, just skip it
                i += 1
        return parts

    def is_consonant(self, phoneme):
        return phoneme in self.generator_map and phoneme not in self.vowels

    def is_valid_word(self, word):
        """Checks if the generated Bangla word exists in our weighted dictionaries."""
        return hasattr(self, 'word_weights') and word in self.word_weights

    def get_word_priority(self, word):
        """Returns a priority score (lower is better)."""
        # Weight 1-4 from dictionaries. If not found, weight 5 (guess).
        weight = self.word_weights.get(word, 5)
        if len(word) == 1:
            weight += 2
        if word.endswith(self.hasanta):
            weight += 3
        return weight

    def expand_shorthand(self, word):
        """Generates vowel-inserted candidate variants for consonant-heavy chat shorthand."""
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_inserts = ['a', 'o', 'e', 'u', 'i']
        n = len(word)
        if n <= 1:
            return []

        digraphs = {
            'sh', 'kh', 'th', 'ch', 'gh', 'dh', 'bh', 'ph', 'ng', 'nd',
            'nt', 'st', 'kk', 'tt', 'dd', 'pp', 'bb', 'mm', 'nn', 'll',
            'ss', 'bd', 'kt', 'sk', 'sp', 'sm', 'sn', 'tr', 'dr', 'pr',
            'br', 'gr', 'kr', 'kl', 'gl', 'mr', 'sr', 'sw'
        }

        cons_indices = []
        i = 0
        while i < n - 1:
            if word[i:i+2] in digraphs:
                i += 2
                continue
            c1, c2 = word[i], word[i + 1]
            if c1 not in vowels and c2 not in vowels:
                cons_indices.append(i + 1)
            i += 1

        if not cons_indices:
            return []

        target_indices = cons_indices[:2]
        candidates = [word]
        for ins_pos in reversed(target_indices):
            new_cands = []
            for cand in candidates:
                new_cands.append(cand)
                for v in vowel_inserts:
                    new_cands.append(cand[:ins_pos] + v + cand[ins_pos:])
            candidates = new_cands

        return [c for c in candidates if c != word]

    def _generate_raw_candidates(self, banglish_word):
        """Splits banglish word and builds Bangla candidates using phonetic rules."""
        phonemes = self.split_banglish(banglish_word)
        if not phonemes:
            return []

        candidates = [("", False)]
        for p in phonemes:
            new_candidates = []
            options = self.generator_map.get(p, [p])
            is_curr_cons = self.is_consonant(p)
            
            for cand_str, last_was_cons in candidates:
                for opt in options:
                    if cand_str == "" and opt in self.dependent_vowels:
                        continue

                    current_opt = opt
                    if (p == 'a' or p == 'o') and opt == 'অ' and last_was_cons and not cand_str.endswith(self.hasanta):
                        current_opt = ""
                    
                    new_candidates.append((cand_str + current_opt, is_curr_cons))
                    
                    if last_was_cons and is_curr_cons:
                        if not cand_str.endswith(self.hasanta):
                            new_candidates.append((cand_str + self.hasanta + opt, is_curr_cons))
            
            candidates = new_candidates
            if len(candidates) > 5000:
                candidates = candidates[:5000]

        return [c[0] for c in candidates]

    def convert(self, banglish_word):
        # Handle empty or whitespace
        if not banglish_word or not banglish_word.strip():
            return banglish_word

        banglish_word = banglish_word.lower()
        
        # Step 1: Check if we already know this exact word (known map or in-memory cache)
        if banglish_word in self.b2b_map:
            return self.b2b_map[banglish_word]
        if hasattr(self, 'b2b_cache') and banglish_word in self.b2b_cache:
            return self.b2b_cache[banglish_word]

        # Step 2: Direct candidate generation
        raw_candidates = self._generate_raw_candidates(banglish_word)
        valid_candidates = []
        for cand_str in raw_candidates:
            if self.is_valid_word(cand_str):
                valid_candidates.append(cand_str)

        if valid_candidates:
            best_direct = min(valid_candidates, key=lambda x: self.get_word_priority(x))
            # If direct candidate is a high-priority match (weight <= 2), use it immediately
            if self.get_word_priority(best_direct) <= 2:
                self.save_new_mapping(banglish_word, best_direct)
                return best_direct

        # Step 3: Shorthand Vowel-Expansion for abbreviations/consonant clusters
        expansions = self.expand_shorthand(banglish_word)
        for exp_word in expansions:
            exp_raw = self._generate_raw_candidates(exp_word)
            for cand_str in exp_raw:
                if self.is_valid_word(cand_str):
                    valid_candidates.append(cand_str)

        if valid_candidates:
            best = min(valid_candidates, key=lambda x: self.get_word_priority(x))
            self.save_new_mapping(banglish_word, best)
            return best
        
        # If nothing found in dictionary, return the best guess
        best_guess = raw_candidates[0] if raw_candidates else banglish_word
        return best_guess

    def convert_sentence(self, text):
        """Converts a full sentence of Banglish text to Bangla."""
        import re
        tokens = re.split(r'(\s+|[.,!?;:])', text)
        result = []
        for token in tokens:
            if not token or not token.strip() or re.match(r'[.,!?;:]', token):
                result.append(token)
            else:
                result.append(self.convert(token))
        return "".join(result)

    def save_new_mapping(self, eng, ban):
        if not hasattr(self, 'b2b_cache'):
            self.b2b_cache = {}
        self.b2b_cache[eng] = ban

# Testing the logic
if __name__ == "__main__":
    conv = BanglishConverter()
    print("Banglish to Bangla Converter (Sentence Mode)")
    print("Type 'exit' to quit.")
    while True:
        try:
            test_text = input("\nEnter Banglish: ")
            if test_text.lower() == 'exit':
                break
            print(f"Bangla Result: {conv.convert_sentence(test_text)}")
        except EOFError:
            break
        except KeyboardInterrupt:
            break
