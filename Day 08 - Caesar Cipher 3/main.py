alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
direction_list = ["encode","decode"]
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caeser(direction,text,shift):
    if direction not in direction_list:
        print("Invalid direction!")
        return
    length = len(alphabet)
    result = ''
    
    if direction == "decode":
        shift *= -1
    
    for i in text:
        pos = alphabet.index(i)
        pos += shift
    
        if direction == "encode":
            while pos >= length:
                pos -= length
        else:
            while pos <= 0:
                pos += length
        
        result += alphabet[pos]
    print(result)
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caeser(direction,text,shift)