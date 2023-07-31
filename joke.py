def bot_joke():
    jokes = [
        "There are only 10 kinds of people in this world: those who know binary and those who don’t.",
        "Got a B in my computer programming class. Call that a C++",
        "Q: Why did the programmer quit his job?\nA: Because they didn't get arrays.",
        "Q. How did the programmer die in the shower?\nA. They read the shampoo bottle instructions: Lather. Rinse. Repeat.",
        "Q: How many programmers does it take to screw in a light bulb? A: None. It's a hardware problem.",
        "A programmer is heading out to the grocery store. Their mom says 'get a gallon of milk, and if they have eggs, get a dozen.' They return with 13 gallons of milk.",
        "A programmer's friend asked about their new baby, 'Is it a boy or a girl?'\nThe programmer responded,'Yes'.",
    ]

    print("A joke, eh? Here you go: ")
    print()
    joke = jokes[random.randint(0, len(jokes) - 1)]
    print(joke)
