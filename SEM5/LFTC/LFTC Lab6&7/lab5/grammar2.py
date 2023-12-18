from operator import indexOf

class RegularGrammar:
    def __init__(self, filename):
        self.N = []
        self.E = []
        self.P = {}
        self.startSymbol = ''
        self.numberedProduction = {}
        self.getGrammarFromFile(filename)

    def getGrammarFromFile(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        indice = 0

        for line in lines:
            elements = []
            line = line.replace("\n", '')
            position = indexOf(line, "=")
            elements.append(line[:position])
            elements.append(line[position + 1:])

            if elements[0] == 'N':
                self.N = elements[1].split(" ")
            elif elements[0] == 'E':
                self.E = elements[1].split(" ")
            elif elements[0] == 'P':
                indice += 1
                elements[1].replace(" ", "")
                prod = elements[1].split("->")
                self.numberedProduction[prod[1]] = indice
                if prod[0] in self.P.keys():
                    self.P[prod[0]].append(prod[1])
                else:
                    self.P[prod[0]] = [prod[1]]
            elif elements[0] == 'S':
                self.startSymbol = elements[1]
        file.close()

        if not self.isCFG():
            print("This is not a CFG")
            return



    def getAllNonterminals(self):
        stringBuilder = "N = {"

        for state in self.N:
            stringBuilder += state
            stringBuilder += ', '

        stringBuilder = stringBuilder[0:-2] + "}"

        return stringBuilder

    def getAllTerminals(self):
        stringBuilder = "Σ = {"

        for elem in self.E:
            stringBuilder += elem
            stringBuilder += ', '

        stringBuilder = stringBuilder[0:-2] + "}"

        return stringBuilder

    def getAllProductions(self):
        stringBuilder = ""

        for key in self.P.keys():
            stringBuilder = stringBuilder + key + ' -> '
            if type(self.P[key]) == list:
                for elem in self.P[key]:
                    stringBuilder = stringBuilder + elem + "|"
            stringBuilder = stringBuilder[:-1]
            stringBuilder += '\n'

        return stringBuilder

    def getStartSymbol(self):
        return "S = " + self.startSymbol

    def isCFG(self):
        list = []
        for key in self.P.keys():
            for terminal in self.P[key]:
                if terminal in list and key in self.N:
                    print(terminal, " ", key)
                    list.append(terminal)
                    return False


        return True
