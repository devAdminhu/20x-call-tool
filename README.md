20x Call Tool
A tool for interactive user input processing with image and text handling capabilities, built with CustomTkinter and Pillow.
Setup Instructions

Clone the Repository:
git clone https://github.com/devAdminhu/20x-call-tool.git
cd 20x-call-tool


Install Dependencies: Ensure you have Python installed. Then, install the required packages:
pip install customtkinter CTkMessagebox Pillow


Configure Cursor IDE: To enable the interactive task loop in the Cursor IDE, follow these steps:

Create a directory named .cursor/rules/ in the root of the project:
mkdir -p .cursor/rules


Copy the content of rules.md (provided below) into a new file named .mdc inside .cursor/rules/:
touch .cursor/rules/.mdc


Open .cursor/rules/rules.mdc in a text editor and paste the following content:
---
description: 
globs: 
alwaysApply: true
---

### ✅ Task: Interactive Task Loop with User Feedback 

1. The `userinput.py` file must be present in the root directory.

2. **Main Flow** (priority):

   * Perform your assigned tasks.

   * Run:

     ```bash
     python userinput.py
     ```
   * The terminal should open in the chat window itself.

   * Read the user's input.

   * Based on the input, perform the next set of tasks.

   * Repeat the process after finishing each created task list.

3. **Exit Condition**:

   * If the user types `"stop"` when prompted, exit the loop and terminate the process.


Save the .mdc file.



Run the Application: Execute the main script to start the interactive loop:
python userinput.py



Usage

The application prompts you to choose between uploading an image or entering text.
If you choose an image:
Select an image file (PNG, JPG, JPEG, BMP, or GIF).
The image is copied to 20xbuild/img/, and old images are removed.
You can optionally add a prompt for the AI.


If you choose text:
Enter a text prompt for the AI.


The program outputs the result and any additional prompt to the console.
To exit, type "stop" when prompted (if integrated with the task loop).

Requirements

Python 3.x
Libraries: customtkinter, CTkMessagebox, Pillow

Project Structure

userinput.py: Main script for user interaction and image/text processing.
.cursor/rules/.mdc: Configuration file for Cursor IDE to enable the interactive task loop.
