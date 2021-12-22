TEXT = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
MORSE = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----']
input_string = input("Please input your string")

character_list = list(input_string.lower())
print(character_list)

output_morse = ''
for character in character_list:
    try:
        pos = TEXT.index(character)
        output_morse = output_morse + MORSE[pos]
    except ValueError:
        output_morse = output_morse + character

print(output_morse)

