from flask import Flask, render_template, request, jsonify
from lexer import tokenize
from parser import parse_expression
from evaluator import evaluate_expression

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    try:
        code = request.json.get("code", "")
        tokens = tokenize(code)
        tree = parse_expression(tokens)
        result = evaluate_expression(tree) if tree else None
        return jsonify({"tokens": tokens, "tree": tree, "result": result})
    except Exception as e:
        import traceback
        traceback.print_exc() 
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
