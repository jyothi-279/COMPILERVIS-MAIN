def evaluate_expression(node):
    if "num" in node:
        return node["num"]
    left = evaluate_expression(node["left"])
    right = evaluate_expression(node["right"])
    op = node["op"]
    return {
        "+": left + right,
        "-": left - right,
        "*": left * right,
        "/": left / right
    }[op]
