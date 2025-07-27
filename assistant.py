import requests

GROQ_API_URL = "https://api.groq.com/openai/v1"  # Replace with actual Groq endpoint
GROQ_API_KEY = ""  # Replace with your actual Groq API key

messages = [
    {"role": "system", "content": "You are a friendly AI assistant."}
]

def get_response(user_input):
    messages.append({"role": "user", "content": user_input})

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "Llama-3.1-8B-8192",  # Replace with the correct Groq model name
        "messages": messages
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        reply = response.json()['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"Error: {str(e)}"

print("Welcome to AI Chatbot (type 'exit' to quit)")
while True:
    user_input = input("You: ")

    if user_input.lower() in ['exit', 'quit']:
        print("Chatbot: Goodbye!")
        break

    reply = get_response(user_input)
    print("Chatbot:", reply)
