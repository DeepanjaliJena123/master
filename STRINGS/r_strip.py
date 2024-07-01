#exa1:
# string = "geekssss"
# print(string.rstrip('s'))        #geek

#exa2: remove from right side
# string = "geeks for geeks"
# print(string.rstrip("ske"))           #geeks for g

#exa3:
string = "geeks for geeks"

# string doesn't have trailing 'e' or 'k'
# thus the rstrip() method didn't update the string
print(string.rstrip('ek'))