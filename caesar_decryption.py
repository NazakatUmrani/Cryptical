def decrypt(text,s):
    s=26-s 
        
    result=""  #empty string
    for i in range(len(text)):
        char=text[i]
        if(ord(char)==35): #if the text[i] is a #
            result=result+chr(32) # replace it with space ' '
        elif(char.isupper()):  #if the text[i] is in upper case
            result=result+chr((ord(char)+s-65)%26+65)
        else: #if it is lower
            result=result+chr((ord(char)+s-97)%26+97)
    return result


word=str(input("enter the word:"))
d=int(input("Enter the key: "))

print("Encoded word in Caeser cipher is: ",decrypt(word,d))

'''
----------OUTPUT----------
enter the word:klwkhuhpbqdphlvdekludp
Enter the key: 3
Encoded word in Caeser cipher is:  hitheremynameisabhiram
>>> 
'''
