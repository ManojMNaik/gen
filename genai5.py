from gensim.downloader import load
import random

# Load the pre-trained GloVe model (50 dimensions)
print("Loading pre-trained GloVe model (50 dimensions)...")
model = load("glove-wiki-gigaword-50")
print("Model loaded successfully!")

# Function to construct a meaningful paragraph
def create_paragraph(iw, sws):
    paragraph = f"The topic of {iw} is fascinating, often linked to terms like\n"
    random.shuffle(sws)  # Shuffle similar words for variety
    for word in sws:
        paragraph += str(word) + ", "
    paragraph = paragraph.rstrip(", ") + "."  # Clean ending
    return paragraph

# Seed word
iw = "hacking"

# Get top 5 similar words from the GloVe model
sws = model.most_similar(iw, topn=5)
words = [word for word, similarity in sws]  # Extract only words

# Create and print paragraph
paragraph = create_paragraph(iw, words)
print(paragraph)

