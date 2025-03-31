from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests
import os

app = Flask(__name__)

# Load settings from environment variables or default values
API_KEY = os.getenv('API_KEY', 'your_openai_api_key')
API_URL = os.getenv('API_URL', 'https://api.openai.com/v1/engines/davinci-codex/completions')

def get_vibe_score(code):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': f'Rate the following code from 0 to 10:\n\n{code}',
        'max_tokens': 1
    }
    response = requests.post(API_URL, headers=headers, json=data)
    score = response.json()['choices'][0]['text'].strip()
    return int(score)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    code = request.form['code']
    score = get_vibe_score(code)
    return jsonify({'score': score})

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global API_KEY, API_URL
    if request.method == 'POST':
        API_KEY = request.form['api_key']
        API_URL = request.form['api_url']
        # Save settings to environment variables or a file
        os.environ['API_KEY'] = API_KEY
        os.environ['API_URL'] = API_URL
        return redirect(url_for('index'))
    return render_template('settings.html', api_key=API_KEY, api_url=API_URL)

if __name__ == '__main__':
    app.run(debug=True)