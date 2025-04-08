from flask import Flask, request, jsonify

app = Flask(__name__)
# Sample data representing assessments
assessments = [
    {
        "name": "Java Developer Assessment",
        "url": "https://www.shl.com/solutions/products/product-catalog/java-developer",
        "remote_support": "Yes",
        "adaptive_support": "Yes",
        "duration": "40 minutes",
        "test_type": "Technical"
    },
    {
        "name": "Python Proficiency Test",
        "url": "https://www.shl.com/solutions/products/product-catalog/python-proficiency",
        "remote_support": "Yes",
        "adaptive_support": "No",
        "duration": "60 minutes",
        "test_type": "Technical"
    },
    {
        "name": "Cognitive Ability Test",
        "url": "https://www.shl.com/solutions/products/product-catalog/cognitive-ability",
        "remote_support": "Yes",
        "adaptive_support": "Yes",
        "duration": "30 minutes",
        "test_type": "Cognitive"
    },
    {
        "name": "Personality Assessment",
        "url": "https://www.shl.com/solutions/products/product-catalog/personality-assessment",
        "remote_support": "Yes",
        "adaptive_support": "No",
        "duration": "45 minutes",
        "test_type": "Personality"
    },
    # Add more assessments as needed
]

@app.route('/api/recommend', methods=['POST'])
def recommend_assessments():
    query = request.json.get('query')
    # Here you would implement your logic to find relevant assessments
    # For simplicity, returning all assessments for now
    return jsonify(assessments[:10])  # Return up to 10 assessments

if __name__ == '__main__':
    app.run(debug=True)
