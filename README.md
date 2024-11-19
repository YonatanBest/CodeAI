# **CODEAI**

## Description

CODEAI is a Flask-based web application that integrates IBM Watson's AI capabilities to generate code snippets based on user inputs. The application takes project specifications like the programming language and framework and produces ready-to-use code, accelerating the development process.

## Features

- **User-friendly Interface**: Simple homepage to input project details.
- **AI Code Generation**: Utilizes IBM Watson's foundation models to generate language-specific code.
- **Secure Configuration**: Sensitive credentials like API keys are securely managed using environment variables.
- **Customizable Prompts**: Tailor the AI's output by adjusting input prompts.

## Technologies Used

- **Backend**: Flask
- **AI Integration**: IBM Watson
- **Frontend**: HTML (via Jinja templates)
- **Deployment**: Local or cloud environments (e.g., Heroku, AWS)

## Installation and Setup

### Prerequisites

- Python 3.7+
- Virtual Environment (optional but recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/YonatanBest/CODEAI.git
cd CODEAI
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory and add the following:

```plaintext
IBM_API_KEY=your_ibm_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

## Usage

1. Open the homepage.
2. Enter your project details (e.g., project name, language, framework).
3. Click submit to generate code.
4. View and copy the generated code from the output.

## Security

- **API Key Management**: The API key is managed securely using environment variables.
- **Sensitive Data**: Ensure `.env` is included in `.gitignore` to prevent accidental exposure.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Submit a pull request.

## Acknowledgements

- **IBM Watson** for providing the AI foundation models.
- **Flask** for the lightweight web framework.s
