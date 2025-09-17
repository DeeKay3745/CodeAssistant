## Code Assistant (Gradio + Local API)

This project provides a simple chat-style code assistant interface built with Gradio.
It connects to a locally running model API (via http://localhost:11434/api/generate) and allows you to interact with it through a web UI.

# Features
	- 💬 Interactive chatbot interface with conversation history
	-	🔗 Connects to a local model API (e.g., Ollama or similar server)
	-	📝 Persists conversation history within the session
	-	🖥️ Built with Gradio for a clean and user-friendly frontend
	-	⚡ Supports multi-line inputs and flexible outputs

 # Requirements
	•	Python 3.10+
	•	A running local API at http://localhost:11434/api/generate (replace URL if different)

 # Install dependencies
 pip install -r requirements.txt

# Usage

	1.	Start your local model API
    Make sure your model server is running at http://localhost:11434/api/generate.
	2.	Run the app
    python app.py
  3. Open in browser
     Gradio will start a local server (default: http://127.0.0.1:7861) where you can interact with the chatbot.

# Customizing the Model

  In the file app.py, the model is defined inside the payload:

    data = {
      "model": "codeWIFI",   # <--- model name
      "prompt": final_prompt,
      "stream": False
  }
  Replace "codeWIFI" with the model you want to use.
	  - Examples:
	•	"llama2"
	•	"mistral"
	•	"codellama"
 Make sure the chosen model is installed and available in your local API backend.

# Project Structure
.
├── app.py             # Main application file
├── requirements.txt   # Dependencies
└── README.md          # Project documentation

# Notes
  •	Update the url variable in app.py if your API runs on a different port or endpoint.
	•	The conversation history is session-based and resets when you restart the app.
	•	You can switch outputs in Gradio to gr.Code(language="python") if you want syntax-highlighted code responses.
