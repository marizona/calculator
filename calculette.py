 #lambda declare anonymous function, asssign a function to a button, we could not pass any parameter if not anonymous function
#[-1]last button added to our list, the command must be a function, in order to give parameter to function we need to make a wrapper funtion, lambda function that wraps the original function.
#this lambda takes parameter (x), this lambda function will take the button itself as a parameter. this function will then call the self.change_text function and it will give it the text of the button that it took as a parameter
#for each button, we need to assign function when we press it, -1 the last element of the list, we are refering to the komand of the last button of our list.
from tkinter import *

WIDTH = 600
HEIGHT = 800

root = Tk()  # calling tk function to create a basic window

class Calculator : # classes capital letter declare class to declare window
    def __init__(self, root, width, height):  # constructor
        self.root=root
        self.width=width
        self.height=height
        
        self.root.geometry(f"{self.width}x{self.height}")#we are converting width and height to string, we are modifying the size of the window
        self.root.resizable(False, False)#we can't resize
        
        self.display=Frame(self.root,bg="grey")#spliting the window in multiple parts, we need to display it
        self.display.place(relwidth=1, relheight=0.2)#we are placing our new frame, same width as root window, 20% of the height of the root window, rel = parent object (root)
        self.button_frame=Frame(self.root, bg="white")
        self.button_frame.place(relwidth=1, relheight=0.8, rely=0.2)#the starting point will be 20 % = the end of the display frame
        
        self.output=Label(self.display, text="0", bg= "grey", font=("Arial", 25))#creating text area, font()= toople, you cant change the value inmutable
        self.output.pack(side=RIGHT, padx=15 )#pack=vertically center the label. vertically align right side, PADX= space between border of window, displaying display
        self.setup_buttons()
    def setup_buttons(self):#buttons
         buttons=["(", ")", "C", "del", "pi", "x^y", "log", "sqrt", "mod",
         "e", "7", "8", "9", ":", "!", "4", "5", "6", "x", "sin", "1", "2", "3", "-", "cos", ",", "0", "=", "+", "tan"]  #list of buttons
         button_list=[]
         for i,button in enumerate(buttons):#get index and value
            button_list.append(Button(self.button_frame, text=button, font=("Arial", 25), bg="white"))#for each button , we are adding a physical button
            button_list[-1]["command"]=lambda x=button_list[-1] :  self.change_text(x["text"])  
                                                                            
            button_list[-1].place(relwidth=0.2, relheight=0.1666, relx=i%5*0.2, rely=i//5*0.1666)#5 buttons per row, each button takes 20% of the space, 6 rows in total, the mod operation return the reminder of the division i over i, relx= determine position of the button, they must be align
        
    def change_text(self, text): #text of button we just pressed, we need to update display
        if text == "=":
            self.output["text"] = str(self.equal())#press equal, it will calculate the result of what we have written and display it
        elif text == "C":
            self.output["text"]=""       #erase button
        else:
            self.output["text"]+= text#text of our self output label

    def convert_expression(self, s):  #converting the regurlar string of text in a list, splitting the string into numbers and operations    # "23 + 4 : (4+2)"   [23, +, 4, :, [4,+,2]]
        op = [] #result that we return at the end
        operations = ["+", "-", ":", "x"]
        start = 0 #keep track of what number we were on. 
        for i, e in enumerate(s): #looping with index through our string in the display e= character
            if e == s[-1]: #s=text if the character is the last character of the text, we are going to add at the end of the list, op = empty list store our converting string
                op.append(s[start:])
            if e in operations: #if we meet an operation, we are going to add the first number to our list
                op.append(s[start:i]) #
                op.append(e)
                start = i + 1#get the correct next number
        return op
        
    def equal(self): #calling the convert expression method, calculate the result from the list
        expression = self.convert_expression(self.output["text"]) #store the result of the converted string inside expression
        order = ["x:", "+-"] #list of operation
        while len(expression) > 1: #while we have 2 or more numbers, we haven't gotten to the result and we enter the loop
            for operationset in order: #order of the operation, operation set is the first element of the list, operation loops through the elements of the list
                for operation in operationset: #loop through each character
                    for i, n in enumerate(expression): #loop through our converted list with index
                        if n == operation: #n is the character we are looping , if we met an operation sign then it stores the previous value and the next value, 
                            n1 = expression[i-1] 
                            n2 = expression[i+1]
                            if n == "x": #which operation it is , if it is X we multiply ... etc
                                result =float(expression[i-1]) * float(expression[i+1])   #calculating the result, converting each number to float because we have been working with strings   
                            elif n == ":":
                                result = float(expression[i-1]) / float(expression[i+1])
                            elif n == "+":
                                result = float(expression[i-1]) + float(expression[i+1])
                            else:
                                result = float(expression[i-1]) - float(expression[i+1])
                            
                            expression.remove(n)# we remove the operator sign and we remove the previous and the next value
                            expression.remove(n1)
                            expression.remove(n2)
                            expression.insert(i-1, result) #then we insert in the list the result of the operation
                   
        return expression[0]#return the value inside the list
        
window=Calculator(root, WIDTH, HEIGHT) #create object of this class to modify window
root.mainloop()  # start the interface/ at the end always, because we start the interface at the end