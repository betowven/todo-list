# Todo List With python Using Tkinter
This project is a simple to-do list application implemented using the Tkinter library in Python. The code creates a GUI window with a listbox to display tasks, an entry field to input new tasks, and two buttons to add and delete tasks.

Here is the English translation of the code:

## installation
```
pip install tkinter
```
requirements : ```tkinter```
# Function to add a task to the list
```python
from tkinter import *

def add_task():
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
```

# Function to delete a selected task from the list
```python
def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass
```
# Create the root window
```python
root = Tk()
root.title("To-Do List")
```
# Create a frame to hold the listbox
```python
frame = Frame(root)
frame.pack(pady=10)
```
# Create a listbox to display tasks
```python
listbox = Listbox(
    frame,
    width=50,
    height=10,
    font=("Courier New", 12)
)
listbox.pack(side=LEFT, fill=Y)
```
# Create a scrollbar for the listbox
```python
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
```
# Configure the listbox to use the scrollbar
```python
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

```
# Create an entry field to input new tasks
```python
entry = Entry(
    root,
    font=("Courier New", 12)
)
entry.pack(pady=10)
```
# Create a frame to hold the buttons
```python
button_frame = Frame(root)
button_frame.pack(pady=10)
```
# Create a button to add a task
```python
add_button = Button(
    button_frame,
    text="Add Task",
    command=add_task
)
add_button.pack(side=LEFT)
```
# Create a button to delete a task
```python
delete_button = Button(
    button_frame,
    text="Delete Task",
    command=delete_task
)
delete_button.pack(side=LEFT)
```
# Start the main event loop
**root.mainloop()**

**This code creates a window titled "To-Do List" with a listbox to display tasks, an entry field to input new tasks, and two buttons to add and delete tasks. The tasks are stored in the listbox and can be added or deleted using the respective buttons.
tkinter**

<h2>🛡️ License:</h2>

This project is licensed under the  [Sadra Kakami](https://discord.com/users/957658384629391410)
