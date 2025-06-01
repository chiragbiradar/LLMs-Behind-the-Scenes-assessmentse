import ollama

def run_llm_prompt(model_name: str, prompt: str) -> str:
    """
    Run a prompt through a local LLM using Ollama and return the response.
    
    Args:
        model_name (str): Name of the LLM model (e.g., 'llama3.1')
        prompt (str): The prompt to send to the LLM
    
    Returns:
        str: The LLM's response
    """
    try:
        # Send prompt to the model and get response
        response = ollama.generate(
            model=model_name,
            prompt=prompt
        )
        return response['response']
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Configuration
    model = "llama3.1"  # You can change this to mistral, phi, dolphin, or tinyllama
    prompt = "What is the capital of France?"
    
    # Run the prompt
    print(f"Prompt: {prompt}")
    print(f"Model: {model}")
    print("AI Response:")
    response = run_llm_prompt(model, prompt)
    print(response)

if __name__ == "__main__":
    main()
