import ast
code = "x=1+2"
tree = ast.parse(code)
for node in ast.walk(tree):
    print(type(node).__name__)