import re
import random


chars = ["Monica", "Phoebe", "Rachel", "Ross", "Joey", "Chandler"]


def setup():
    """Read and parse the friends file, building a map of lines per char"""
    with open("Friends_Transcript.txt") as f:
        fulltext = f.read()

    # This is not perfect. There were one or two episodes that were missing
    # end tag. But this is good enough.
    episodes = re.split("End\n|\nTHE END\n", fulltext)

    episode_maps = []
    for episode in episodes:
        lines = [line.strip() for line in episode.split("\n") if line.strip()]
        if not lines:
            continue
        episode_map = {char: [line.strip(f"{char}: ")
                              for line in lines
                              if line.startswith(f"{char}:")]
                       for char in chars}
        episode_map["title"] = lines[0]
        episode_maps.append(episode_map)

    return episode_maps


def menu(episode_maps):
    menu = """
(1) about
(2) explore
(3) play
(q) quit
"""
    while True:
        print(menu)
        resp = input("Enter your choice --> ").strip()
        if resp == "1":
            print("Approx num episodes:", len(episode_maps))
            for index, map in enumerate(episode_maps):
                print(index, map["title"])
        elif resp == "2":
            print("explore game")
        elif resp == "3":
            play(episode_maps)
        elif resp == "q" or resp == "quit":
            break
        else:
            print("Unknown response")


def play(episode_maps):
    instructions = """
Choose a particular episode.
A line will be displayed on screen that was uttered by one of the main Friends.
You will guess which friend said it, and type their first name.
The game will tell you if your guess was correct or not.
Type quit at any time to quit playing.
"""
    print(instructions)
    while True:
        choice = input(f"Choose a number between 1 and {len(episode_maps)} --> ")
        if choice.lower() == "quit":
            return
        if choice.isnumeric():
            choice = int(choice)-1
            break
        else:
            print("Please enter a valid number")
    episode_map = episode_maps[choice]
    print(f"{episode_map['title']}")
    while True:
        char = random.choice(chars)
        lines = episode_map[char]
        print(random.choice(lines))
        resp = input("Who said it? --> ")
        if resp == char:
            print("You got it!!")
        else:
            print(f"Nope. It was {char}")
        if resp.lower() == "quit":
            return


def run():
    episode_maps = setup()
    print("Welcome to 'Name That Friend'")
    menu(episode_maps)
    print("Thanks for playing!")


if __name__ == "__main__":
    run()
