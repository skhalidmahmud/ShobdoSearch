import sys
from converter import BanglishConverter

def test_converter():
    conv = BanglishConverter()
    
    test_cases = [
        ("ka", "কা"),
        ("kha", "খা"),
        ("khal", "খাল"),
        ("khali", "খালি"),
        ("eta", "এটা"),
        ("kemn", "কেমন"),
        ("kemon", "কেমন"),
        ("acho", "আছো"),
        ("ami", "আমি"),
        ("tumi", "তুমি"),
        ("valo", "ভালো"),
        ("bhalo", "ভালো"),
        ("dhanyabad", "ধন্যবাদ"),
        ("bangla", "বাংলা"),
        ("shobdo", "শব্দ"),
        ("bondhu", "বন্ধু"),
        ("khabar", "খাবার"),
        ("pani", "পানি"),
        ("dekho", "দেখো"),
        ("dekhcho", "দেখছো"),
        ("korchi", "করছি"),
        ("bolchi", "বলছি"),
        ("ekhon", "এখন"),
        ("kothay", "কোথায়"),
        ("ki", "কি"),
        ("keno", "কেন"),
        ("bhai", "ভাই"),
        ("shob", "সব"),
        ("onek", "অনেক"),
        ("shundor", "সুন্দর"),
        ("ghor", "ঘর"),
        ("manush", "মানুষ"),
        ("kosto", "কষ্ট"),
        ("bhasha", "ভাষা"),
        ("somoy", "সময়"),
        ("roza", "রোজা"),
        ("namaz", "নামাজ"),
        ("fol", "ফল"),
        ("shokal", "সকাল"),
        ("shesh", "শেষ"),
        ("mon", "মন"),
    ]

    print("===========================================")
    print("      SHOBDOSEARCH CONVERSION TESTS       ")
    print("===========================================")
    
    passed = 0
    failed = 0
    for eng, expected in test_cases:
        actual = conv.convert(eng)
        if actual == expected:
            print(f" [PASS] {eng:12} -> {actual}")
            passed += 1
        else:
            print(f" [FAIL] {eng:12} -> {actual} (Expected: {expected})")
            failed += 1
            
    print("-------------------------------------------")
    print(f"Total: {len(test_cases)} | Passed: {passed} | Failed: {failed}")
    
    sentence_test = "ami banglay gan gai, ami banglar gan gai."
    conv_sentence = conv.convert_sentence(sentence_test)
    print("\nSentence Test:")
    print(f"Original:  {sentence_test}")
    print(f"Converted: {conv_sentence}")
    print("===========================================")
    
    if failed == 0:
        print(" ALL TESTS PASSED SUCCESSFULLY!")
    else:
        print(f" {failed} test(s) failed.")
        sys.exit(1)

if __name__ == "__main__":
    test_converter()
