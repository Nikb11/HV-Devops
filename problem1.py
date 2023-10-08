word=input("Enter a word")

b=set()

for char in word:
    if word not in b:
        b.add(char)
print ("unique:".join(b))        