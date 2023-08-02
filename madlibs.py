import random


def madlibs_game(bot_name, player_name):
    print("Welcome to Mad Libs Game! Let's have some fun\n")

    # Get inputs from user
    place = input("Name the last place you visited: ")
    color = input("What is the color of your favorite shirt: ")
    album = input("Name an album you enjoy: ")
    emotion = input("Let us know how you're feeling: ")

    # The code starts here
    print()
    print()
    madlibs_story_1 = "Title: The Surprise Party\n" \
        f"Once upon a sunny day, {bot_name} decided to plan a surprise party for {player_name}. " \
        f"The party was going to be held at {place}, and {bot_name} invited all of their mutual friends. " \
        f"They secretly prepared decorations in {color}, baked a colorful cake, and arranged a playlist of {album} that {player_name} loved. " \
        f"Everything was set for a wonderful celebration. On the day of the party, {player_name} arrived at {place} to find everyone hiding. " \
        f"As they shouted, Surprise!, {player_name} couldn't help but feel {emotion}. The room was filled with laughter and joy. " \
        f"They danced to songs from {album}, played games, and shared {emotion} stories late into the night. " \
        f"The surprise party turned out to be a massive success, leaving {player_name} with memories they would treasure forever. " \
        f"In the end, {player_name} realized that the greatest gift of all was the love and friendship shared during this unforgettable celebration."

    madlibs_story_2 = f"Hello, {player_name} and {bot_name}! " \
        f"Once upon a time, in a faraway land, you both decided to visit {place}." \
        f"The sun was shining, and the sky was painted in beautiful shades of {color}." \
        f"As you explored the enchanting surroundings, you listened to your favorite album, '{album}', which filled the air with delightful melodies." \
        f"You both felt {emotion} and couldn't have been happier in that moment." \
        f"And so, your unforgettable adventure came to an end, but the memories you made will last a lifetime." \
        f"Thank you for joining us on this magical journey!" \

    madlibs_story_3 = f"I hope this letter finds you well. I am writing to share my recent adventure with you." \
        f"Dear {bot_name}," \
        f"Last week, I visited {place}, and it was an incredible experience. The weather was perfect, with the sun shining brightly and the sky painted in beautiful shades of {color}." \
        f"During my visit, I couldn't stop listening to my favorite album, '{album}', which added an extra layer of magic to the whole trip." \
        f"As I explored the enchanting surroundings, I couldn't help but feel {emotion}. It was a mix of excitement, joy, and contentment." \
        f"I wish you were there with me, {bot_name}, to share these unforgettable moments. I'm sure you would have loved every bit of it." \
        f"Please let me know when we can plan our next adventure together. I'm looking forward to more exciting experiences with you." \
        f"Take care and see you soon!" \
        f"Warm regards," \
        f"{player_name}" \

    stories = [madlibs_story_1, madlibs_story_2, madlibs_story_3]

    # Randomly choose one of the stories
    random_story = random.choice(stories)
    print(random_story)

    print()
    print(f"{bot_name} hope you enjoyed this Madlibs story")
