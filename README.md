# Search Engine Web App

A Flask-based AI-powered search engine that utilizes Google Gemini AI to generate relevant search results. The app provides a user-friendly interface with a modern, responsive design.

## 🚀 Features
- AI-powered search using Google Gemini API
- Clean and modern UI with a centered search box
- Responsive design for various screen sizes
- JSON-based search result formatting

## 📌 Tech Stack
- **Backend:** Flask, Google Gemini AI
- **Frontend:** HTML, CSS, JavaScript (AJAX for dynamic search results)
- **Hosting:** Localhost (Flask Development Server)

## 📂 Project Structure
```
Search_Engine-Web-App/
│── static/
│   ├── style.css          # Frontend styling
│── templates/
│   ├── index.html         # Main UI for search
│── app.py                 # Main Flask application
│── config.py              # API key configuration
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

## 🔧 Installation & Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/Md-Abu-Omayer-Babu/Search_Engine-Web-App.git
   cd Search_Engine-Web-App
   ```
2. **Create a Virtual Environment (Optional)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Configure API Key**
   - Create a `config.py` file and add your **Google Gemini API Key**:
     ```python
     GEMINI_API_KEY = "your_api_key_here"
     ```
5. **Run the Application**
   ```sh
   python app.py
   ```
6. **Access the Web App**
   - Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## 📜 Usage
1. Enter a search query in the input box.
2. Click the **Search** button.
3. AI-generated search results will appear below.

## 🛠 Troubleshooting
- **500 Internal Server Error?**
  - Check if your `config.py` contains the correct API key.
  - Ensure all dependencies are installed.
- **Empty Search Query Error?**
  - Enter a valid search term before submitting.

## 📄 License
This project is licensed under the MIT License.

---

👨‍💻 Developed by [Md Abu Omayer Babu](https://github.com/Md-Abu-Omayer-Babu) 🚀
