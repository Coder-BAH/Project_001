# Occurrence of each characters

sentence = input("Enter the sentence: ")
dictionary = {}
for item in sentence:
    if item in dictionary:
        dictionary[item] += 1
    else:
        dictionary[item] = 1
        
print ("Occurrence of each characters in the sentence is : "+ str(dictionary))
