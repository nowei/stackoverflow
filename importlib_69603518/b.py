import importlib.machinery
import inspect

module = importlib.machinery.SourceFileLoader("a", './a.py').load_module()
class_members = inspect.getmembers(module, inspect.isclass)

import ast

def get_classes(path):
    with open(path) as fh:        
       root = ast.parse(fh.read(), path)
    classes = []
    for node in ast.iter_child_nodes(root):
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)
        else: 
            continue
    return classes
    
for c in get_classes('a.py'):
    print(c)
