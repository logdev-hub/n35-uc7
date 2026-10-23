import sys
import fitz

for path in sys.argv[1:]:
    doc = fitz.open(path)
    print(f"FILE {path} PAGES {len(doc)}")
    for index, page in enumerate(doc, 1):
        text = " ".join(page.get_text("text").split())
        print(f"{index:03d}: {text[:240]}")
