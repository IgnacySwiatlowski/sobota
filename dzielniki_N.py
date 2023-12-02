from tkinter import *
 
# method that performs the action
def action ():
    
    # retrieve the value of the edit control
    N = int (entryNumber1.get ())
    lblDivisors ['text'] = 'The  divisors  of  N    :    '
    
    # find the divisors s of n by going through all the integers from 1 to n
    for i in range (1, N + 1):
        if ( N%i == 0 ):
            lblDivisors ['text'] = lblDivisors ['text'] + "   " + str(i) + "   "


# Creation of the main window
fen = Tk ()
fen.geometry ("400x175")


# input field for the integer N with the associated label
lblnumber1 = Label (fen, text = "Enter the value of N")
lblnumber1.place (x = 10, y = 20)
entryNumber1 = Entry (fen)
entryNumber1.place (x = 200, y = 20)


# Label which gets the result
lblDivisors = Label (fen, text = "The divisors of N : ")
lblDivisors.place (x = 10, y = 50)


# validation button
Validate = Button (fen, text = "Validate", width = 20, command = action)
Validate.place (x = 200, y = 90)


fen.mainloop ()