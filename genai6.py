from transformers import pipeline

# Load pre-trained sentiment-analysis pipeline
print("Loading sentiment analysis model...")
sent_an = pipeline("sentiment-analysis") 
print("Model loaded successfully!")

# Sample customer reviews (real-world application)
cf = [ 
    "I absolutely loved this phone! The battery life is amazing.",
    "Terrible service. The product stopped working within a week.",
    "It's okay, not as good as I expected.",
    "Amazing picture quality and very fast delivery!",
    "Worst purchase ever. I want my money back!"
]

# Analyze each review
for f in cf: 
    sr = sent_an(f)  # Get the first result from the list
    sl = sr[0]['label']
    sc = sr[0]['score']
    print(f"\nReview: {f}")
    print(f"Sentiment: {sl} (Confidence: {sc:.2f})\n")

