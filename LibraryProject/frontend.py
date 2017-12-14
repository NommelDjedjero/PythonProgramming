# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:52:05 2017

@author: ghisl
"""

"""
A program that stores this book information
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Add entry 
Update entry
Delete an entry
Close the program 
"""

#//////////////////BUILDING THE FRONT-END INTERFACE ////////////////////////////#
from tkinter import*
import backend
windows = Tk()
# variables
l1 = Label(windows,text="Title")
l1.grid(row=0,column=0)

l2 = Label(windows,text="Author")
l2.grid(row=0,column=2)

l3 = Label(windows,text="Year")
l3.grid(row=1,column=0)

l4 = Label(windows,text="ISBN")
l4.grid(row=1,column=2)

# Creating entries
title_text = StringVar()
e1 = Entry(windows,textvariable = title_text)
e1.grid(row=0, column =1)

author_text = StringVar()
e2 = Entry(windows,textvariable = author_text)
e2.grid(row=0, column =3)

year_text = StringVar()
e3 = Entry(windows,textvariable = year_text)
e3.grid(row=1, column =1)

isbn_text = StringVar()
e4 = Entry(windows,textvariable = isbn_text)
e4.grid(row=1, column =3)

# Create the Listbox
list1 = Listbox(windows,height=6, width=35)
list1.grid(row=2,column=0, rowspan=6,columnspan=2)
# create scroll bar for the listbox
sb1 = Scrollbar(windows) # attach it to the window
sb1.grid(row=2,column=2,rowspan=6) # show it on the grid
# configure the listbox and scrollbar for them to work together
list1.configure(yscrollcommand=sb1.set) # want a vertical scroll bar commanded by the sb1 scroll bar
sb1.configure(command=list1.yview) # shows the vertical view of the object in listBox

# Create Buttons
b1 = Button(windows,text="View all", width = 12)
b1.grid(row=2,column=3)

b2 = Button(windows,text="Search entry", width = 12)
b2.grid(row=3,column=3)

b3 = Button(windows,text="Add entry", width = 12)
b3.grid(row=4,column=3)

b4 = Button(windows,text="Update", width = 12)
b4.grid(row=5,column=3)

b4 = Button(windows,text="Delete", width = 12)
b4.grid(row=6,column=3)

b4 = Button(windows,text="Close", width = 12)
b4.grid(row=7,column=3)


windows.mainloop()