*****************************************************************************************
Author : Jessica Napolitano 
Created: 3/02/2014

Modification Date         Name                      Description   
6/7/2014		  Jessica Napoltiano 	    Updated graphics with background

*****************************************************************************************


WHAT TO RUN: 
	
	To run the application run the program decoder_encoder.py. 



DESCRIPTION :

	The general idea of the application is that it gets the key from the entry field and the message, then produces the proper ascii number that is associated with it.
If that number is in the range between 65 and 91 then it is an upper case letter and thus it adds the key and loops it through so that if when you add the key
it is out of the upper case letter range it will go back to the beginning of the range rather than going to different symbols. This is done by utilizing the 
remainder operation. The same is done for the lower case. And if in the beginning the ascii number is not in the range of the upper case letters or the lower 
case then it is a punctuation such as ! or ? or even a space, thus my program leaves those charcters alone and does not encode or decode them. It then takes 
these new numbers and turns them into characters again. It does this process to encode both the messages and the files. They only difference would be for a 
file it saves the result to a file rather than outputing it into the output box. For decoding it is basically the same thing but rather than adding the cipher 
key it will subtract it.
 


WAYS TO IMPROVE: 
	
	I am hoping to added the option to encode using other ciphers such as the Playfair cipher or the Pigpen cipher. In addition I would love to also include 
the feature of email so that the user can send encoded messages via email as well as decode recieved emails. 
