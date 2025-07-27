import requests


GROQ_API_KEY = ""


MODEL_NAME = "llama3-8b-8192"


GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"


headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

BUSINESS_SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a helpful AI assistant specialized in business topics. "
        "Only answer questions that are related to business, such as market insights, invoices, client communication, data summaries, and similar topics. "
        "If a user asks something unrelated to business, politely respond that you can only assist with business-related queries."
    )
}

conversation = []

def get_groq_response(messages):
    # Always prepend the business system prompt
    full_messages = [BUSINESS_SYSTEM_PROMPT] + [m for m in messages if m["role"] != "system"]
    payload = {
        "model": MODEL_NAME,
        "messages": full_messages,
        "temperature": 0.7,
        "max_tokens": 512
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(" Error:", response.status_code)
        print(response.text)
        return None

def chat():
    print(" Groq Chatbot is ready! Type your message (or 'exit' to quit):\n")

    while True:
        user_input = input(" You: ")
        if user_input.lower() in {"exit", "quit"}:
            print(" Goodbye!")
            break

       
        conversation.append({"role": "user", "content": user_input})

        
        reply = get_groq_response(conversation)

        if reply:
            print(" Groq:", reply)
           
            conversation.append({"role": "system", "content": "You are a business-focused AI assistant. Only respond to queries about business, finance, marketing, operations, or customer service. If a user asks something unrelated (like jokes, general knowledge, or random questions), politely say: 'I'm designed to assist only with business-related topics.' Always answer professionally and concisely."})
        else:
            print(" Failed to get a response. Try again later.")

if __name__ == "__main__":
    chat()
    

