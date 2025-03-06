import requests

# DeepSeek API settings
API_KEY = "sk-5f1c3029619844ad96384417fb760376"
API_URL = "https://api.deepseek.com/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_deepseek_response(message):
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": message}],
        "stream": False
    }
    response = requests.post(API_URL, headers=HEADERS, json=data)
    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

# Interactive chat loop
if __name__ == "__main__":
    print("Welcome to DeepSeek Chat! Type 'quit' to exit.")
    while True:
        user_message = input("You: ")
        if user_message.lower() == "quit":
            print("Goodbye!")
            break
        reply = get_deepseek_response(user_message)
        print(f"AI: {reply}")