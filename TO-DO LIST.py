# Import the tkinter module for creating GUI Components
from tkinter import *
from tkinter import messagebox

class iTask():
    #iTask class for managing a To-Do list.
    #Features:
    #- Add, delete, clear tasks
    #- Save tasks to a file
    #- Display information about the app
    
    def Todo_info(self):
        # Display an information dialog about the application.
        messagebox.showinfo(
            "info", "This is Todolist V.1.0 \n Created by Rashika Gangraj\n Python Project", )

    def __init__(self, root):
        # Initialize the iTask
        self.root = root
        self.tasks = []

        # Configure the main window properties
        self.root.geometry('500x450+500+200')
        self.root.title("iTask List")
        self.root.config(bg='#223441')
        self.root.resizable(width=False, height=False)

        # Create a frame to hold the task list and scrollbar
        self.frame = Frame(self.root)
        self.frame.pack(pady=10)

        # Create a Listbox to display tasks
        self.task_list = Listbox(
            self.frame,
            width=25,
            height=8,
            font=('Times', 18),
            bd=0,
            fg='#464646',
            highlightthickness=0,
            selectbackground='#a6a6a6',
            activestyle="none",
        )
        self.task_list.pack(side=LEFT, fill=BOTH)

        # Create a scrollbar for the Listbox
        self.sb = Scrollbar(self.frame)
        self.sb.pack(side=RIGHT, fill=Y)

        # Configure the scrollbar with the Listbox
        self.task_list.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.task_list.yview)

        # Predefined tasks for the list
        predefined_tasks = [
            'Workout', 'Breakfast', 'Write a blog', 'Practice Coding', 'DSA', 
            'Cycling', 'Paint canvas', 'Task 10', 'Task 11', 'Task 12', 
            'Task 13', 'Task 14', 'Task 15'
        ]
        for task in predefined_tasks:
            self.task_list.insert(END, task)
            self.tasks.append(task)

        # Create an Entry widget for task input
        self.my_entry = Entry(
            self.root,
            font=('times', 24)
        )
        self.my_entry.pack(pady=20)

        self.button_frame = Frame(self.root)
        self.button_frame.pack(pady=20)

        # Create buttons for adding, deleting, clearing, saving tasks, and showing info
        self.addTask_btn = Button(
            self.button_frame,
            text='Add Task',
            font=('times 14'),
            bg='#c5f776',
            padx=20,
            pady=10,
            command=self.add_task_from_entry
        )
        self.addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

        self.delTask_btn = Button(
            self.button_frame,
            text='Delete Task',
            font=('times 14'),
            bg='#ff8b61',
            padx=20,
            pady=10,
            command=self.delete_task
        )
        self.delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

        self.clear_button = Button(
            self.button_frame,
            text='Clear',
            font=('times 14'),
            bg='#ff8b61',
            padx=20,
            pady=10,
            command=self.clear_task
        )
        self.clear_button.pack(fill=BOTH, expand=True, side=LEFT)

        self.save_button = Button(
            self.button_frame,
            text='Save',
            font=('times 14'),
            bg='#c5f776',
            padx=20,
            pady=10,
            command=self.save_task
        )
        self.save_button.pack(fill=BOTH, expand=True, side=LEFT)

        self.info_button = Button(
            self.button_frame,
            text='Info',
            font=('times 14'),
            bg='#c5f776',
            padx=20,
            pady=10,
            command=self.Todo_info
        )
        self.info_button.pack(fill=BOTH, expand=True, side=LEFT)

    def add_task_from_entry(self):
        # Add a task from the entry widget to the list
        task = self.my_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(END, task)
            self.my_entry.delete(0, END)

    def clear_task(self):
        #Clear all tasks from the list
        self.task_list.delete(0, END)
        self.tasks = []

    def delete_task(self):
        # Delete the selected task from the list
        task_index = self.task_list.curselection()
        if task_index:
            task_index = task_index[0]
            self.tasks.pop(task_index)
            self.task_list.delete(task_index)

    def save_task(self):
        # Save the current list of tasks to a text file
        with open("iTask.txt", 'w') as f:
            for task in self.tasks:
                f.write(task + '\n')

# Create the main application and run the iTask application
root = Tk()
iTask_list = iTask(root)
root.mainloop()
 