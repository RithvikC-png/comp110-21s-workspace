"""Tar Heels exercise redux as a structured program."""

__author__ = "730398645"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    unc: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
print(tar_heels(unc))

# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(unc: int) -> str:

    a = int(input("Enter a number "))

    if (a % 2) == 0 and (a % 7) == 0:
        print("TAR HEELS")
    elif (a % 2) == 0:
        print("TAR")
    elif (a % 7) == 0:
        print("HEELS")
    else:
        print("CAROLINA")

if __name__ == "__main__":
    main()
