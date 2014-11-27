#decoder_encoder.py
#Jessica Napolitano (jnapolit@conncoll.edu)
#Mar 2, 2014
#This program encodes and decodes messages inputed by user. It can also encode and decode files
#   and output them to a specified file.


from graphics import*

"""DESCRIPTION OF FUNCTIONS PRIOR TO GUI: This gets the key from the entry field and the message, then
produces the proper ascii number that is associated with it
If that number is in the range between 65 and 91 then it is an
upper case letter and thus it adds the key and loops it through
so that if when you add the key it is out of the upper case letter
range it will go back to the beginning of the range rather than going
to different symbols. This is done by utilizing the remainder operation.
the same is done for the lower case. And if in the beginning the ascii number
is not in the range of the upper case letters or the lower case then it is
a punctuation such as ! or ? or even a space, thus my program leaves those charcters
alone and does not encode or decode them. It then takes these new numbers and turns them into characters again.
It does this process to encode both the messages
and the files. They only difference would be for a file it saves the result to a file
rather than outputing it into the output box. For decoding it is basically the same thing
but rather than adding the cipher key it will subtract it."""



#encoding for a message
#asc stands for the ascii number associated with that character.

def encode(key,msge):
    
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

    inFile=inFile.getText()
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
#__________________________________________________________________

#decoding for a file
def decode_file(key,inFile):
    
    key=eval(key.getText())
    inFile=inFile.getText()
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

#__________________________________________________________________

#setting up window, buttons, and output 
def GUI():
    #set up window
    win=GraphWin('Encoder/Decoder',400,500)
    win.setCoords(0.0,0.0,3.0,4.0)

    #set text for inputs and outputs
    Text(Point(1,3), 'Message:').draw(win)
    Text(Point(1,2.4), 'Cipher key:').draw(win)
    Text(Point(1,.8), 'Output:').draw(win)
    Text(Point(.5,2),'inFile:').draw(win)
    Text(Point(1.8,2),'outFile:').draw(win)
    
    #makes msge entry field
    msge=Entry(Point(2,3),20)
    msge.setText('Enter message here')
    msge.draw(win)

    #makes cipherkey entry field
    key=Entry(Point(2,2.4),10)
    key.setText('Enter key')
    key.draw(win)

    #makes output field 
    output=Entry(Point(2,.8),20)
    output.setText('Message')
    output.draw(win)

    #makes inFile name Entry field 
    inFile=Entry(Point(1.1,2),10)
    inFile.setText('File name.txt')
    inFile.draw(win)

    #makes outFile name Entry field 
    outFile=Entry(Point(2.4,2),10)
    outFile.setText('File name.txt')
    outFile.draw(win)

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
    
    #encode_msge button
    Rectangle(Point(1.4,1.8),Point(.5,1.6)).draw(win)
    #decode_msge button
    Rectangle(Point(1.5,1.8),Point(2.5,1.6)).draw(win)
    #encode_file button
    Rectangle(Point(1.4,1.5),Point(.5,1.3)).draw(win)
    #decode_file button
    Rectangle(Point(1.5,1.3),Point(2.5,1.5)).draw(win)
    #exit button
    Rectangle(Point(1,0),Point(2,.3)).draw(win)

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
      (pt.getY()>=0 and pt.getY()<=.3)):
        if (pt.getX()>=.5 and pt.getX()<=1.4) and\
            (pt.getY()>=1.6 and pt.getY()<=1.8):
            encoded=encode(key,msge)
            output.setText(encoded)
        elif ((pt.getX()>=1.5 and pt.getX()<=2.5) and\
            (pt.getY()>=1.6 and pt.getY()<=1.8)):
            decoded=decode(key,msge)
            output.setText(decoded)
        elif ((pt.getX()>=.5 and pt.getX()<=1.4) and\
            (pt.getY()>=1.3 and pt.getY()<=1.5)):
            encoded_file=encode_file(key,inFile)
            filename=outFile.getText()
            filename=open(filename,'w',encoding="utf-8")
            print(encoded_file,file=filename)
            filename.close()
        elif ((pt.getX()>=1.5 and pt.getX()<=2.5) and\
            (pt.getY()>=1.3 and pt.getY()<=1.5)):
            decoded_file=decode_file(key,inFile)
            filename=outFile.getText()
            filename=open(filename,'w',encoding="utf-8")
            print(decoded_file,file=filename)
            filename.close()
            
        pt=win.getMouse()

            
    win.close()
            
    



GUI()



    






    

