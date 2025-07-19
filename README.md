#20x-Tool-Calls - Interactive Loop with User Feedback

A simple rules setup designed for agent-based coding assistants that support tool calls, helping you maximize your monthly tool call allowance through an interactive loop with user input.

## 🚀 How It Works
Each cycle receives text input from the user.

The `userinput.py` script handles input collection and prompts for the next task.

The loop runs automatically until you type `stop` or reach the tool call limit.


## ✅ Requirements
Python 3.8 or higher


## 🔧 How to Use
Create the .cursor/rules directory in your project:

```bash
   mkdir -p .cursor/rules
```
Copy the rules.md file into the newly created directory.

Rename rules.md to rules.mdc:

```bash
   mv .cursor/rules/rules.md .cursor/rules/rules.mdc
````
Run the script:
```bash
   python userinput.py
```

📌 Notes
Type stop to exit the loop.

The goal is to maximize tool call usage within your monthly allowance.
