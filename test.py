
print("Enter the word you are looking for: ")
x = input()
K = open('The_Gray_Nun.txt','r')
rd = K.read()
oc = rd.count(x)
print("Number of occurances of the word-and: ", oc)

