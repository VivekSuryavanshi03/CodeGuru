# CodeGuru: A Code Teaching Assistant

Check out the live application: [CodeGuruT](https://838bb905eb1e585e5f.gradio.live) 

This is a Gradio-based frontend application using LangChain and Codellama models. The application serves as a code assistant, answering code-related questions based on user prompts.

## Requirements

- Python 3.x
- Required libraries:
  - `langchain`
  - `gradio`

## Model Configuration

The model used for this project is `CodeLlama`, and it is designed to act as a code teaching assistant. The model is pre-configured with the following settings:

- **Model**: `codellama`
- **Temperature**: `1` (used to control the randomness of responses)
- **System Prompt**:
    ```
    You are a code teaching assistant named CodeGuru created by Vivek (BABU). Answer all the code-related questions being asked.
    ```

## Setup and Usage

To get the application running on your local machine, follow the instructions below.

### 1. Clone the Repository
```bash
https://github.com/VivekSuryavanshi03/CodeGuru.git
```

### 2. Install Dependencies and Run in One Step
```bash
pip install -r requirements.txt && python app.py
```

