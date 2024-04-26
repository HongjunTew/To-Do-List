# To-Do-List tool, changes

## Sunday, April 21, 2024
* Fixed shortcut conflicts. Remove all button is now rename to delete all, and shortcut is alt+d. Enter task text edit box is alt+e, remove a task button is alt+r, and exit button is alt+x.

## Wednesday, April 10, 2024
* Added the check to completion of tasks. From now on, trying to mark as completed upon the task that is already marked as completed will end up failure, displaying error message.
* Added `compile.bat` file into the directory, allowing to compile into executable to be distributed.
* Added error handling in `save_tasks()` function to handle cases where the list is empty or the file doesn't exist.
* Changed `totallen` to `total_len` for consistency.
* Corrected the naming convention for the `quit_button` variable.
* Added missing indentation in the `remove_task` function after `else` block.

## Tuesday, April 09, 2024
* Added exit button. Shortcut keys are now spoken as using the & keyword.
* Added a new feature called remove all, which removes all tasks.
* Now, If the tasks list has less than 1 elements, the save function will delete the `tasks.json` file.

## Monday, April 08, 2024,
* added focuses in failures and successes

## Thirsday April 04, 2024
* Changed to GUI tool using wx.
* updated Readme.
* Added the ability to save, in JSON format.
* First release