import ast

def findHello():
    with open('hello.py') as f:
        content = f.read()

    code = ast.parse(content)
    for node in ast.walk(code):
        if isinstance(node, ast.Return) and "Hello, World!" == node.value.s:
            return True

    return False

print(findHello())


# exec(compile(code, filename="", mode="exec"))
