import re
from fa import FA
from menu import Menu


#Object made of Value(ID or Const) and the Code
class Aux:
    def __init__(self,val,cod):
        self.value=val
        self.cod=cod

    def value(self):
        return self.value()

    def cod(self):
        return self.cod()

    def __str__(self):
       return f"{self.value} {self.cod}"

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    #We take as parameters the key that we want to insret into the BST
    def insert(self, key):
        self.root = self.insert_recursive(self.root,key)


    #We search recursively for the spot where the key needs to be inserted, so we keep the BST sorted
    #We take as parameters the root (the current node) and the key that we want to insert
    def insert_recursive(self, root, key):
        if (root is None):
            return Node(key)

        if (key.value < root.val.value):
            root.left = self.insert_recursive(root.left,key)

        if (key.value >= root.val.value):
            root.right = self.insert_recursive(root.right,key)

        return root

    #We take as parameters the key that we are searching for in the BST
    def search(self,key):
        if self.search_recursive(self.root,key) == None:
            return None

        return self.search_recursive(self.root,key).val.cod

    #Because the BST is sorted, we know how to search for the desired key and we do so recursively
    #We take as parameters the root(the current node) and the key we are searching for
    def search_recursive(self,root,key):
        if (root is None or root.val.value == key):
            return root

        if (root.val.value < key):
            return self.search_recursive(root.right, key)
        else:
            return self.search_recursive(root.left, key)

    #I chose the inorder traversal, starting from left to right, I'm taking all the values from the BST
    #This way, they will be alphabetically sorted
    def inorder(self):
        result=[]
        self.inorder_recursive(self.root,result)
        return result

    def inorder_recursive(self,root,result):
        if (root):
            self.inorder_recursive(root.left, result)
            result.append(str(root.val))
            self.inorder_recursive(root.right, result)

bst = BST()


#This reads the tokens from tokens.txt
def read_tokens():
    ITERATOR=0
    tokens=[]
    with open('tokens.txt', 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            parts = line.split()  # Split the line into words
            if len(parts) >=2:
                number = int(parts[0])
                word = parts[1]
                tokens.append((number, word))
    tokens.append((12, ' '))
    return tokens

#searching it the word is in the tokens list
def search_word(tokens,search_word):
    matching_pairs = [(number, word) for number, word in tokens if search_word == word]
    if len(matching_pairs)==0:
        return -1
    return matching_pairs


tokens=read_tokens()
#print(tokens)
print(search_word(tokens,","))
#x = re.search("#.*\$","#alooo")
#print(x)


faintegers = FA('integers.txt')
faidentifiers = FA('identifiers.txt')

menu = Menu()


def parse_text(tokens):
    result = []
    it = 0
    separators = " ,;()\n"
    local_word = ""
    words = []
    errors = []

    #SO :)
    #We made a list of separatos so we know what will be our stopping point for the worsd
    #We will ready line by line, then at every line we will read character by character

    with open('example.txt', 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char not in separators:
                    local_word+=char                    #If char is not in the separators, then we just add chars to form the word
                else:
                    if (local_word):                    #If char is a separator, we add it and then we add the separator as well
                        words.append(local_word)        #We add the separator even if the word is empty or not, because we can have
                    words.append(char)                  # space and comma, like this " ," or comma and space ", " and we must keep
                    local_word=""                       #both separators



            for word in words:
                word = word.replace('\t', '')           #then we start word by word, we remove the tabs and the endlines
                word = word.replace('\n', '')
                if (word != ''):

                    if search_word(tokens,word)==-1:

                        #x = re.search('^#.*\$$',word)   #Here we search for the identifiers and in my language they all have to
                        x=menu.uiCheck(faidentifiers, word)             #HERE WE CHECK WITH FA
                        ok=False                        #start with # and and in $
                        if (x!=False):
                            if bst.search(word) == None:    #If it is not already in the Symbol table, we generate a unique value
                                it = it + 1                 #We form the object and we insert it into the symbol table
                                a = Aux(word, it)
                                bst.insert(a)
                            pos = bst.search(word)          #Here we add the word inside the PUI, because every word that is not an error
                            result.append(("42",pos))       #has to be added inside the PUI
                            ok=True
                        #x = re.search('^\d+(nrpozitiv|nrnegativ)',word)     #Here we search for number constants that always end in
                        x = menu.uiCheck(faintegers, word)          #HERE WE CHECK WITH FA
                        if (x!=False and ok==False):                         #nrpozitiv or nrnegativ
                            if bst.search(word) == None:
                                it = it + 1
                                a = Aux(word, it)
                                bst.insert(a)
                            pos = bst.search(word)
                            result.append(("43", pos))
                            ok=True
                        x = re.search("'[a-zA-Z]'",word)                #Here we search for char constants
                        if (x!=None and ok==False):
                            if bst.search(word) == None:
                                it = it + 1
                                a = Aux(word, it)
                                bst.insert(a)
                            pos = bst.search(word)
                            result.append(("43", pos))
                            ok=True
                        x = re.search('"[a-zA-Z\d]*"',word)
                        if (x!=None and ok==False):                 #here we search for string constants
                            if bst.search(word) == None:
                                it = it + 1
                                a = Aux(word, it)
                                bst.insert(a)
                            pos = bst.search(word)
                            result.append(("43", pos))
                            ok=True

                        if ok==False:                       #If the word didn't fit anywhere, then it is an error

                            errors.append(word)

                    token_match = search_word(tokens, word)     #if it doesn't belong to the symbol table, then we just add it in the PUI
                    if (token_match!=-1):
                        #print(token_match)
                        result.append((token_match[0][0],0))

            words=[]                        #When the line finishes, we reset the words list

    print(result)
    with open("PUI.txt", 'w') as file:
        # Write each item from the list to the file, one item per line
        for item in result:
            file.write(str(item[0]) + ' ' + str(item[1]) + '\n')

    with open("ERRORS.txt", 'w') as file:
        for item in errors:
            file.write(item + '\n')



print(parse_text(tokens))








# parse_text()
#
# inorder_result = bst.inorder()
# print(inorder_result)