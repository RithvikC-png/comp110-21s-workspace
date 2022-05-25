"""Trying to create a virtual DFA system"""

# 5-Tuple Collection

states = []
alphabet = []
start_state = ""
accepted_states = ""
transition = {}
active_state = ""


# Collecting the 5-tuple
def start() -> None:
    print("Enter the states of the DFA spearated by spaces: ", end = "")
    states = input().split()

    print("Enter the alphabet for the DFA separated by spaces: ", end = "")
    alphabet = input().split()

    print("Enter the next state for each transition")
    for state in states:
        for char in alphabet:
            print(f"\t{state}\t {char} --->\t", end = "")
            dest = input()

            transition[(state, char)] = dest

    print("Enter the start state of the DFA: ", end = "")
    start_state = input()

    print("Enter the accept states of the DFA separated by spaces: ", end = "")
    accepted_states = input().split()


    def transition_function(a) -> None:
        active_state = start_state
        amount = 0

        for char in a:
            active_state = transition[(active_state, char)]

        for state in accepted_states:
            if (active_state in state):
                print("Accepted")
            else:
                print("Rejected")
            
# Taking in the input string of transitions
    def input_string() -> None:
        print("Enter the input string to run the DFA, if you want to make a new DFA type EXIT: ", end = "")
        transition_input = input()
        if(transition_input == "EXIT"):
            start()
        transition_function(transition_input)
        input_string()

    input_string()

start()