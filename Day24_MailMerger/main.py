
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    print(names_list)
    for name in names_list:
        if "\n" in name:
            name = name.replace('\n','')
        filename = name+'.txt'

        with open("./Input/Letters/starting_letter.txt") as letter:
            letter = letter.read()
            letter = letter.replace("[name]", name)
            filepath = "./Output/ReadyToSend/"+filename
            with open(filepath,'w') as output:
                output.write(letter)

