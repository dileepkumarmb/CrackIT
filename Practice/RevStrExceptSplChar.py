#dileep@gmail.com
import re

def validate_ph(phn):
    pat = "\d{10}"
    if(re.search(pat,phn)):
        print("valid phone")
    else:
        print("Invalid phone")
validate_ph("1234578090")

def validate(email):
    pat = "\w{3,4}@\w+\.(com|in)"
    pat = re.compile(pat)
    obj1 = re.match(pat, email)
    print("Match pattern is:", obj1)
    if obj1:
        print("Perfet email")
    else:
        print("Invalid email")

validate("dile@gamil.in")



print("################# New Program : reverse string except special char################")
strSample = 'abc/defgh$ij'
# convert string into list
listSample = list(strSample)

i = 0
j = len(listSample) - 1

while i < j:
    if not listSample[i].isalpha():
        i += 1
    elif not listSample[j].isalpha():
        j -= 1
    else:
        # swap the element in the list ,if both elements are alphabets
        listSample[i], listSample[j] = listSample[j], listSample[i]
        i += 1
        j -= 1

# convert list into string, by concatinating each element in the list
strOut = ''.join(listSample)
print(strOut)