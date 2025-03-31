from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests
import os

app = Flask(__name__)

# Load settings from environment variables or default values
API_KEY = os.getenv('API_KEY', 'your_openai_api_key')
API_URL = os.getenv('API_URL', 'https://api.openai.com/v1/engines/davinci-codex/completions')
OLLAMA_API_URL = os.getenv('OLLAMA_API_URL', 'http://localhost:11434/api/generate')
API_PROVIDER = os.getenv('API_PROVIDER', 'ollama')  # Default to OpenAI

def get_vibe_score(code):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': f'Rate the following code from 0 to 10. Answer only with a number from 0 to 10 and nothing else.\n\n{code}',
        'max_tokens': 1
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response_json = response.json()

    if 'choices' in response_json and len(response_json['choices']) > 0:
        score = response_json['choices'][0]['text'].strip()
        return int(score)
    else:
        raise ValueError("Invalid response from API: 'choices' key not found")

def get_ollama_score(code):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'llama2',
        'prompt': f'Rate the following code from 0 to 10. Answer only with a number from 0 to 10 and nothing else.\n\n{code}',
        'stream': False
    }
    response = requests.post(OLLAMA_API_URL, headers=headers, json=data)
    response_json = response.json()

    if 'response' in response_json:
        score = response_json['response'].strip()
        return int(score)
    else:
        raise ValueError("Invalid response from Ollama API: 'response' key not found")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    code = request.form['code']
    if API_PROVIDER == 'ollama':
        score = get_ollama_score(code)
    else:
        score = get_vibe_score(code)
    return jsonify({'score': score})

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global API_KEY, API_URL, OLLAMA_API_URL, API_PROVIDER
    if request.method == 'POST':
        API_KEY = request.form['api_key']
        API_URL = request.form['api_url']
        OLLAMA_API_URL = request.form['ollama_api_url']
        API_PROVIDER = request.form['api_provider']
        # Save settings to environment variables or a file
        os.environ['API_KEY'] = API_KEY
        os.environ['API_URL'] = API_URL
        os.environ['OLLAMA_API_URL'] = OLLAMA_API_URL
        os.environ['API_PROVIDER'] = API_PROVIDER
        return redirect(url_for('index'))
    return render_template('settings.html', api_key=API_KEY, api_url=API_URL, ollama_api_url=OLLAMA_API_URL, api_provider=API_PROVIDER)

if __name__ == '__main__':
    app.run(debug=True)