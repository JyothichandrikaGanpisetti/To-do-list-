import tkinter as tk
from tkinter import messagebox

# Function to add a task to the listbox
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete the selected task from the listbox
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to clear all tasks from the listbox
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Function to exit the application
def exit_app():
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("To-Do List Application")

# Create a frame for the task list and scrollbar
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

# Create a scrollbar
task_scrollbar = tk.Scrollbar(task_frame)
task_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a listbox for the tasks
task_listbox = tk.Listbox(task_frame, height=10, width=50, yscrollcommand=task_scrollbar.set, selectbackground="lightblue")
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Configure the scrollbar
task_scrollbar.config(command=task_listbox.yview)

# Create an entry widget to add tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Create a button to add tasks
add_task_button = tk.Button(root, text="Add Task", width=48, command=add_task)
add_task_button.pack(pady=5)

# Create a button to delete the selected task
delete_task_button = tk.Button(root, text="Delete Selected Task", width=48, command=delete_task)
delete_task_button.pack(pady=5)

# Create a button to clear all tasks
clear_tasks_button = tk.Button(root, text="Clear All Tasks", width=48, command=clear_tasks)
clear_tasks_button.pack(pady=5)

# Create a button to exit the application
exit_button = tk.Button(root, text="Exit", width=48, command=exit_app)
exit_button.pack(pady=5)

# Start the main event loop
root.mainloop()
