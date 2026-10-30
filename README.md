# Text Analyzer

## Project Description
Text Analyzer is a simple web application built with Python and Flask. It allows users to enter text and view basic statistics about the submitted content.

## Features
- Count the total number of words.
- Count the total number of characters.
- Count the number of sentences.
- Calculate the average word length.

## Technologies Used
- Python
- Flask
- HTML and CSS
- Pytest
- Git and GitHub
- GitHub Actions

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/CrystalNicole3/text_analyzer.git
   ```

2. Navigate into the project folder:
   ```bash
   cd text_analyzer
   ```

3. Create and activate a virtual environment.

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Run the following command:

```bash
python app.py
```

Open your browser and visit:

`http://127.0.0.1:5000`

## Running Automated Tests

Run the following command:

```bash
python -m pytest
```

The project includes automated tests for the text analysis functions. GitHub Actions automatically runs these tests when changes are pushed to the main branch.

## Deployment

The application is configured to use Gunicorn for deployment through the included Procfile.