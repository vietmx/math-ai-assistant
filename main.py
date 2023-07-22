import wolframalpha
import wikipedia
from tkinter import *

root = Tk()


def user_input():
    """This function is used for querying through wiki and wolframalpha"""
    search = (input_ent.get())
    
    try:
        # wolframalpha
        api_id = "******-**********" # <-- you will need to enter the API key from wolframalpha
        client = wolframalpha.Client(api_id)
        # creating a client for the api_id
        result = client.query(search) 
        answer = next(result.results).text
        print(answer)
        # displaying results onto result_text widget
        result_text.insert(END, answer)
    
    except:
        # returning a summary from wiki for your question
        print(wikipedia.summary(search))

  
def clear_search():
    """This function is used to clear the values from search entry and from the results box"""
    input_ent.delete(0, "end")
    result_text.delete(1.0, END)
   

# input box for search
input_ent = Entry(root, 
                  width=57)
input_ent.place(x=26, y=100)

# submit button
submit_btn = Button(root, 
                    width=22, 
                    height=2, 
                    text="Submit",
                    command=user_input)
submit_btn.place(x=25, y=130)

# button to remove search and results
clear_btn = Button(root, 
                   width=22, 
                   height=2, 
                   text="Clear",
                   command=clear_search)
clear_btn.place(x=208, y=130)

# text box for displaying search results
result_text = Text(root,
                   width=43,
                   height=10)
result_text.place(x=25, y=190)

root.geometry("400x400")
root.resizable(0, 0)
root.attributes("-topmost", True)
root.mainloop()