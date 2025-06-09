from gensim.downloader import load
import torch
from transformers import pipeline

# Load pre-trained word embeddings (GloVe)
model = load("glove-wiki-gigaword-50")
torch.manual_seed(42)

# Define contextually relevant word enrichment
def enrich(prompt):
    ep = ""# Start with the original prompt
    words = prompt.split() # Split the prompt into words
    for word in words:
        sw = model.most_similar(word, topn=3)
        print("Test Data\n",sw)
        enw=[]
        for s,w in sw:
            enw.append(s)
        ep+=" " + " ".join(enw)
    return ep

# Example prompt to be enriched
op = "lung cancer"
ep = enrich(op)

# Display the results
print("Original Prompt:", op)
print("Enriched Prompt:", ep)
generator = pipeline("text-generation", model="gpt2")#, tokenizer="gpt2")
response = generator(op, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2)#top_p=0.95, temperature=0.7)
print("\n\nPrompt response\n",response[0]["generated_text"])
response = generator(ep, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2) #top_p=0.95, temperature=0.7)
print("\n\nEnriched prompt response\n",response[0]["generated_text"])