
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



def parse_text():
    ITERATOR=0
    with open('example.txt', 'r', encoding='utf-8') as file:
        sentence=""

        #I chose to read until EndOfLine, just to keep things more organised

        while True:
            char = file.read(1)
            sentence=sentence+char
            ok=True
            start_index = 0
            if char == '\n':
                while ok==True:
                    found_at=sentence.find('#', start_index)
                    ended_at=sentence.find('$', start_index)
                    if found_at == -1:
                        ok=False
                        break
                    ID=""                                               #We know that the IDS have to start with a # and end in a $
                    for c in range (found_at,ended_at+1):               #So we just search for them. We combine the characters into the
                        ID=ID+sentence[c]                               #ID value. We search to see if it was added in the BST and if it wasnt
                    start_index=ended_at+1                              #We add it, incrementing the code by one

                    if bst.search(ID) == None:
                        ITERATOR = ITERATOR + 1
                        elem = Aux(ID, ITERATOR)
                        bst.insert(elem)
                    #print(ID)
                ok=True
                start_index=0

                while ok == True:
                    found_at = sentence.find('nrpozitiv', start_index)
                    if found_at == -1:
                        ok = False
                                                                        #What I explained above, but for constants
                    if (found_at==-1):                                  #In this case, for positive numbers
                        break
                    const = ""

                    poz=found_at

                    for c in range(1, found_at+1):
                        if sentence[poz-c]>='0' and sentence[poz-c]<='9':
                            const = const + sentence[poz-c]
                        else:
                            break
                    start_index = found_at + 10
                    const=const[::-1]

                    if bst.search(const) == None:
                        ITERATOR = ITERATOR + 1
                        elem = Aux(const, ITERATOR)
                        bst.insert(elem)
                ok=True
                start_index=0


                while ok == True:
                    found_at = sentence.find('nrnegativ', start_index)
                    if found_at == -1:
                        ok = False

                    if (found_at==-1):
                        break
                    const = ""                                           #For negative numbers

                    poz=found_at

                    for c in range(1, found_at+1):
                        if sentence[poz-c]>='0' and sentence[poz-c]<='9':
                            const = const + sentence[poz-c]
                        else:
                            break
                    start_index = found_at + 10
                    const=const[::-1]

                    if bst.search(const) == None:
                        ITERATOR=ITERATOR+1
                        elem=Aux(const,ITERATOR)
                        bst.insert(elem)
                sentence = ""

            if not char:
                print('Reached end of file')
                break


parse_text()

inorder_result = bst.inorder()
print(inorder_result)