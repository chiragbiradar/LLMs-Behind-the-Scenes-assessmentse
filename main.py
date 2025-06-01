import requests

def get_ollama_response(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama3",  # You can change this to any model you have installed
        "prompt": prompt,
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    ai_response = get_ollama_response(prompt)
    print(f"Prompt: {prompt}\nAI Response: {ai_response}")
