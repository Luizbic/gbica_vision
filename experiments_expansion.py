from modules.expansion import gbicaExpansion

expansion = gbicaExpansion()

text = 'a handsome man'

for i in range(64):
    print(expansion(text, seed=i))
