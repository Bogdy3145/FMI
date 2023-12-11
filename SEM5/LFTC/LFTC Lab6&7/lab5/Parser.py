import copy


class LL1Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.first = {}
        self.follow = {}
        for terminal in self.grammar.E:
            self.first[terminal] = terminal
        for non_terminal in self.grammar.N:
            self.follow[non_terminal] = []

        self.table = {}
        for terminal in self.grammar.E:
            if terminal != 'epsilon':
                self.table[terminal] = []
        self.table['$'] = []
        for non_terminal in self.grammar.N:
            self.table[non_terminal] = []

    def computeFirst(self):
        for key in self.grammar.P.keys():
            if key not in self.first.keys():
                self.first[key] = []
            for elem in self.grammar.P[key]:
                if elem in self.grammar.E or elem == "epsilon":
                    self.first[key].append(elem)
                elif elem[0] in self.grammar.E:
                    self.first[key].append(elem[0])

        grammar = self.grammar
        while True:
            # currentFirst = dict(self.first)
            currentFirst = copy.deepcopy(self.first)
            for key in self.grammar.P.keys():
                for elem in grammar.P[key]:
                    if elem[0] in self.grammar.N and len(self.first[elem[0]]) == 1 and "epsilon" in self.first[elem[0]]:
                        for char in elem:
                            if 'epsilon' in self.first[char] and len(self.first[char]) == 1:
                                continue
                            else:
                                if char in self.grammar.N and len(self.first[char]) != 0:
                                    self.first[key] = list(set(self.first[key] + self.first[char]))
                                    if "epsilon" in self.first[key]:
                                        self.first[key].remove("epsilon")
                                    break
                                elif char in self.grammar.E:
                                    self.first[key] += self.first[char]
                                    break
                    elif elem[0] in self.grammar.N and len(self.first[elem[0]]) != 0:
                        self.first[key] = list(set(self.first[key] + self.first[elem[0]]))
                        if "epsilon" in self.first[key]:
                            self.first[key].remove("epsilon")
                        break

            if currentFirst == self.first:
                break

    def compute_follow(self):
        self.follow[self.grammar.startSymbol].append("epsilon")

        while True:
            previousFollow = copy.deepcopy(self.follow)
            for nonterminal in self.grammar.N:
                for key in self.grammar.P:
                    for result in self.grammar.P[key]:
                        if nonterminal in result:
                            for i in range(len(result)):
                                firstForNextSymbol = []

                                if result[i] == nonterminal:
                                    if len(result) > i + 1:
                                        firstForNextSymbol = self.first[result[i + 1]]
                                    else:
                                        self.follow[nonterminal] = list(
                                            set(self.follow[nonterminal] + previousFollow[key]))

                                    if "epsilon" in firstForNextSymbol and len(result) > i + 1:
                                        self.follow[nonterminal] = list(set(previousFollow[nonterminal] +
                                                                            list(firstForNextSymbol)))
                                    elif len(result) > i + 1:
                                        self.follow[nonterminal] = list(set(previousFollow[nonterminal] +
                                                                            list(firstForNextSymbol)))

                                    if "epsilon" in firstForNextSymbol:
                                        self.follow[nonterminal] = list(
                                            set(self.follow[nonterminal] + previousFollow[key]))

            if previousFollow == self.follow:
                break


    def parsing_table(self):
        #self.computeFirst()
        #self.compute_follow()
        for i in self.grammar.E:
            self.table[i] = [i, "POP", 0]
        index=0
        for element in self.first.keys():
            if element in self.grammar.N:
                production = self.grammar.P[element]
                for prod in production:
                    if "epsilon" in prod:
                        index+=1
                        for elem_follow in self.follow[element]:
                            self.table[element].append(
                                [elem_follow, 'epsilon', index])
                    else:
                        index+=1
                        char = prod[0]
                        if char in self.grammar.E:
                            self.table[element].append(
                                [char, prod, index])

                        else:
                            for elem in self.first[char]:
                                self.table[element].append(
                                    [elem, production[0], index])
