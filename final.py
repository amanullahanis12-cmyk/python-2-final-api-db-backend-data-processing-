"""
* Name         : Limitted .Txt Creator
* Author       : Amanullah Anis
* Created      : 5/5/2025
* Course       : CIS189
* IDE          : Visual Studio
* Description  : Asks user for summary of book with book information and then makes a .txt file if summary is valid.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.       
"""
#Gets tkinter module and imports methods from Functions file for simple procedures
import tkinter
import tkinter.messagebox
from Functions import Methods

#Used to retrieve information
def textlimit():   
    #Variable used to match texbox size indentations
    counting = 0
    #Gets the text box input
    texts = text_entry.get("1.0","end-1c")
    #Methods class is initialized with help variable
    help = Methods()
    #Gets every input but summary input and puts it into a dictionary
    dictionary = initialize_dict()
    #Used to see if there are any numbers in the name text box
    try:
        #Uses number function and passes the author's name from the dictionary
        help.number(dictionary["Author"])
    except:
        #Outputs a message box if number is inputted into name textbox, clears textbox, then cancels the funtion.
        tkinter.messagebox.showinfo(message=f'Need letters for name')
        n_entry.delete("1.0","end-1c")
        return
    #Returns how many words are there based off of spaces in summary
    count = help.limit_validating(texts)
    #used to see if there too many words in summary
    if count > 29:
        #Counts how many words are over than outputs message in message box. Then clears the summary text box.
        count = count - 29
        tkinter.messagebox.showinfo(message=f'{count} words over')
        text_entry.delete("1.0","end-1c")    
    else :
        #Gets the name for the .txt file
        title_name = get_file()
        #Iterates through the summary
        for letters in texts:
            #Used incase user inputs a new line to make sure the charchter counter for each line gets a reset
            if letters == '\n':
                counting = 0
            #Opens a file with the name inputted into the text box then appends new information. Creates f as object.
            with open(f'{title_name}.txt', 'a') as f:
                #APpends a charachter at a time. Letters is charchters.
                f.write(letters)
                #Makes sure summary is formatted and indents according to textbox size. 
                counting = counting + 1
                if counting == 100:
                    f.write(f'\n')
                    counting = 0
    #iterates through tuples in dictionary with date, title, and author.
    for k, v in dictionary.items():
        #Error pops up in terminal called unboundlocalerror
        try:
            #Opens the same file and appends in new lines text box input of date, title, and author with correct prompts.
            with open(f'{title_name}.txt', 'a') as f:
                f.write(f'\n{k}-')
                f.write(f' {v}.')
        #Throws it away the error
        except:
            return
    with open(f'{title_name}.txt', 'a') as f:
        f.write(f'\n')
        f.close()
    print(dictionary)
#Gets current date from Functions file and returns it.
def date():
    help = Methods()
    current_date = help.get_date()
    return current_date
#Returns list for dictionary
def initialize_info1():
    return ["Date", "Title", "Author"]
#Returns the textbox input in a list for dictionary
def initialize_info2():
    names = get_name()
    titles = get_title()
    today = date()
    return [today, titles, names]
#Creates dictionary of tuples
def initialize_dict():
    info = initialize_info1()
    user = initialize_info2()
    a_dict = {}
    for k, v in zip(info,user):
        a_dict[k] = v
    return a_dict
#Gets the input for the file name
def get_file():
    file_name = file_name_entry.get("1.0","end-1c")
    return file_name
#Gets the input for the authors name
def get_name():
    name = n_entry.get("1.0","end-1c")
    return name
#Gets the information for the title of the book
def get_title():
    title = title_entry.get("1.0","end-1c")
    return title
#Initializing tkinter object.
m = tkinter.Tk()
#Output for author name with textbox for input
n_label = tkinter.Label(m, text="Name")
n_label.grid(row=1)
n_entry = tkinter.Text(m,width=18,height=1)
n_entry.grid(row=2)
#Output for title of book with textbox for input
title_label = tkinter.Label(m, text="Title")
title_label.grid(row=1,column=3)
title_entry = tkinter.Text(m,width=18,height=1)
title_entry.grid(row=2,column=3)
#Output for summary of book with textbox for input
text_label = tkinter.Label(m, text="Text area")
text_label.grid(row=4,column=2)
text_entry = tkinter.Text(m,width=100)
text_entry.grid(row=5,column=2)
#Button created to initialize textlimit function to validate and output data into a .txt file
texts = tkinter.Button(m, text="retrive", command=textlimit)
texts.grid(row=3,column=2)
#Output for title of file with textbox for input
file_name_label = tkinter.Label(m, text="file name")
file_name_label.grid(column=2, row=1)
file_name_entry = tkinter.Text(m,width=18,height=1)
file_name_entry.grid(row=2, column=2)
#Prompt to make sure user knows that summary cannot exceed certain limit
instruntions_forGUI = tkinter.Label(m, text="Type your book summarry above. Make sure it is below 30 words to fit on book once published.")
instruntions_forGUI.grid(row=6,column=2)
#Exit button to close tkinter
exit_button = tkinter.Button(m, text="EXIT", command=m.destroy, bg="PINK", width=10, height=3)
exit_button.grid(row=6,column=3)
#Start the program
m.mainloop()


