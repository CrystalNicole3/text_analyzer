
from flask import Flask, render_template, request

# Create our Flask application
app = Flask(__name__)


# Function to analyze the submitted text
def analyze_text(text):

    # Break the text into individual words
    words = text.split()

    # Calculate text statistics
    word_count = len(words)
    character_count = len(text)

    # Count sentence-ending punctuation
    sentence_count = sum(
        text.count(mark) for mark in [".", "!", "?"]
    )

    # Calculate average word length
    if word_count > 0:
        average_word_length = round(
            sum(len(word) for word in words) / word_count, 2
        )
    else:
        average_word_length = 0

    # Return the results
    return {
        "word_count": word_count,
        "character_count": character_count,
        "sentence_count": sentence_count,
        "average_word_length": average_word_length
    }


# Home page
@app.route("/", methods=["GET", "POST"])
def home():

    results = None

    # Check whether the user submitted text
    if request.method == "POST":

        text = request.form.get("text", "")

        # Analyze the submitted text
        results = analyze_text(text)

    return render_template("index.html", results=results)


# Run the application
if __name__ == "__main__":
    app.run(debug=True)

