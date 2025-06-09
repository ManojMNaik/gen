from transformers import pipeline

# Specify the model explicitly
summarizer = pipeline(
    "summarization", 
    model="facebook/bart-large-cnn"  # You can replace this with any other summarization model if needed
)

# Function to summarize a given passage
def summarize_text(text):
    # Summarizing the text using the pipeline
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

text = """
Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. 
The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is valuable. 
NLP techniques are used in many applications, such as speech recognition, sentiment analysis, machine translation, and chatbot functionality. 
Machine learning algorithms play a significant role in NLP, as they help computers to learn from vast amounts of language data and improve their ability to process and generate text. 
However, NLP still faces many challenges, such as handling ambiguity, understanding context, and processing complex linguistic structures. 
Advances in NLP have been driven by deep learning models, such as transformers, which have significantly improved the performance of many NLP tasks.
"""

# Get the summarized text
summarized_text = summarize_text(text)

# Display the summarized text
print("Original Text:\n", text)
print("\nSummarized Text:\n", summarized_text)

