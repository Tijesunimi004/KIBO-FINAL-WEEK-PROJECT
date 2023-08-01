def quiz_func():
    print("Pick a Category")
    options = ["Anime", "Films", "General Knowledge"]
    for (i, option) in enumerate(options):
        print(f"{i + 1}. {option}")
    choice = input("Pick a number: ")

    if choice.isdecimal() and int(choice) == 1:
        print("Welcome to the Anime Quiz! Please answer A, B, C, or D\n")
        # Anime quiz questions and answers
        questions_anime = [
                "What is the name of the stuffed lion in Bleach?\n A. Kon\n B. Urdiu\n C. Jo\n D. Chad",
                "What is the last name of Edward and Alphonse in the Fullmetal Alchemist series?\n A. Ellis\n B. Eliek\n C. Elric\n D. Elwood",
                "Which anime follows the story of a young boy, Gon Freecss, as he aspires to become a Hunter and find his father?\n A. Hunter x Hunter\n B. My Hero Academia\n C. Fairy Tail\n D. Black Clover",
                "In Attack on Titan, which branch of the military is responsible for conducting research on the Titans?\n A. Garrison\n B. Military Police Brigade\n C. Survey Corps\n D. Scout Regiment",
                "In Naruto, who is known as the Copy Ninja and is the sensei of Naruto and Sasuke?\n A. Kakashi Hatake\n B. Jiraiya\n C. Itachi Uchiha\n D. Orochimaru",
            ]

        correct_anime_answers = ["A", "C", "A", "C", "A"]
        anime_quiz_score = 0

        for i, question_anime in enumerate(questions_anime):
            print(question_anime)
            answer_anime = input("Your Answer: ").upper()

            if answer_anime in ["A", "B", "C", "D"]:
                if answer_anime == correct_anime_answers[i]:
                    anime_quiz_score += 10

            print("Your Anime Quiz Score:", anime_quiz_score)

    elif choice.isdecimal() and int(choice) == 2:
        print("Welcome to the Films Quiz! Please answer A, B, C, or D\n")
                    # Films quiz questions and answers
        questions_films = [
                "Which movie features a young lion cub named Simba, who must reclaim his kingdom from his uncle Scar?\n A. The Lion King\n B. Beauty and the Beast\n C. Aladdin\n D. Frozen",
                "Who directed the film 'Inception'?\n A. Christopher Nolan\n B. Steven Spielberg\n C. Quentin Tarantino\n D. Martin Scorsese",
                "Which movie won the Academy Award for Best Picture in 2020?\n A. Parasite\n B. Joker\n C. 1917\n D. The Shape of Water",
                "Which iconic film features the line 'Here's looking at you, kid'?\n A. Casablanca\n B. The Godfather\n C. Titanic\n D. Forrest Gump",
                "Which animated film follows the adventures of a young robot named WALL-E, who falls in love with another robot named EVE?\n A. Ratatouille\n B. Toy Story\n C. Finding Nemo\n D. WALL-E",
            ]

        correct_films_answers = ["A", "A", "A", "A", "D"]
        films_quiz_score = 0

        for i, question_films in enumerate(questions_films):
            print(question_films)
            answer_films = input("Your Answer: ").upper()

        if answer_films in ["A", "B", "C", "D"]:
            if answer_films == correct_films_answers[i]:
                films_quiz_score += 10

        print("Your Films Quiz Score:", films_quiz_score)

    elif choice.isdecimal() and int(choice) == 3:
        print("Welcome to the General Knowledge Quiz! Please answer A, B, C, or D\n")
            # General Knowledge quiz questions and answers
        questions_general_knowledge = [
                "What is the capital of France?\n A. Berlin\n B. London\n C. Paris\n D. Madrid",
                "Which planet is known as the 'Red Planet'?\n A. Venus\n B. Mars\n C. Jupiter\n D. Saturn",
                "What is the largest organ in the human body?\n A. Liver\n B. Heart\n C. Brain\n D. Skin",
                "Who wrote the play 'Romeo and Juliet'?\n A. William Shakespeare\n B. Oscar Wilde\n C. Charles Dickens\n D. Jane Austen",
                "Which famous scientist formulated the theory of relativity?\n A. Isaac Newton\n B. Galileo Galilei\n C. Albert Einstein\n D. Nikola Tesla",
            ]

        correct_general_knowledge_answers = ["C", "B", "D", "A", "C"]
        general_knowledge_score = 0

        for i, question_gk in enumerate(questions_general_knowledge):
                print(question_gk)
                answer_gk = input("Your Answer: ").upper()

                if answer_gk in ["A", "B", "C", "D"]:
                    if answer_gk == correct_general_knowledge_answers[i]:
                        general_knowledge_score += 10

        print("Your General Knowledge Quiz Score:", general_knowledge_score)

    else:
        print("Invalid choice or category. Please select the Anime (1), Films (2), or General Knowledge (3) category.")
