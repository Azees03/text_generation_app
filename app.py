from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
text_generator = pipeline("text-generation", model="gpt2-large")

@app.route("/", methods=["GET", "POST"])
def index():
    generated_text = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        generated_text = text_generator(prompt, max_length=50, temperature=0.6, top_p=0.9)[0]['generated_text']
    return render_template("index.html", generated_text=generated_text)

if __name__ == "__main__":
    app.run(debug=True)
