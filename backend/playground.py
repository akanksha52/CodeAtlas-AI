from tree_sitter import Language, Parser
import tree_sitter_python as tspython

PY_LANGUAGE = Language(tspython.language())

parser = Parser(PY_LANGUAGE)

code = b"""
def add(a, b):
    return a + b
"""

tree = parser.parse(code)

root = tree.root_node

print(root.type)
print(root.children)

root = tree.root_node

for child in root.children:
    print(child.type)
    
function = root.children[0]

for child in function.children:
    print(child.type)
        
for child in function.children:
    if child.type=="identifier":
        print(code[child.start_byte: child.end_byte].decode("utf-8"))
        
for child in function.children:
    if child.type=="identifier":
        print(child.text.decode("utf-8"))