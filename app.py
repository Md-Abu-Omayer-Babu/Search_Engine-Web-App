import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
from config import GEMINI_API_KEY


app = Flask(__name__)

genai.configure(api_key=GEMINI_API_KEY)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')

    if not query:
        return jsonify({"error": "Empty search query"}), 400

    try:
        # Call Gemini AI for search results
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(query)

        # Extract relevant response content
        search_results = response.text.split("\n")[:5]  # Get top 5 lines of the response

        formatted_results = []
        for result in search_results:
            formatted_results.append({
                "title": result[:50],  # First 50 characters as title
                "link": f"https://www.google.com/search?q={query.replace(' ', '+')}",
                "snippet": result
            })

        return jsonify({"results": formatted_results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
