from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Special logic for handling 1+1
def calculate(expression):
    if expression == "1+1":
        return "Matulog kana"
    try:
        return str(eval(expression))  # evaluate mathematical expression
    except Exception:
        return "Error"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_expression():
    data = request.json
    expression = data.get('expression', '')
    result = calculate(expression)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
