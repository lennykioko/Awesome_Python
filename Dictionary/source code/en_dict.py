import json
from tkinter import *
from difflib import get_close_matches

# Backend code
with open("data.json") as json_data:
    data = json.load(json_data)

def define(word):
    word = word.lower()

    if word in data:
        return data[word]
    
    elif word.title() in data: # if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    
    elif word.upper() in data: # in case user enters words like USA or NATO
        return data[word.upper()]

    elif get_close_matches(word, data.keys()):
        closest_match = get_close_matches(word, data.keys())[0]
        return "Did you mean {} instead? Please double check your input".format(closest_match)

    else:
        return "Sorry, that word does not exist"



# Frontend code
def define_command():
    word = word_entry.get()
    definition.delete(1.0, END)
    definition.insert(END, define(word))


window = Tk()
window.geometry("348x250")
window.wm_title("English Dictionary")
window.wm_iconbitmap('dict_icon.ico')


word_label = Label(window, text="Enter the word:")
word_label.grid(row=0, column=0, padx=5, pady=20)


search_text = StringVar()
word_entry = Entry(window, textvariable=search_text)
word_entry.grid(row=0, column=1, padx=5, pady=20)


search_button = Button(window, text="Search", width=12, command=define_command, bg='khaki')
search_button.grid(row=0, column=2)


definition = Text(master=window, height=10, width=35)
definition.grid(row=2, column=0, rowspan=10, columnspan=5)

scroller = Scrollbar(window)
scroller.grid(row=2,column=3,rowspan=10)

definition.configure(yscrollcommand=scroller.set)
scroller.configure(command=definition.yview)
             

window.mainloop()
