#Regular expression use: verify string match a pattern, subsitituation in text(find and replace)
"""import re
pattern = r"eggs"

if re.match(pattern,"eggseggseggsb"):
    print("Match found")
else:
    print("No match found")"""

#Search and find all--------------------------------------
"""import re
pattern = r"eg"
#for searching the string
if re.search(pattern, "baconeggseggseggsbe"):
    print("Found the instance")
else:
    print("Instance not found")
    
#for finding the number of instance
if re.findall(pattern, "baconeggseggseggsbe"):
    print("Found the instance")
else:
    print("Instance not found")

#alternate way
print(re.findall(pattern, "baconeggseggseggsbe"))"""

#find and replace-----------------------------------------------------
#sub is used for replacing the name in the string

"""import re
string = "My name is Jhon, Hi I am Jhon"
pattern = r"Jhon"
newstr = re.sub(pattern,"Girish",string)
print(newstr)"""

#the dot metacharacter------------------------------------------------
#it allows regular expression to be more efficent

"""import re
pattern = r"gr..y" #. represent that you could have any charcter there
if re.search(pattern,"greey"):
    print("Match found")
else:
    print("Match not found")"""

#Craret & dollar metacharacter-------------------------------------------
"""import re
pattern = r"^gr.y$" #^starting point, $ending point
if re.match(pattern,"grey"):
    print("match found")
else:
    print("Match not found")"""

#charcter class------------------------------------------------------------

#way to match one of the specific content

"""import re
pattern = r"[A-Z][A-Z][0-9]" #represtation of pattern
if re.match(pattern,"AX9"):
    print("match found")
else:
    print("Match not found")"""

#Star meta----------------------------------------------------------------
"""import re
pattern = r"eggs(bacon)*" #() content will have 0 or more instance but eggs should be there
if re.match(pattern,"eggsbaconbacon"):
    print("match found")
else:
    print("Match not found")"""

#group----------------------------------------------------------------------
"""import re
pattern = r"bread(eggs)*bread"
if re.match(pattern,"breadeggsbreadeggs"):
    print("match found")
else:
    print("Match not found")"""