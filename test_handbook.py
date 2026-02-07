from handbook_generator import HandbookGenerator

generator = HandbookGenerator()
text = generator.generate_handbook(
    "RNA secondary structure prediction"
)

print("Word count:", len(text.split()))
print(text[:2000])
