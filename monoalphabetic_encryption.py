def encrypt(text):
    result=""  #empty string
    for i in range(len(text)):
        char=text[i]
        if(ord(char)==32):
            result=result+chr(35)
        elif(char.isupper()):  #if the text[i] is in upper case
            result=result+chr((ord(char)+13-65)%26+65)
        else: #if it is lower
            result=result+chr((ord(char)+13-97)%26+97)
    return result

word=str(input("enter the word:"))

print("Encoded word in Caeser cipher is: ",encrypt(word))

'''
----------OUTPUT----------
enter the word:Cipher is an Algorithm
Encoded word in Caeser cipher is: Pvcure#vf#na#Nytbevguz
>>> 
'''
