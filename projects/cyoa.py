"""My first attempt at a project from scratch!"""

from random import randint

__author__ = "730398645"

player: str = " "

points: int = 0


def main() -> None:
    """The starting place for the user."""
    score = 0

    greet()

    h: int = int(input("What do you wanna do? \n 1) Guess the number \n 2) How many points \n 3) Exit \n"))

    if h == 1:
        guess_number()
    elif h == 2:
        how_many_points(score)
    elif h == 3:
        duke_sucks = (input("Do you think Duke sucks? yes/no \n"))
        if(duke_sucks == "yes" or duke_sucks == "YES" or duke_sucks == "Yes"):
            print(f"Excellent answer, have a nice day {player}! ")
        else:
            print(f"Bye! We won't miss you {player} ")


def greet() -> None:
    """A way to greet the player."""
    print("Hi there! ")
    global player
    player = input("What is your name? ")

    print(f"Welcome to the game {player}! ")
    

def guess_number() -> None:
    """Asking the player to guess."""
    print(f"{player}, Guess a number from 1 to 7, if you're right, you get points, get 5 wrong in a row, you lose ")
    health = 5
    global points
    points = points

    while health > 0:
        rand = randint(1, 7)
        guess = int(input("Guess a number "))
        if guess == rand:
            print("Well done you got it right ")
            points = points + 1
            health = int(5)
        else:
            print("You got it wrong ")
            health = health - 1
    else:
        print(f"Game over {player} better luck next time \n You scored {points} points")
        play_again = input("Would you like to go back to the start? yes/no \n ")
        if (play_again == "yes" or play_again == "YES" or play_again == "Yes"):
            main()
        else:
            print(f"Thank you for stopping by {player}! ")


def how_many_points(score: int) -> int:
    """A game to see how many points you can score in the March Madness Finals for Carolina!"""
    print(f"Hey {player}! The finals of March Madness is about to start. UNC needs you!")
    score = 0
    shots_left: int = 7
    celebrate: str = "\U0001f389"

    while (shots_left > 0):
        shoot = (input("would you like to shoot? yes/no \n "))
        if(shoot == "yes" or shoot == "Yes" or shoot == "YES"):
            odds = randint(1, 3)
            if (odds > 2):
                print(f"Excellent work {player}! You scored 3 points! ")
                score += 3
                shots_left -= 1
            elif (odds > 1):
                print(f"Great job {player}! You scored 2 points! ")
                score += 2
                shots_left -= 1
            else:
                print("You missed your shot, maybe you'll make it next time! ")
                shots_left -= 1
        elif(shoot == "no" or shoot == "No" or shoot == "NO"):
            print(f"Roy is sad {player}, everyone hates you, you move to Sibera in shame and live with Polar Bears ")
            play_again = input("Would you like to go back to the start? yes/no \n")
            if (play_again == "yes" or play_again == "YES" or play_again == "Yes"):
                main()
            else:
                print(f"Thank you for stopping by {player}! ")
                break
        if shots_left == 0 and score > 12:
            print(f"Well done {player} you scored {score} points and won UNC its first title since 2017! {celebrate} ")
            play_again = input("Would you like to go back to the start? yes/no \n")
            if (play_again == "yes" or play_again == "YES" or play_again == "Yes"):
                main()
            else:
                print(f"Thank you for stopping by {player}! ")
        if shots_left == 0 and score < 13:
            print(f"You fought {player} valiantly and scored {score} points better luck next year! ")
            play_again = input("Would you like to go back to the start? yes/no \n")
            if (play_again == "yes" or play_again == "YES" or play_again == "Yes"):
                main()
            else:
                print(f"Thank you for stopping by {player}! ")
    return(score)


if __name__ == "__main__":
    main()