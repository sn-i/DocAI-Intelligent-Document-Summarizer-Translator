# DocAI: Intelligent Document Summarizer & Translator

[![Watch the Demo](https://img.youtube.com/vi/K-IjX7KNEsA/0.jpg)](https://www.youtube.com/watch?v=K-IjX7KNEsA&ab_channel=SaniInauri)

**DocAI** is a powerful AI-driven tool designed to streamline document summarization and translation. Leveraging Azure Cognitive Services, this application simplifies document processing by providing concise summaries and translating text across multiple languages. Built with Flask, HTML, CSS, and SQLite, DocAI combines advanced natural language processing with a seamless user experience.

---

## 🌐 Accessing the Application
- **Home Page (`/`)**: Input text or upload a document for summarization and translation, all from an intuitive interface.
- **History Page (`/history`)**: Access previous summaries and translations, each saved with a timestamp for easy reference.

---

## 📈 Real-World Applications
DocAI addresses essential needs across various sectors by making language and document processing faster and more accessible. Here are some key use cases:

- **Business Reporting**: Quickly summarize complex reports and translate them for global teams, enhancing productivity and communication.
- **Research & Academia**: Simplify academic articles for easy review and translate research for cross-language collaboration, making information accessible to a wider audience.
- **Content Localization**: Translate and summarize marketing materials, manuals, and presentations to reach diverse audiences worldwide.

---

## 🧩 Future Improvements
DocAI is designed with scalability in mind, offering opportunities for further development:

- **Advanced AI Features**: Incorporate sentiment analysis, named entity recognition, and additional NLP functionalities for deeper content insights.

---

## 🎯 Technical Highlights

- **Azure Cognitive Services Integration**: Uses Azure Text Analytics and Translator APIs to provide summarization and translation, demonstrating effective use of cloud-based AI.
- **Full-Stack Development**: Built with Flask for backend operations and HTML, CSS, and Bootstrap for a responsive frontend.
- **SQLite Database**: Stores summary and translation history for easy retrieval, demonstrating data persistence.
- **Git & GitHub Workflow**: Maintained organized version control and collaboration, essential for ongoing development and improvements.

---

## 🛠️ Project Structure

```plaintext
DocAI/
├── app.py                     # Main Flask application with routes and logic
├── translate.py               # Module for Azure Translator API integration
├── txtsummary.py              # Module for Azure Text Analytics summarization
├── templates/
│   ├── index.html             # Main UI template for summarization and translation
│   └── history.html           # History page template
├── static/
│   └── css/
│       └── styles.css         # CSS styling for the application
├── history.db                 # SQLite database for storing history of operations
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables (API keys and configuration)

```

---

## 🔧 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sn-i/DocAI-Intelligent-Document-Summarizer-Translator.git
   cd DocAI-Intelligent-Document-Summarizer-Translator
   ```

2. **Create a Virtual Environment and Install Dependencies**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   - Create a `.env` file in the root directory with the following keys:
     ```plaintext
     LANGUAGE_KEY=<your-azure-language-key>
     LANGUAGE_ENDPOINT=<your-azure-language-endpoint>
     TRANSLATE_KEY=<your-azure-translate-key>
     TRANSLATE_API=<your-azure-translate-api>
     TRANSLATE_REGION=<your-azure-region>
     SECRET_KEY=<your-secret-key>
     ```

4. **Initialize the Database**
   - Open a Python shell and run:
     ```python
     from app import init_db
     init_db()
     ```

5. **Run the Application**
   ```bash
   flask run
   ```

   The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🌐 Using DocAI
- **Summarization & Translation**: Enter text directly, select languages, and click "Summarize & Translate" to see results in seconds.
- **History**: Access the **History** page to review all previous summaries and translations with timestamps for easy tracking.

