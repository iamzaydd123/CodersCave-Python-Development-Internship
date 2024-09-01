import tkinter as tk 
from tkinter import messagebox as tkMessageBox


class TaskSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Scheduler")

        self.tasks = []

        self.task_label = tk.Label(root, text="Task:")
        self.task_label.grid(row=0, column=0, padx=10, pady=10)

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.tasks_listbox = tk.Listbox(root, width=50, height=15)
        self.tasks_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        self.clear_button = tk.Button(root, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            tkMessageBox.showwarning("Input Error", "Please enter a task.")

    def edit_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.update_task_list()
                self.task_entry.delete(0, tk.END)
            else:
                tkMessageBox.showwarning("Input Error", "Please enter a task.")
        except IndexError:
            tkMessageBox.showwarning("Selection Error", "Please select a task to edit.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            tkMessageBox.showwarning("Selection Error", "Please select a task to delete.")

    def clear_tasks(self):
        if tkMessageBox.askyesno("Clear All Tasks", "Are you sure you want to delete all tasks?"):
            self.tasks = []
            self.update_task_list()

    def update_task_list(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskSchedulerApp(root)
    root.mainloop()
