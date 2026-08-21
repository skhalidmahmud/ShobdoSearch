from converter import BanglishConverter

conv = BanglishConverter()
tests = ["ka", "kha", "nam", "kemn", "eta", "dekhcho", "acho", "ami"]
print("--- VERIFICATION RESULTS ---")
for t in tests:
    print(f"{t} -> {conv.convert(t)}")
