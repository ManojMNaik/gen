from gensim.models import Word2Vec

# Custom Word2Vec model training function
def cw(corpus):
    model = Word2Vec(
        sentences=corpus,
        vector_size=50,    # Dimensionality of word vectors
        window=5,          # Context window size (before/after each word)
        min_count=1,       # Minimum frequency for a word to be considered
        workers=4,         # Number of worker threads
        epochs=10          # Number of training epochs
    )
    return model

# Analyze trained word embeddings
def anal(model, word):
    sw = model.wv.most_similar(word, topn=5)
    for w, s in sw:
        print(w, s)

# Domain-specific text corpus (medical/legal)
corpus = [
    "The patient was prescribed antibiotics to treat the infection.".split(),
    "The court ruled in favor of the defendant after reviewing the evidence.".split(),
    "Diagnosis of diabetes mellitus requires specific blood tests.".split(),
    "The legal contract must be signed in the presence of a witness.".split(),
    "Symptoms of the disease include fever, cough, and fatigue.".split(),
]

# Train the model on the custom corpus
model = cw(corpus)

# Analyze word similarities
print("Analysis for word 'patient'")
anal(model, "patient")

print("\nAnalysis for word 'court'")
anal(model, "court")

