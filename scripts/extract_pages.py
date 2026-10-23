import sys
import fitz

doc = fitz.open(sys.argv[1])
start = int(sys.argv[2])
end = int(sys.argv[3])
for page_no in range(start, min(end, len(doc)) + 1):
    print(f"\n===== PAGE {page_no} =====\n")
    print(doc[page_no - 1].get_text("text"))
