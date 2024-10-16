import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-type': 'application/json'
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)
    data = {
        "model": "codeguru",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        data = json.loads(response.text) 
        actual_response = data['response']
        return actual_response
    else:
        print("error:", response.text)

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your Prompt"),
    outputs="text" 
)
interface.launch(share=True)


#public link = "https://838bb905eb1e585e5f.gradio.live"
