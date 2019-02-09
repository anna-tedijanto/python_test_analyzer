import ast

### Does this string contain hello world?
def findHello():
    with open('hello.py') as f:
        content = f.read()

    code = ast.parse(content)
    for node in ast.walk(code):
        if isinstance(node, ast.Str) and "Hello, World!" == node.s:
            return True

    return False
