# Vibometer
## The vibe coder companion
Here's to you Vibometer, the perfect companion tool for the modern vibe coder! Just paste your code and let the vibes flow. 
Vibometer will analyze your code and give your code a score from 0 to 10, along with a description of the vibe and a visual representation of the score. 
The higher the score, the better the vibe!

**Note**: this tool is an April fool's joke and should not be taken seriously. While it does what it claims, to add dimensions
to the joke this tool was itself "vibe-coded", as you can tell from the poor interface quality. So, more than ever,
*you use this tool at your own risk, I give no guarantee whatsoever*. I only tested it with Ollama. 

What follows from here on is an LLM-generated readme for this project.




# Code Vibe Score

This is a Flask web application that evaluates the "vibe" of a given code snippet using either the OpenAI or Ollama API. The application allows users to input code, select the API provider, and specify the model for Ollama. The result is displayed as a score with a corresponding needle on a meter and a text description of the vibe.

## Features

- Evaluate code snippets using OpenAI or Ollama API.
- Configure API settings and model through a settings page.
- Display a spinner while waiting for the API response.
- Show the vibe score with a needle on a meter and a text description.

## Requirements

- Python 3.13
- Flask
- Requests

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/GTP95/Vibometer
    cd Vibometer
    ```

2. Create a virtual environment:
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    ```sh
    export API_KEY='your_openai_api_key'
    export API_URL='https://api.openai.com/v1/engines/davinci-codex/completions'
    export OLLAMA_API_URL='http://localhost:11434/api/generate'
    export API_PROVIDER='openai'  # or 'ollama'
    export OLLAMA_MODEL='llama2'
    ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter your code snippet in the text area and click "Evaluate".

4. To change settings, click on the "Settings" link, update the fields, and save.

## Docker

### Build the Docker image

1. Build the Docker image:
    ```sh
    docker build -t code-vibe-score .
    ```

2. Run the Docker container:
    ```sh
    docker run --network="host" -e API_KEY='your_openai_api_key' -e API_URL='https://api.openai.com/v1/engines/davinci-codex/completions' -e OLLAMA_API_URL='http://localhost:11434/api/generate' -e API_PROVIDER='ollama' -e OLLAMA_MODEL='llama2' code-vibe-score
    ```

3. Open your web browser and go to `http://localhost:5000`.

## Project Structure

- `app.py`: Main application file.
- `templates/`: Directory containing HTML templates.
  - `index.html`: Home page template.
  - `settings.html`: Settings page template.
- `.venv/`: Virtual environment directory (ignored by Git).
- `.gitignore`: Git ignore file.

## License

This project is licensed under the GPLv3 License.
