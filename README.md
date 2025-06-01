Local LLM Prompt Runner
This repository contains a simple Python script (llm_prompt.py) that programmatically sends a prompt to a local Large Language Model (LLM) using Ollama and prints the response. The script fulfills the requirements of running a local LLM, sending a prompt, and retrieving a response without using CLI commands.
Features

Uses the ollama Python library to interact with a local LLM.
Configurable model (e.g., llama3.1, mistral, phi, dolphin, tinyllama).
Sends a sample prompt ("What is the capital of France?") and prints the response.
Error handling for robust execution.
Single, self-contained script for easy setup and execution.

Prerequisites

Python 3.6+: Ensure Python is installed on your system.
Ollama: Download and install Ollama from https://ollama.com for your platform (Mac, Linux, or Windows).
Ollama Python Library: Install the required Python package (see setup instructions below).
LLM Model: A model like llama3.1 must be pulled using Ollama (instructions below).

Setup Instructions

Install Ollama:

Download and install Ollama from https://ollama.com.
Pull the desired model (e.g., llama3.1) by running the following command in your terminal:ollama pull llama3.1

You can replace llama3.1 with mistral, phi, dolphin, or tinyllama as needed.


Install Python Dependencies:

Install the ollama Python library using pip:pip install ollama




Clone the Repository:

Clone this repository to your local machine:git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>





Running the Script

Ensure Ollama is running on your system (Ollama runs as a local server by default).
Run the script using Python:python llm_prompt.py


The script will:
Use the llama3.1 model (configurable in the script).
Send the prompt: "What is the capital of France?"
Print the prompt, model name, and the LLM's response (e.g., "The capital of France is Paris.").



Customizing the Script

Change the Model: Edit the model variable in llm_prompt.py to use a different model (e.g., mistral, phi, etc.). Ensure the model is pulled via ollama pull <model_name> first.
Change the Prompt: Modify the prompt variable in llm_prompt.py to send a different question to the LLM.

Example Output
Prompt: What is the capital of France?
Model: llama3.1
AI Response:
The capital of France is Paris.

Notes

The script is designed to be simple and self-contained, meeting the submission guidelines.
Ensure the Ollama server is running before executing the script.
If you encounter errors, verify that the model is correctly installed and Ollama is accessible.
The script avoids CLI commands, using the ollama Python library for programmatic access.

License
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Built using Ollama for local LLM execution.
Inspired by the need for a simple, programmatic LLM interface.

