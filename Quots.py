import random

def random_quote_generator():
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today.",
        "Do not watch the clock. Do what it does. Keep going.",
        "The future depends on what you do today.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Act as if what you do makes a difference. It does."
    ]
    print("Random Quote: ", random.choice(quotes))


random_quote_generator()
