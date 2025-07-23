---
description:
globs:
alwaysApply: true
---

### ✅ Task: Interactive Task Loop with User Feedback

## 1. Initial Setup
**Check file**: Verify if `userinput.py` exists in root directory
- **If missing**: Create file with exact content:
```python
# userinput.py
user_input = input("prompt: ")
```
- **If exists**: Proceed to normal task execution

## 2. Task Execution Protocol
**For each assigned task**:
1. **Execute**: Complete the designated task
2. **Conditional Feedback**: Only when having doubts about the tasks:
   - Execute: `python userinput.py`
   - **Terminal requirement**: Must be open in chat window
   - **Read input**: Capture user response about doubts/guidance
   - **Process input**: Apply received feedback to tasks
3. **Continue**: Keep executing next tasks

## 3. Flow Control
**Continuation**: Loop continues indefinitely executing tasks
**Completion**: Mark all tasks as complete **ONLY** when user types `"stop"`
