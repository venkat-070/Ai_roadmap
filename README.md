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

## Day 2 - Tokens, temperature , context window 
**TOKENS**:
Tokens are nothing but words in terms of LLM's. but not every word is token - sometimes a word is split into multiple tokens
example: unbelivable - "Un" + "beliv" +"able" are 3 tokens 

**Temperature:** 
Temperature controls the selection on words with the help of prediction 
low temp - accurate , safe answers , highest probability words are picked
High temp - this is used when there is a need of creative writting or narrating a story

**context window:**
This is the maximum amount of information the llm can take as input or generate as an output 
######
## Day 3 - API Keys, Requests, and Responses

**API Key:**
An API key is like a password for my program, not for me personally. It tells Google who is making the request and tracks usage. It must never be hardcoded or pushed to GitHub — if leaked, someone else could use it and I could get billed for their usage, or my key could get suspended. I'll store it in a .env file (excluded by .gitignore) and load it with python-dotenv, same as planned in Month 1.

**Request structure:**
Calling the Gemini API is similar to the Weather Fetcher app from Month 1, but uses POST instead of GET (since I'm sending data, not just asking for it). A simplified request looks like:
{

"contents": [{"parts": [{"text": "my prompt here"}]}],

"generationConfig": {"temperature": 0.7}

}
- "contents" = my actual prompt
- "generationConfig" = settings like temperature
**Response structure:**
The response comes back as JSON, and I need to dig into nested keys to extract the actual text - same skill as extracting weather data in Month 1.
{
"candidates": [{"content": {"parts": [{"text": "the actual answer"}]}}]
}
To extract the text in Python:
```python
response_data["candidates"][0]["content"]["parts"][0]["text"]
```
This is the same overall workflow as Weather Fetcher: build request → send it → get JSON back → extract the field I need → display it. The new pieces this week: API key for authentication, and POST instead of GET.

# Week 6 - Gemini API Basics

## What I learned
- How to initiate api call from python script
- The use of system prompt
- 

## Scripts
- `day1_first_call.py` - This code makes a api call to gemini model and returns the output.
- `day2_system_prompt.py` - The system prompt are the instructions given to the model on how output is to be generated.

## Tech Stack
- Python
- Google Gemini API
- python-dotenv

## How to run
1. Clone this repo
2. `pip install google-generativeai python-dotenv`
3. Add `GEMINI_API_KEY=your_key` to `.env`
4. Run any script: `python day1_first_call.py`


# Week 7 - Prompt Engineering

## What I learned
- The difference in prompts given to model using two methods zero-shot and few-shot
- How to tell a model to output the answer in json strurture.
- The chain of thought is a process of making the model produce an output in step by step process.

## Scripts
- `day1_zeroshot_vs_fewshot.py` - The model returns an output with nrml prompt and a prompt with examples on how to generate output.
- `day2_json_output.py` - giving a struture to the model to return in the same format
- `day3_chain_of_thought.py` - Making the model think in step by step process which increases model performance.
- `day4_prompt_comparison.py` - The comparision between zero-shot , few-shot , chain of thought.

## Key concepts covered
- Zero shot vs few shot 
- Json strurcture output 
- chain of thought

## Tech Stack
- Python
- Groq API (LLaMA 3.3 70B)
- python-dotenv

# Week 8 - streamlit app

## What it does
** It is an assistant helps us in our tasks. additionally replies in the tone we need. **

## Features
- An option to enter prompt aliased as topic in the app , which helps user to ask his thoughts.
- **Tone** : The tone selection feature which states the assistant , in which tone the response should be addressed.

## Tech Stack
- Python
- Streamlit
- Groq API (LLaMA 3.3 70B)
- python-dotenv

## Live Demo
Url: [https://appapp-stsybjawozpdstmwrwypv3.streamlit.app/]

## How to run locally
1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Groq API key to a `.env` file: `GROQ="your_key_here"`
4. Run: `streamlit run app.py`
