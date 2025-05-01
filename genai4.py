from gensim.downloader import load
import torch
from transformers import pipeline

# 🔹 Load pre-trained GloVe model (50 dimensions)
model = load("glove-wiki-gigaword-50")

# 🔹 Set manual seed for reproducibility
torch.manual_seed(42)

# 🔹 Function to enrich prompt using similar words
def enrich(prompt):
    ep = ""  # Enriched prompt
    words = prompt.split()  # Split the prompt into individual words
    for word in words:
        try:
            sw = model.most_similar(word, topn=3)  # Get top 3 similar words
            enw = [s for s, w in sw]  # Extract similar words
            ep += " " + " ".join(enw)
        except KeyError:
            # If word not in vocabulary, skip
            ep += " " + word
    return ep

# 🔹 Original input prompt
op = "lung cancer"
ep = enrich(op)

# 🔹 Display both prompts
print("Original Prompt:", op)
print("Enriched Prompt:", ep)

# 🔹 Load GPT-2 pipeline from Hugging Face Transformers
generator = pipeline("text-generation", model="gpt2", tokenizer="gpt2")

# 🔹 Generate response for original prompt
response = generator(op, max_length=200, top_p=0.95, temperature=0.7)
print("\nPrompt response:\n", response[0]["generated_text"])

# 🔹 Generate response for enriched prompt
response = generator(ep, max_length=200, top_p=0.95, temperature=0.7)
print("\nEnriched prompt response:\n", response[0]["generated_text"])

