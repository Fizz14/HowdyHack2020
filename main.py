import Operation1 as op1
import Operation2 as op2
import Operation3 as op3

codeprocess = []                #process of encrypting
phrase = "secretstuff"          #phrase for encrypting

'''
The following three functions, exe_method(), exe_encrypt(), and exe_decrypt() were adapted from the console app. 

The first takes one parameter, which is an encryption method according to the syntax operation:parameter,parameter;operation:parameter,parameter....
e.g. "1:-3,2;3:3,5;2:-15;"

it sets codeprocess, a global variable.

The second are given a parameter of a message to encrypt or decrypt and set/return phrase based on that. 

I will try to link them to the gui tonight, but if I fail, I actually don't think there's too much more to do. (I hope)
'''


def exe_method(command = "1:-3,2;3:3,5;2:-15;"):
    print(command)
    codeprocess.clear()
    #cut command into parts
    commands = command.split(';')  
    commands.pop()  #I don't know why, but it always has an extra element
    print(commands)
    for x in commands:
        parts = x.split(':')
        print(parts)
        try:
            testnum = int(parts[0])

        except ValueError:
            print("ERROR")

        operation = int(parts[0])
        print("Operation:", operation)

        parameters = parts[1].split(',')
        print("Parameters:", parameters)
        
        nloopindex = 0
        for x in parameters:
            parameters[nloopindex] = int(x)
            nloopindex = nloopindex + 1

        if(operation > 3):
            print("ERROR")  
        
    
        try:  #this is done to make sure all parameters are integers
            for x in parameters:
                testnum = int(x)

        except ValueError:
            print("ERROR")
            continue
    
        codeprocess.append(operation) 
        codeprocess.append(parameters) 
    
    print(codeprocess)
    return codeprocess
    

def exe_encrypt(param_phrase = "A sentence"):
    phrase = param_phrase
    print(phrase)
    codeprocess_copy = codeprocess[:]
    while (len(codeprocess_copy) > 0):
        current_operation = codeprocess_copy.pop(0)
        current_parameters = codeprocess_copy.pop(0)

        loopindex = 0
        for x in current_parameters:
            current_parameters[loopindex] = int(x)
            loopindex = loopindex + 1
      
        #Make the array of parameters length 3 so none of the functions crash  
        while (len(current_parameters) < 3):
            current_parameters.append(-1)

        if(current_operation == 1):
            phrase = op1.encryption_1(phrase, current_parameters[0], current_parameters[1])
            print("encr1")
      
        if(current_operation == 2):
            phrase = op2.encryption_2(phrase, current_parameters[0])
    
        if(current_operation == 3):
            phrase = op3.encryption_3(phrase, current_parameters[0], current_parameters[1])
    
    return phrase


def exe_decrypt(param_phrase = "A sentence"):
    phrase = param_phrase
    print(phrase)
    codeprocess_copy = codeprocess[:]
    print(codeprocess_copy)
    while (len(codeprocess_copy) > 0):
        current_parameters = codeprocess_copy.pop(-1)
        current_operation = codeprocess_copy.pop(-1)
    
        while (len(current_parameters) < 3):
            current_parameters.append(-1)

        if(current_operation == 1):
            phrase = op1.decryption_1(phrase, current_parameters[0], current_parameters[1])
            print("encr2")
            print(phrase)

        if(current_operation == 2):
            phrase = op2.decryption_2(phrase, current_parameters[0])
    
        if(current_operation == 3):
            phrase = op3.decryption_3(phrase, current_parameters[0], current_parameters[1])

    return phrase