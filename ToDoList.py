import wx
import json
import os

# Function to add a task to the to-do list
def add_task(event):
	task = task_entry.GetValue()
	if task.strip():
		todo_list.append(task)
		task_entry.Clear()
		update_list()
		save_tasks()
		wx.MessageBox("Task added successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
	else:
		wx.MessageBox("Please enter a task.", "Error", wx.OK | wx.ICON_ERROR)

# Function to mark a task as completed
def complete_task(event):
	task_index = task_list.GetSelection()
	if task_index != -1:
		todo_list[task_index] += " - Completed"
		update_list()
		save_tasks()
		wx.MessageBox("Task marked as completed!", "Success", wx.OK | wx.ICON_INFORMATION)
	else:
		wx.MessageBox("No task selected.", "Error", wx.OK | wx.ICON_ERROR)

# Function to view the to-do list
def update_list():
	task_list.Clear()
	for task in todo_list:
		task_list.Append(task)

# Function to remove a task from the to-do list
def remove_task(event):
	task_index = task_list.GetSelection()
	if task_index != -1:
		removed_task = todo_list.pop(task_index)
		update_list()
		save_tasks()
		wx.MessageBox(f"Task '{removed_task}' removed successfully!", "Success", wx.OK | wx.ICON_INFORMATION)
	else:
		wx.MessageBox("No task selected.", "Error", wx.OK | wx.ICON_ERROR)

# Function to remove all.
def remove_all_tasks(event):
	if len( todo_list) <1:
		wx.MessageBox("No task to remove.", "Error", wx.OK | wx.ICON_ERROR)
	else:
		totallen=len(todo_list)
		todo_list.clear()
		update_list()
		save_tasks()
		wx.MessageBox(f"{totallen} task{"s" if totallen >1 else ""} removed successfully!", "Success", wx.OK | wx.ICON_INFORMATION)

# Function to save tasks to JSON file
def save_tasks():
	if len(todo_list)<1:
		os.remove("tasks.json")
	else:

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
todo_list = load_tasks()

app = wx.App()
frame = wx.Frame(None, title="To-Do List Manager", size=(400, 400))

panel = wx.Panel(frame)

task_label = wx.StaticText(panel, label="Enter Task:")
task_entry = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

add_button = wx.Button(panel, label="Add Task")
add_button.Bind(wx.EVT_BUTTON, add_task)

complete_button = wx.Button(panel, label="Mark Task as Completed")
complete_button.Bind(wx.EVT_BUTTON, complete_task)

remove_button = wx.Button(panel, label="Remove Task")
remove_button.Bind(wx.EVT_BUTTON, remove_task)

remove_all_button = wx.Button(panel, label="Remove all Tasks")
remove_all_button.Bind(wx.EVT_BUTTON, remove_all_tasks)

list_title = wx.StaticText(panel, label="Tasks")
task_list = wx.ListBox(panel, style=wx.LB_SINGLE | wx.LB_ALWAYS_SB)

#Set shortcuts.
accelerator_entries = [
(wx.ACCEL_ALT, ord("A"), add_button.GetId()),
(wx.ACCEL_ALT, ord("F"), complete_button.GetId()),
(wx.ACCEL_ALT, ord("D"), remove_button.GetId()),
(wx.ACCEL_ALT, ord("R"), remove_all_button.GetId())
]
accelerator_table = wx.AcceleratorTable(accelerator_entries)
frame.SetAcceleratorTable(accelerator_table)

# Load tasks initially
update_list()

sizer = wx.BoxSizer(wx.VERTICAL)
sizer.Add(task_label, 0, wx.ALL, 5)
sizer.Add(task_entry, 0, wx.EXPAND | wx.ALL, 5)
sizer.Add(add_button, 0, wx.ALL, 5)
sizer.Add(complete_button, 0, wx.ALL, 5)
sizer.Add(remove_button, 0, wx.ALL, 5)
sizer.Add(remove_all_button, 0, wx.ALL, 5)
sizer.Add(list_title, 0, wx.LEFT | wx.TOP, 5)
sizer.Add(task_list, 1, wx.EXPAND | wx.ALL, 5)

panel.SetSizer(sizer)

frame.Show(True)
app.MainLoop()
