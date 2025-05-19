import fitz  # PyMuPDF

# Step 1: Extract Text from IPC PDF
def extract(file): 
    text = "" 
    with fitz.open(file) as pdf: 
        for page in pdf: 
            text += page.get_text() 
    return text 

# Step 2: Search for Relevant Sections in IPC
def search(query, ipc): 
    query = query.lower() 
    lines = ipc.split("\n") 
    results = [] 
    for line in lines: 
        if query in line.lower(): 
            results.append(line)  
    if results: 
        return results 
    else:   
        return ["No relevant section found."]    

# Step 3: Main Chatbot Function
def chatbot(): 
    print("Loading IPC document...") 
    ipc = extract("IPC_Crimes_and_Punishments.pdf") 
    print("Chatbot ready. Type 'exit' to quit.")
    while True: 
        query = input("Ask a question about the IPC: ") 
        if query.lower() == "exit": 
            print("Goodbye!") 
            break 
        results = search(query, ipc) 
        print("\n".join(results)) 
        print("-" * 50)

# Run the chatbot
chatbot()

