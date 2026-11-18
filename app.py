from flask import Flask
from flask import render_template
from flask import request

from services.gemini_service import ask_gemini

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html"
        )


@app.route("/ask", methods=["POST"])
def ask():
    question = request.form["question"]

    answer = ask_gemini(question)

    return {"answer": answer}


if __name__ == "__main__":
    app.run(debug=True)