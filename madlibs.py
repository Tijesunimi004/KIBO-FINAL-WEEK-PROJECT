import random
def madlibs_game():
  print("Welcome to Mad Libs Game! Let's have some fun")
  print()
  name = input("What is your name? ")
  friend_name = input("Enter a friend's name: ")
  place = input("Name the last place you visited: ")
  color = input("What is the color of your favorite shirt: ")
  album = input("Name an album you enjoy: ")
  emotion = input("Let us know how you're feeling: ")

# The code starts here
  print()
  print("Title: The Surprise Party")
  print()
  madlibs_story_1 = f"Once upon a sunny day, {friend_name} decided to plan a surprise party for {name}. The party was going to be held at {place}, and {friend_name} invited all of their mutual friends. They secretly prepared decorations in {color}, baked a colorful cake, and arranged a playlist of {album} that {name} loved. Everything was set for a wonderful celebration. On the day of the party, {name} arrived at {place} to find everyone hiding. As they shouted, Surprise!, {name} couldn't help but feel {emotion}. The room was filled with laughter and joy. They danced to songs from {album}, played games, and shared {emotion} stories late into the night. The surprise party turned out to be a massive success, leaving {name} with memories they would treasure forever. In the end, {name} realized that the greatest gift of all was the love and friendship shared during this unforgettable celebration."
  madlibs_story_2 = f"""
    Hello, {name} and {friend_name}! 
    Once upon a time, in a faraway land, you both decided to visit {place}.
    The sun was shining, and the sky was painted in beautiful shades of {color}.

    As you explored the enchanting surroundings, you listened to your favorite album, '{album}', which filled the air with delightful melodies.

    You both felt {emotion} and couldn't have been happier in that moment.

    And so, your unforgettable adventure came to an end, but the memories you made will last a lifetime.

    Thank you for joining us on this magical journey!
    """
  madlibs_story_3 = f"""
    Dear {friend_name},

    I hope this letter finds you well. I am writing to share my recent adventure with you.

    Last week, I visited {place}, and it was an incredible experience. The weather was perfect, with the sun shining brightly and the sky painted in beautiful shades of {color}.

    During my visit, I couldn't stop listening to my favorite album, '{album}', which added an extra layer of magic to the whole trip.

    As I explored the enchanting surroundings, I couldn't help but feel {emotion}. It was a mix of excitement, joy, and contentment.

    I wish you were there with me, {friend_name}, to share these unforgettable moments. I'm sure you would have loved every bit of it.

    Please let me know when we can plan our next adventure together. I'm looking forward to more exciting experiences with you.

    Take care and see you soon!

    Warm regards,
    {name}
    """

  stories = [madlibs_story_1, madlibs_story_2, madlibs_story_3]

    # Randomly choose one of the stories
  random_story = random.choice(stories)
  print(random_story)

  print()
  print("We hope you enjoyed this Madlibs story")
