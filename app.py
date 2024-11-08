from flask import Flask, render_template, request, redirect, url_for, flash
from translate import Translate
from txtsummary import TxtSummary

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text_input = request.form.get('text_input')
    from_lang = request.form.get('from_lang')
    to_lang = request.form.get('to_lang')

    if not text_input:
        flash("Please provide text")
        return redirect(url_for('index'))

    # Summarize and translate
    txt_summary = TxtSummary()
    summary = txt_summary.sample_extractive_summarization(text_input)

    translator = Translate()
    translation = translator.translate_text(summary, from_lang, to_lang)

    # Pass input, summary, and translation back to the template
    return render_template(
        'index.html',
        text_input=text_input,
        summary=summary,
        translation=translation,
        from_lang=from_lang,
        to_lang=to_lang
    )

if __name__ == "__main__":
    app.run(debug=True)
