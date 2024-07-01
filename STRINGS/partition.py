#The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
#exa1:
# s="i love for geek for geeks"
# print(s.partition("for"))

#exa2:
# string = "light attracts bug"
# print(string.partition("attracts"))

#exa3:
# str = "gold is heavy"
# print(str.partition("is"))     #('gold ', 'is', ' heavy')

#exa4: its will partition  1st occurance

# string = "I am happy, I am proud"
# print(string.partition("am"))        #('I ', 'am', ' happy, I am proud')

#exa5: "are" not found,so it will give 2spaces
# str="geek for geek"
# print(str.partition("str"))        #('geek for geek', '', '')

#exa6:
# url = "https://www.example.com/index.html"
# r=url.partition("//")
# print(r)    #('https:', '//', 'www.example.com/index.html')
# r=r[2].partition('/')
# print(r[0])

#exa7:
# sentence = "The quick Brown fox jumps over the lazy Fox."
# result = sentence.partition("fox")
# print(result)
# result = sentence.partition("Fox")
# print(result)












