from flask import Flask, request, jsonify, send_from_directory, render_template
import os
import getpass
from ibm_watsonx_ai.foundation_models import Model
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
model_id = "ibm/granite-34b-code-instruct"
@app.route('/')
def homepage():
    return render_template('index.html')
def get_credentials():
    return {
        "url": "https://us-south.ml.cloud.ibm.com",
        "apikey": os.getenv("IBM_API_KEY")
    }
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 1000,
    "min_new_tokens": 1,
    "stop_sequences": ["<end of code>"],
    "repetition_penalty": 1
}
project_id = "f43dd9f1-8284-426c-87c8-6c42da67f73e"
space_id = os.getenv("SPACE_ID")
model = Model(
    model_id=model_id,
    params=parameters,
    credentials=get_credentials(),
    project_id=project_id,
    space_id=space_id
)
def generate_project_code(prompt_input):
    try:
        generated_response = model.generate_text(prompt=prompt_input, guardrails=False)
        return generated_response
    except Exception as e:
        return str(e)
@app.route('/generate_project', methods=['POST'])
def generate_project():
    data = request.json
    project_name = data.get('projectName')
    language = data.get('language')
    framework = data.get('framework')

    # prompt_input = f"""Write {language} code for {project_name} using {framework if framework else 'no specific framework'}."""
    prompt_input = f"""
You are an expert programmer. Generate Python code only, without any explanations, comments, or additional text.

Input: Write a Python code that prints 'Hello World!' n times with user input.
Output: 
    def print_n_times(n):
        for i in range(n):
            print("Hello World!")
    n = input("Please enter a number: ")
    print_n_times(n)

<end of code>

Input: Write a {language} code for {project_name} using {framework if framework else 'no specific framework'}.
Output:
"""

    result = generate_project_code(prompt_input)
    return jsonify({"generated_code": result})

if __name__ == '__main__':
    app.run(debug=True)
