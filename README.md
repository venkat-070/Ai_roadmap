# AI Roadmap - Month 1: Python Fundamentals

A structured 4-week Python learning journey focused on building real-world CLI applications from scratch.

## Projects Built

### Week 1 — Contact Book CLI
A command-line contact book built with Python.
- Features: Add, View, Search, and Delete contacts
- Concepts used: Functions, *args, **kwargs, loops, dictionaries, list comprehensions
- [View Code](Ai_roadmap/day04_week1_project/contact_book.py)

### Week 2 — Bank Account OOP App
A command-line bank account manager built using Object-Oriented Programming.
- Features: Deposit, Withdraw, Check Balance, Overdraft protection
- Concepts used: Classes, objects, __init__, instance methods, inheritance, super()
- [View Code](Ai_roadmap/day07_week2_project/BankAccount_app.py)

### Week 3 — Notes Saver App
A command-line notes manager that saves data permanently to a JSON file.
- Features: Add, View, Delete notes — data persists after closing the program
- Concepts used: File handling, JSON read/write, error handling (try/except)
- [View Code](Ai_roadmap/day09_week3_project/notes_saver.py)

### Week 4 — Weather Fetcher App
A command-line weather app that fetches real-time weather data from a public API.
- Features: Enter any city name, displays temperature, humidity, wind speed, description
- Concepts used: requests library, REST APIs, JSON parsing, error handling
- [View Code](Ai_roadmap/day11_week4_project/weather_fetcher.py)

## Concepts Covered

### Week 1 — Python Fundamentals
- Functions — parameters, return values, default arguments
- *args and **kwargs
- for loops — over lists and dictionaries
- enumerate()
- List comprehensions and dictionary comprehensions
- while True loop — menu pattern

### Week 2 — Object Oriented Programming
- Classes and objects
- __init__ constructor
- self — connecting attributes to objects
- Instance methods
- __str__ method
- Inheritance and method overriding
- super().__init__()

### Week 3 — File Handling & Error Handling
- Reading and writing .txt files
- JSON file handling — json.dump() and json.load()
- try/except blocks
- Handling ValueError, ZeroDivisionError, TypeError, Exception
- os.path.exists() for file checks

### Week 4 — APIs & External Libraries
- requests library — requests.get()
- REST API concepts — endpoints, status codes
- response.status_code and response.json()
- Parsing nested JSON responses
- Error handling for network requests

# Week 5 - LLM Concepts

## Day 1 - What is an LLM?

An LLM (Large Language Model) generates text by predicting the next word, one token at a time, based on patterns learned from massive amounts of training text (books, articles, code, websites).

Before this, I assumed AI models worked like a lookup system — fetching a pre-written response from some backend database. That's wrong. The model isn't retrieving an answer; it's generating one word at a time, fresh, based on probability.

At each step, the model doesn't just pick the single "best" next word. It calculates a probability for every possible next word (e.g. "the" → 40%, "a" → 25%, "an" → 10%, etc.) and can sample from this distribution rather than always picking the top choice. This is why the same prompt can give different answers each time.

This is different from a calculator. `2+2` always has one correct, deterministic answer — no randomness involved. LLMs are not deterministic by default because of this probability-based sampling.

This randomness is controlled by a setting called **temperature** (and another called **top-p**) — covered in Day 2.

Resource used: Andrej Karpathy's "Intro to Large Language Models" (YouTube, watched 0–40 min mark).
