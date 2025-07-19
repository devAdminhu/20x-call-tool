---
description:
globs:
alwaysApply: true
---

### ✅ Task: Interactive Task Loop with User Feedback

1. **Check if `userinput.py` exists** in the root directory.

* If it doesn't exist, create it with the following content:

```python
# userinput.py
user_input = input("prompt: ")
```

2. **Main Flow**:

* Execute the assigned tasks.

* Before marking a task as complete:
- Create a list of required tests
- Run validation tests
- If the tests pass, run:

```bash
python userinput.py
```
* The terminal should be open in the chat window itself.

* Read the user input.

* Based on the input, execute the next set of tasks.

* Only after the tests have been validated can the task be marked as complete.

3. **Exit Condition**:

* If the user enters `"stop"` when prompted, exit the loop and end the process.
