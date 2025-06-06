# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

f = open("poem.txt")

c = f.read()
if("Twinkle" in c):
    print("The twinkle is present in c.")

else:
    print("The twinkle is not  present in c.")   

f.close()     