#CREATOR: Jessica Napolitano
#FUNCTION: This program encodes and decodes messages inputed by user.
#It can also encode and decode files and output them to a specified file.


from graphics import*
import os.path


#encoding for a message
#asc stands for the ascii number associated with that character.

def encode(key,msge):

   #boolen to tell if the user inputted information into the input box
    haveKey = False
    
    if key.getText().isdigit() != True:
        return haveKey

    haveKey=True 
    key=eval(key.getText())
    msge=msge.getText()
    encoded= ''
    for ch in msge:
        asc=ord(ch)
        if asc in range(65,91):
                asc=asc+key
                if asc not in range(65,91):
                    asc=((asc-65)%26)+65
        elif asc in range(97,123):
            asc=asc+key
            if asc not in range(97,123):
                asc=((asc-97)%26)+97
        else:
            asc=asc
            
        encoded=encoded+chr(asc) 

    return encoded

#____________________________________________________________________

#decoding for a message
#asci also stands for the ascii number associated with that character
def decode(key,msge):
    
    #boolen to tell if the user inputted information into the input box
    haveKey = False
    
    if key.getText().isdigit() != True:
        return haveKey
    
    key=eval(key.getText())
    msge=msge.getText()
    decoded=''
    for ch in msge:
        asci=ord(ch)
        if asci in range(65,91):
            asci=asci-key
            if asci not in range(65,91):
                asci=((asci-65)%26)+65
        elif asci in range(97,123):
            asci=asci-key
            if asci not in range(97,123):
                asci=((asci-97)%26)+97
        else:
            asci=asci
            
        decoded=decoded+chr(asci)
        
    return decoded


#____________________________________________________________________

#encoding for a file
def encode_file(key,inFile):

    #boolen to tell if the user inputted information into the input box
    haveKey = False
    
    if key.getText().isdigit() != True:
        return haveKey

    #tests to make sure that the file inputted exists in the current directory 
    inFile=inFile.getText()
    fileExist = os.path.isfile(inFile)

    if fileExist==True:  
        inFile=open(inFile,'r',encoding="utf-8")
        all_Conts=inFile.read()
        key=eval(key.getText())
        encoded_file= ''
        for ch in all_Conts:
            asc_file=ord(ch)
            if asc_file in range(65,91):
                asc_file=asc_file+key
                if asc_file not in range(65,91):
                    asc_file=((asc_file-65)%26)+65
            elif asc_file in range(97,123):
                asc_file=asc_file+key
                if asc_file not in range(97,123):
                    asc_file=((asc_file-97)%26)+97
            else:
                asc_file=asc_file
                
            encoded_file=encoded_file+chr(asc_file)
            inFile.close()
        return encoded_file

    return -1
#__________________________________________________________________

#decoding for a file
def decode_file(key,inFile):
    
   #boolen to tell if the user inputted information into the input box
    haveKey = False
    
    if key.getText().isdigit() != True:
        return haveKey
    
    key=eval(key.getText())

    #tests to make sure that the file inputted exists in the current directory 
    inFile=inFile.getText()
    fileExist = os.path.isfile(inFile)

    if fileExist==True:  
    
        inFile=open(inFile,'r',encoding="utf-8")
        all_Conts=inFile.read()
        decoded_file=''
        for ch in all_Conts:
            asci_file=ord(ch)
            if asci_file in range(65,91):
                asci_file=asci_file-key
                if asci_file not in range(65,91):
                    asci_file=((asci_file-65)%26)+65
            elif asci_file in range(97,123):
                asci_file=asci_file-key
                if asci_file not in range(97,123):
                    asci_file=((asci_file-97)%26)+97
            else:
                asci_file=asci_file
                
            decoded_file=decoded_file+chr(asci_file)
            inFile.close()
            
        return decoded_file

    return -1
#__________________________________________________________________



"""THIS IS THE MAIN FUNCTION. All the other functions culminate to this one.
It sets up the window and buttons and then puts the functionality and logic
into the application """



#setting up window, buttons, and output 
def GUI():

    
    #set up splash screen 
    
    win=GraphWin('Encoder/Decoder',1000,500)
    
    background = Rectangle(Point(0, 0), Point(1000, 500))
            
    background.setFill('purple')
    
    background.draw(win)


    sticker = Image(Point(500,70),'caesarsticker.gif')
    
    sticker.draw(win)
        

    instructions = Text(Point(500,250),"""CAESAR CIPHER

   The Caesar Cipher was developed back in the time of Caesar. It is one of the simplest and widely known encryption
   techniques. There are two main types of ciphers, transition and substitution. The Caesar Cipher is a
   substituion cipher. This means that each letter in the plaintext (the intelligable, original text) is substituted
   with a letter some fixed position down in the alphabet. The fixed position down in the alphabet is determined
   by a value called the key. Once the key is applied, the resulting output is called the ciphertext. When going
   from plaintext to ciphertext that is called encoding and going the other way is called decoding. Once the plaintext
   is encoded, only people who know the key are able to decode it.

   In this application the user has the ability to encode and decode a message that they can type into the input
   box. The user also has the ability to encode or decode a file which they place in this same directory. """)

    instructions.setFill('gold')

    instructions.setSize(13)

    instructions.setStyle('bold')

    instructions.draw(win)

    continuemsg = Text(Point(500,400),"Click anywhere to continue to the application")

    continuemsg.setFill('gold')

    continuemsg.setSize(20)

    continuemsg.draw(win)

    pt = win.getMouse()

    win.close()

    
    #set up application

    win=GraphWin('Encoder/Decoder',400,500)
    
    win.setCoords(0.0,0.0,3.0,4.0)

    background = Image(Point(1.5,2),'background.gif')
            
    background.draw(win)


    #set text for inputs and outputs
    messagetxt = Text(Point(1,2.8), 'Message:')
    messagetxt.setFill('red')
    messagetxt.setStyle('bold')
    messagetxt.draw(win)
    cipherkeytxt = Text(Point(1,2.4), 'Cipher key:')
    cipherkeytxt.setFill('red')
    cipherkeytxt.setStyle('bold')
    cipherkeytxt.draw(win)
    outputtxt = Text(Point(1.4,1), 'Output Message:')
    outputtxt.setFill('red')
    outputtxt.setStyle('bold')
    outputtxt.draw(win)
    infiletxt = Text(Point(.5,2),'inFile:')
    infiletxt.setFill('red')
    infiletxt.setStyle('bold')
    infiletxt.draw(win)
    outfiletxt = Text(Point(1.8,2),'outFile:')
    outfiletxt.setFill('red')
    outfiletxt.setStyle('bold')
    outfiletxt.draw(win)
    
    #makes msge entry field
    msge=Entry(Point(2,2.8),20)
    msge.setText('Enter message here')
    msge.setFill('gold')
    msge.draw(win)

    #makes cipherkey entry field
    key=Entry(Point(2,2.4),10)
    key.setText('Enter key')
    key.setFill('gold')
    key.draw(win)

    #makes output field 
    output=Entry(Point(1.4,.8),35)
    output.setText('Message')
    output.setFill('gold')
    output.draw(win)

    #makes inFile name Entry field 
    inFile=Entry(Point(1.1,2),10)
    inFile.setText('File name.txt')
    inFile.setFill('gold')
    inFile.draw(win)

    #makes outFile name Entry field 
    outFile=Entry(Point(2.4,2),10)
    outFile.setText('File name.txt')
    outFile.setFill('gold')
    outFile.draw(win)

    #encode_msge button
    encode_msge = Rectangle(Point(1.4,1.8),Point(.5,1.6))
    encode_msge.setFill('purple')
    encode_msge.draw(win)
    #decode_msge button
    decode_msge = Rectangle(Point(1.5,1.8),Point(2.5,1.6))
    decode_msge.setFill('purple')
    decode_msge.draw(win)
    #encode_file button
    encode_fileB = Rectangle(Point(1.4,1.5),Point(.5,1.3))
    encode_fileB.setFill('purple')
    encode_fileB.draw(win)
    #decode_file button
    decode_fileB = Rectangle(Point(1.5,1.3),Point(2.5,1.5))
    decode_fileB.setFill('purple')
    decode_fileB.draw(win)
    #exit button
    exitB = Rectangle(Point(1.2,.1),Point(1.8,.3))
    exitB.setFill('purple')
    exitB.draw(win)

    #sets text for buttons 
    button_encode4msge=Text(Point(1,1.7),'Encode4Msge')
    button_decode4msge=Text(Point(2,1.7),'Decode4Msge')
    button_encode4file=Text(Point(1,1.4),'Encode4File')
    button_decode4file=Text(Point(2,1.4),'Decode4File')
    button_exit=Text(Point(1.5,.2),'Exit')

    #draws text for buttons
    button_encode4msge.draw(win)
    button_decode4msge.draw(win)
    button_encode4file.draw(win)
    button_decode4file.draw(win)
    button_exit.draw(win)
    
 

    #waits for user to click
    pt=win.getMouse()     
        
    #while the user is not clicking on the exit button
    #   if they click the encode message button it will encode it
    #   else if they click the decode message button it will decode it
    #   else if they click the encode file button it will encode it to a specific file
    #   else if they click the decode file button it willl decode it to a specific file
    #   After it exectute one of these it then waits for the user to click again so that
    #   the user can do multiple tasks all in one sitting
    #   if they click the exit button it will close.
    
    while not ((pt.getX()>=1 and pt.getX()<=2) and\
      (pt.getY()>=0 and pt.getY()<=.3)): #exit button
        
        if (pt.getX()>=.5 and pt.getX()<=1.4) and\
            (pt.getY()>=1.6 and pt.getY()<=1.8): #encode message button
            encoded=encode(key,msge)
            if encoded == 0:
                output.setText("ERR: No key inputted")
            else:
                output.setText(encoded)
            
        elif ((pt.getX()>=1.5 and pt.getX()<=2.5) and\
            (pt.getY()>=1.6 and pt.getY()<=1.8)): #decode message button 
            decoded=decode(key,msge)
            if decoded == 0:
                output.setText("ERR: No key inputted")
            else:
                output.setText(decoded)
            
        elif ((pt.getX()>=.5 and pt.getX()<=1.4) and\
            (pt.getY()>=1.3 and pt.getY()<=1.5)): #encode file button 
            encoded_file=encode_file(key,inFile)

            #if no key was inputted
            if encoded_file == 0:
                output.setText("ERR: Key not valid")

            #if the file name is invalid
            elif encoded_file == -1:
                output.setText("ERR: File does not exist")
                
            else:                
                filename=outFile.getText()
                filename=open(filename,'w',encoding="utf-8")
                print(encoded_file,file=filename)
                filename.close()
                output.setText("LOG: Your encoded file has been created")
            
        elif ((pt.getX()>=1.5 and pt.getX()<=2.5) and\
            (pt.getY()>=1.3 and pt.getY()<=1.5)): #decode file button
            decoded_file=decode_file(key,inFile)

            #if no key was inputted
            if decoded_file == 0:
                output.setText("ERR: Key not valid")

            #if the file name is invalid 
            elif decoded_file == -1:
                output.setText("ERR: File does not exist")
                
            else:                
                filename=outFile.getText()
                filename=open(filename,'w',encoding="utf-8")
                print(decoded_file,file=filename)
                filename.close()
                output.setText("LOG: Your decoded file has been created")
            
            
            
        pt=win.getMouse()

            
    win.close()
            
    



GUI()



    






    

