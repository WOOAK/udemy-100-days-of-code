import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction_list = ["encode","decode"]
print(art.logo)

def caeser(direction,text,shift):

   
    if direction not in direction_list:
        print("Invalid direction!")
        return
        
    length = len(alphabet)
    result = ''
    
    if direction == "decode":
        shift *= -1
    
    for i in text:
        if i in alphabet:
            pos = alphabet.index(i)
            pos += shift
    
            if direction == "encode":
                while pos >= length:
                    pos -= length
            else:
                while pos <= 0:
                    pos += length
        
            result += alphabet[pos]
        else:
            result += i
     
    print(f"Here's the {direction}d result: {result}")


#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"
#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a new function that calls itself if they type 'yes'. 



#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Hint: Think about how you can use the modulus (%).

end = False

while end == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(direction, text, shift)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == 'no':
        end = True
        print("Goodbye.")