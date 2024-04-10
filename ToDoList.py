# Import necessary modules
import wx
import json
import os
import sys

# Define global variables
todo_list = []

# Function to add a task to the to-do list
def add_task(event):
	task = task_entry.GetValue()
	if task.strip():
		todo_list.append({"task": task, "completed": False})
		task_entry.Clear()
		update_list()
		save_tasks()
		wx.MessageBox("Task added successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
	else:
		wx.MessageBox("Please enter a task.", "Error", wx.OK | wx.ICON_ERROR)
	task_entry.SetFocus()

# Function to mark a task as completed
def complete_task(event):
	task_index = task_list.GetSelection()
	if task_index != -1:
		if todo_list[task_index]["completed"]:
			wx.MessageBox("This task is already marked as completed!","Error", wx.OK | wx.ICON_ERROR)
		else:
			todo_list[task_index]["completed"] = True
			update_list()
			save_tasks()
			wx.MessageBox("Task marked as completed!", "Success", wx.OK | wx.ICON_INFORMATION)
			task_list.SetFocus()
	else:
		wx.MessageBox("No task selected.", "Error", wx.OK | wx.ICON_ERROR)
		task_list.SetFocus()

# Function to view the to-do list
def update_list():
	task_list.Clear()
	for task in todo_list:
		task_text = f"{task['task']} (Completed)" if task['completed'] else task['task']
		task_list.Append(task_text)

# Function to remove a task from the to-do list
def remove_task(event):
	task_index = task_list.GetSelection()
	if task_index != -1:
		removed_task = todo_list.pop(task_index)
		update_list()
		save_tasks()
		wx.MessageBox(f"Task '{removed_task['task']}' removed successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
	else:
		wx.MessageBox("No task selected.", "Error", wx.OK | wx.ICON_ERROR)
	task_list.SetFocus()

# Function to remove all tasks
def remove_all_tasks(event):
	if len(todo_list) < 1:
		wx.MessageBox("No task to remove.", "Error", wx.OK | wx.ICON_ERROR)
	else:
		dlg = wx.MessageDialog(None, "Are you sure you want to remove all tasks?", "Confirm", wx.YES_NO | wx.ICON_QUESTION)
		result = dlg.ShowModal()
		dlg.Destroy()
		if result == wx.ID_YES:
			total_length=len( todo_list )
			todo_list.clear()
			update_list()
			save_tasks()
			wx.MessageBox(f"All {total_length} tasks removed successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
	task_list.SetFocus()

# Function to save tasks to JSON file
def save_tasks():
	with open("tasks.json", "w") as file:
		json.dump(todo_list, file)

# Function to load tasks from JSON file
def load_tasks():
	try:
		with open("tasks.json", "r") as file:
			return json.load(file)
	except FileNotFoundError:
		return []

# Main program
app = wx.App()
frame = wx.Frame(None, title="To-Do List Manager", size=(400, 400))

panel = wx.Panel(frame)

task_label = wx.StaticText(panel, label="Enter &Task:")
task_entry = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

add_button = wx.Button(panel, label="&Add Task")
add_button.Bind(wx.EVT_BUTTON, add_task)

complete_button = wx.Button(panel, label="Mark Task as &Completed")
complete_button.Bind(wx.EVT_BUTTON, complete_task)

remove_button = wx.Button(panel, label="Remove T&ask")
remove_button.Bind(wx.EVT_BUTTON, remove_task)

remove_all_button = wx.Button(panel, label="&Remove all Tasks")
remove_all_button.Bind(wx.EVT_BUTTON, remove_all_tasks)

exit_button=wx.Button(panel,label="&exit")
exit_button.Bind(wx.EVT_BUTTON, sys.exit)

list_title = wx.StaticText(panel, label="&List of Tasks")
task_list = wx.ListBox(panel, style=wx.LB_SINGLE | wx.LB_ALWAYS_SB)

# Load tasks initially
todo_list = load_tasks()
update_list()

sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(task_label, 0, wx.ALL, 5)
sizer.Add(task_entry, 0, wx.EXPAND | wx.ALL, 5)
sizer.Add(add_button, 0, wx.ALL, 5)
sizer.Add(complete_button, 0, wx.ALL, 5)
sizer.Add(remove_button, 0, wx.ALL, 5)
sizer.Add(remove_all_button, 0, wx.ALL, 5)
sizer.Add(exit_button, 0, wx.ALL, 5)
sizer.Add(list_title, 0, wx.LEFT | wx.TOP, 5)
sizer.Add(task_list, 1, wx.EXPAND | wx.ALL, 5)

panel.SetSizer(sizer)

frame.Show(True)
app.MainLoop()