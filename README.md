## Text Summarizer Web App

This project is a simple Flask-based web application that summarizes large pieces of text using Azure’s AI Language Service. It performs extractive summarization, selecting key sentences from the original input to generate a concise summary.

Features
	<li>Summarize text input into a few important sentences.
	<li>Error handling for empty or invalid inputs.
	<li>Clean and simple web interface.
	<li>Uses Azure’s Text Analytics API for high-quality results.

Technologies Used
	<li>Python 3
	<li>Flask
	<li>Azure AI Language Service
	<li>dotenv (for environment variable management)
	<li>HTML/CSS (for the front-end)

Setup Instructions

1. Clone the Repository
```
git clone https://github.com/yourusername/text-summarizer-webapp.git
cd text-summarizer-webapp
```

2. Create and Activate Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Required Packages
```
pip install -r requirements.txt
```

4. Set Up Environment Variables

Create a .env file in the project root and add:

```
AZURE_AI_KEY=your_azure_key_here
ENDPOINT_TO_CALL_LANGUAGE_API=your_azure_endpoint_here
```

5. Run the Application
```
python main.py
```

6. Access the Web App
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

API Endpoint
	<li>POST /summarize
	<li>Request body (JSON):
```
{
  "text": "your text to summarize"
}
	•	Response (JSON):
{
  "summary": "Summarized text here"
}

```

Project Structure
```
├── main.py
├── templates
│   └── Home.html
├── static
│   └── css
│       └── styles.css
├── .env
├── requirements.txt
└── README.md
```
## Notes
<li>This is meant for development use only. For production, configure a production-grade WSGI server (like Gunicorn) and proper security settings.
<li>Make sure you have a valid Azure subscription and the Text Analytics resource enabled. go to this url to get one: 

```
https://ai.azure.com
```
