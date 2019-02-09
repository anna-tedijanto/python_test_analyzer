import ast

### Does this string contain hello world?
def findHello(content):
    code = ast.parse(content)
    for node in ast.walk(code):
        if isinstance(node, ast.Str) and "Hello, World!" == node.s:
            return True

    return False

def getContent(filename):
    with open(filename, 'r') as f:
        return f.read()
