"""Tar Heels exercise redux as a structured program."""

__author__ = "730398645"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    unc: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(unc))

# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(unc: int) -> str:
    """Tar Heel pride"""
    unc = unc

    if (unc % 2) == 0 and (unc % 7) == 0:
        return("TAR HEELS")
    elif (unc % 2) == 0:
        return("TAR")
    elif (unc % 7) == 0:
        return("HEELS")
    else:
        return("CAROLINA")


if __name__ == "__main__":
    main()
