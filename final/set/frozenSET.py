# Python Method creates an immutable Set object from an iterable.
# It is a built-in Python function. As it is a set object, therefore, we cannot have duplicate values in the frozenset.

# Example
#
# In this example, we are creating a frozen set with the list in Python.
# frozenset=frozenset(["apple","mango","orrange"])
# print(frozenset)           #frozenset({'apple', 'orrange', 'mango'})


#exa#
frozenset=frozenset(["apple","mango","orrange"])
print("apple" in frozenset)        #True
print("bannana" in frozenset)      #False