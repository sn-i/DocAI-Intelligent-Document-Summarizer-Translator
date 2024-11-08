import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from translate import Translate
from txtsummary import TxtSummary
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_text TEXT,
            summary TEXT,
            translation TEXT,
            from_lang TEXT,
            to_lang TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

def add_to_history(original_text, summary, translation, from_lang, to_lang):
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO history (original_text, summary, translation, from_lang, to_lang, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (original_text, summary, translation, from_lang, to_lang, datetime.now()))
    conn.commit()
    conn.close()

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

    # Save to history
    add_to_history(text_input, summary, translation, from_lang, to_lang)

    return render_template(
        'index.html',
        text_input=text_input,
        summary=summary,
        translation=translation,
        from_lang=from_lang,
        to_lang=to_lang
    )

# Route to view history
@app.route('/history')
def view_history():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM history ORDER BY timestamp DESC')
    history = cursor.fetchall()
    conn.close()
    return render_template('history.html', history=history)

if __name__ == "__main__":
    app.run(debug=True)
