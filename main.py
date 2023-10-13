import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        pass

window = tk.Tk()
window.title("Task Manager")

frame = tk.Frame(window)
frame.pack(pady=10)

listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    font=("Courier New", 12)
)
listbox.pack(side=tk.LEFT, fill=tk.Y)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(
    window,
    font=("Courier New", 12)
)
entry.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    command=add_task
)
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    command=delete_task
)
delete_button.pack(side=tk.LEFT)

window.mainloop()
