from grammar import Grammar

#
# g = Grammar.from_file('lftc_lab6/g1.txt')
# print(g)
# print(g.get_nonterminal_productions('S'))
# print(g.is_cfg())


g = Grammar.from_file('g2.txt')
print(g)
print(g.get_nonterminal_productions('program'))
print(g.is_cfg())
#
#
# g = Grammar.from_file('lftc_lab6/g3.txt')
# print(g)
# print(g.get_nonterminal_productions('A'))
# print(g.is_cfg())