import re

# Split document into single sentences
chunks = []
with open("./data/paul_graham_essay.txt", "r", encoding="utf-8") as file:
    text = file.read()
    # split by sentence
    sentences = re.split(r"[\r\n]+", text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    chunks.extend(sentences)

print(chunks)
