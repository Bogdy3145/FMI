from Parser import LL1Parser
from grammar2 import RegularGrammar
#
# g = Grammar.from_file('lftc_lab6/g1.txt')
# print(g)
# print(g.get_nonterminal_productions('S'))
# print(g.is_cfg())


#g = Grammar.from_file('g1.txt')
# print(g)
# print(g.get_nonterminal_productions('S'))
# print(g.is_cfg())

g = RegularGrammar('g22.txt')
parser = LL1Parser(g)
# parser.computeFirst()
# for key in parser.first.keys():
#     print(key, " ", parser.first[key])
#
# print('\n\n\n')
# parser.compute_follow()
# for key in parser.follow.keys():
#     print(key, " ", parser.follow[key])

#parser.parseSequence("what")
parser.print_table()

#
#
# g = Grammar.from_file('lftc_lab6/g3.txt')
# print(g)
# print(g.get_nonterminal_productions('A'))
# print(g.is_cfg())