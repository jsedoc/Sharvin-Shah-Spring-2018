from binary_tree import *
import random, numpy

MAX_VALUE=60

def make_two_children(my_tree, max_num):
    if my_tree.left == None and my_tree.right == None:
        pass
    elif my_tree.left != None and my_tree.right == None:
        my_tree.right = Node(max_num + 1)
        max_num +=1
        max_num = make_two_children(my_tree.left,max_num)

    elif my_tree.left == None and my_tree.right != None:
        my_tree.left = Node(max_num + 1)
        max_num +=1
        max_num = make_two_children(my_tree.right, max_num)
    else:
        max_num = make_two_children(my_tree.right, max_num)
        max_num = make_two_children(my_tree.left,max_num)
    return max_num

def change_nts(my_tree):
    operators = ['+','-','/','*']
    if my_tree.left != None or my_tree.right !=None:
        my_tree.value = operators[ random.randrange(len(operators))]
        change_nts(my_tree.left)
        change_nts(my_tree.right)


def generate_data(depth):
    #my_tree = tree(height=depth, balanced=False)
    my_tree = tree(height=depth, balanced=False, max_num=MAX_VALUE)
    #pprint(my_tree)
    # make sure that every node has two children
    make_two_children(my_tree, inspect(my_tree)['max_value'])
    return my_tree

def convert_to_list_inorder(my_tree, my_list):
    if my_tree.left != None:
        my_list.append('(')
        my_list = convert_to_list_inorder(my_tree.left, my_list) 

    my_list.append(my_tree.value)

    if my_tree.right != None:
        my_list = convert_to_list_inorder(my_tree.right, my_list) 
        my_list.append(')')

    return my_list

def convert_to_list_nltk(my_tree, my_list):

    if my_tree.left != None:
        my_list.append('(')
        my_list.append(my_tree.value)
        my_list = convert_to_list_nltk(my_tree.left, my_list) 

    if my_tree.right != None:
        my_list = convert_to_list_nltk(my_tree.right, my_list) 
        my_list.append(')')
    if my_tree.left == None and my_tree.right == None:
        my_list += [my_tree.value]

    return my_list

def prefix(my_tree, my_list):

    if my_tree.left != None:
        my_list.append(my_tree.value)
        my_list = prefix(my_tree.left, my_list) 

    if my_tree.right != None:
        my_list = prefix(my_tree.right, my_list) 
    if my_tree.left == None and my_tree.right == None:
        my_list += [my_tree.value]

    return my_list

def convert_nltk_tree_to_binarytree(nltk_tree, my_tree):
    if type(nltk_tree) == type(''):
        import pdb; pdb.set_trace()
    my_tree.value = nltk_tree.label()

    # import pdb; pdb.set_trace()
    if len(nltk_tree) > 2:
        raise ValueError('We can only take binary trees')
    if len(nltk_tree) > 1:
        my_tree.right = Node(0)
        if type(nltk_tree[1]) != type(''):
            convert_nltk_tree_to_binarytree(nltk_tree[1], my_tree.right)
        else:
            my_tree.right = Node(nltk_tree[1])
    if len(nltk_tree) > 0:
        my_tree.left = Node(0)
        if type(nltk_tree[0]) != type(''):
            convert_nltk_tree_to_binarytree(nltk_tree[0], my_tree.left)
        else:
            my_tree.left = Node(nltk_tree[0])


    return my_tree


from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token not in prec.keys() and token != ')': #token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

if __name__ == "__main__":
    my_tree = generate_data(2)
    #pprint(my_tree)
    change_nts(my_tree)
    #pprint(my_tree)

    my_list = convert_to_list_inorder(my_tree,[])
    infix_tree = ' '.join(str(e) for e in my_list)

    #print infix_tree
    #print(infixToPostfix(infix_tree))
    print(' '.join(str(e) for e in prefix(my_tree,[])))
    print(' '.join(str(e) for e in convert_to_list_nltk(my_tree,[])))
    #print convert(my_tree)
