import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

header = {
    'Content-Type': 'application/json'
}
history = []

def generate_response(prompt):
    history.append(f"User: {prompt}")
    final_prompt = "\n".join(history)
    data = {
        "model": "codeWIFI",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=header, data=json.dumps(data))

    if response.status_code == 200:
        response = response.text
        data = json.loads(response)
        actual_response = data['response']
        history.append(f"Bot: {actual_response}")
        # Return the entire conversation history as a dynamic output
        return "\n".join(history)
    else:
        print("error", response.text)
        return "An error occurred while generating the response."

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt"),
    outputs=gr.Textbox(lines=15, placeholder="Response will appear here...", interactive=False),
)
interface.launch()