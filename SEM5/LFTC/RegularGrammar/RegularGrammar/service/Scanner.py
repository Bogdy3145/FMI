from domain.PIF import PIF
from domain.SymbolTable import SymbolTable
import re


class Scanner:
    def __init__(self):
        self.pif = PIF()
        self.st = SymbolTable(50)
        self.separators = ['(', ')', ' ', '\n', '[', ']', ';',':' ',', '{', '}']
        self.operators = ["plus", "minus", "ori", "impartit_la", "ia_locul_la", "mai_mic_ca", "mai_mic_egal_ca", "egal_cu", "mai_mare_egal_ca", "mai_mare_ca", "diferit_de", "modulo"]

        self.reservedWords = ["lista", "constanta", "altfel", "daca", "atunci", "numar_intreg", "cuvant", "ori_alba_ori_neagra", "caracter_simplu",
                              "numar_cu_virgula","de_tip", "IDENTIFIER", "CONST",
                              "citeste", "EU_BOGDAN_DECLAR", "cat_timp", "fa", "printeaza_urmatoarele", "armaghedon", "amin", "no_dai", "no_stai"]
        self.errors = ""
        #[ ] ( ) { } : ; , space

    def scan(self, filename):
        file = open(filename, 'r')
        token = ""
        lines = file.readlines()
        for line in lines:
            newLine = line.replace('\n', '')
            for character in newLine:
                if character in self.separators:
                    self.classifyToken(token, lines.index(line))
                    token = ""
                    self.classifyToken(character, lines.index(line))
                else:
                    token += character

        self.writeToFile(self.pif.__str__(), "pif.out")
        self.writeToFile(self.st.__str__(), "st.out")
        if self.errors == "":
            return "lexically correct"

        return self.errors

    def classifyToken(self, token, pos):
        if token == '' or token == ' ':
            return
        if token in self.reservedWords or token in self.operators or token in self.separators:
            self.pif.add(token, 0)
        elif self.checkConstant(token) or self.checkIdentifier(token):
            pos = self.st.add(token)

            if self.checkConstant(token):
                self.pif.add("const", pos)
            else:
                self.pif.add("id", pos)
        else:
            self.errors += "Lexical error: line " + str(pos + 1) + " -> " + str(token) + "\n"

    def checkConstant(self, token):
        constant_pattern = r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$'
        return (re.match(constant_pattern, token)) is not None

    def checkIdentifier(self, token):
        return re.match(r'^#.*\$$', token) is not None

    def writeToFile(self, content, filename):
        file = open(filename, "w")
        file.write(content)
        file.close()
