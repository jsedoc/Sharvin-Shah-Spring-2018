from create_tree import *
from nltk import Tree

my_tree = generate_data(4)
pprint(my_tree)
tree_text = ' '.join(str(e) for e in convert_to_list_nltk(my_tree,[]))
print(tree_text)

nltk_tree = Tree.fromstring(tree_text)

from nltk.treeprettyprinter import * 
print(TreePrettyPrinter(nltk_tree).text())
print(nltk_tree)

converted_tree = Node(0)
converted_tree = convert_nltk_tree_to_binarytree(nltk_tree, converted_tree)
print(converted_tree)
