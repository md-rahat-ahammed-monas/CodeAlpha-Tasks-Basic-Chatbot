# CodeAlpha_Simple-Chatbot

A simple rule-based chatbot developed using Python as part of the CodeAlpha Python Programming Internship.

## Project Overview

This project is a beginner-friendly, command-line rule-based chatbot. It interacts with the user by listening to specific predefined keywords/phrases and responding accordingly using basic conditional statements and a `while` loop.

## Features

* Interactive command-line interface
* Keyword-based responses (hello, how are you, bye)
* Graceful exit mechanism on saying 'bye'
* Default fallback response for unknown inputs

## Concepts Used

* Python Programming
* Functions (`def`)
* `while` loop
* Conditional statements (`if`, `elif`, `else`)
* `input()` for user input
* `print()` for displaying output
*  String method (`.capitalize()`)

## How the Program Works

1. The program starts and welcomes the user, showing available commands.
2. It enters an infinite `while` loop to continuously listen for user input.
3. User input is converted to lowercase to ensure case-insensitive matching.
4. The `if-elif-else` block checks the input:
* If the user says **"Hello"**, the chatbot greets back.
* If the user asks **"How are you"**, the chatbot replies.
* If the user says **"Bye"**, the chatbot says goodbye and breaks the loop to exit the program.
* For any other input, the chatbot displays a polite fallback message.



## Example

```text
Chatbot: Hi! I am a simple chatbot.
Chatbot: You can say 'hello', 'how are you', or 'bye'.
You: hello
Chatbot: Hi!
You: How are you?
Chatbot: I'm fine, thanks!
You: what is your name?
Chatbot: Sorry, I don't understand that.
You: bye
Chatbot: Goodbye!

```

## Technology Used

* Language: Python
* Development Environment: Visual Studio Code

## Project Structure

```text
CodeAlpha-Basic-Chatbot/
│
├── chatbot.py
└── README.md

```

## Learning Outcomes

Through this project, I practiced:

* Python fundamentals and syntax
* Continuous execution loops (`while True`)
* Conditional branching (`if-elif-else`)
* Basic Natural Language Processing (NLP) pattern matching concepts
* Handling user input and program termination

## How to Run

1. **Clone the repository**
```bash
git clone https://github.com/md-rahat-ahammed-monas/CodeAlpha-Basic-Chatbot.git

```


2. **Open the project folder**
```bash
CodeAlpha-Basic-Chatbot

```


3. **Run the Python program**
```bash
Basic Chatbot.py

```



## Project Goal

The goal of this project is to practice fundamental Python programming concepts by developing a simple interactive command-line chatbot.
