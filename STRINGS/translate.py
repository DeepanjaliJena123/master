#returns a string that is a modified string of givens string according to given translation mappings.

##The translation table is defined as a dictionary where keys are ASCII values of characters to be replaced, and values are their replacements.

#exa1:
# translation = {103: None, 101: None, 101: None}
# string="geeks"
# print(string.translate(translation))

#exa2:
# table = { 119 : 103, 121 : 102, 117 : None }
# trg = "weeksyourweeks"
# print(trg.translate(table))
