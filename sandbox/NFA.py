"""Trying to create a virtual NFA system"""

def start() -> None:
    # 5-Tuple Collection

    states = []
    alphabet = []
    start_state = ""
    accepted_states = ""
    transition = {}
    nfa_transition = {}

    # Collecting the 5-tuple
    print("Enter the states of the NFA spearated by spaces: ", end = "")
    states = input().split()

    print("Enter the alphabet for the NFA separated by spaces: ", end = "")
    alphabet = input().split()
    alphabet.append("EPSILON")

    print("Enter the start state of the NFA: ", end = "")
    start_state = input()

    print("Enter the accept states of the NFA separated by spaces: ", end = "")
    accepted_states = input().split()
    

    def transition_function(transition, input, accept, active, i) -> None:
        amount = 0

        for j in range(len(input)):
            for char in input:
            #   Checking each possibile transition, not sure about time complexity but shouldn't exceed n^2
                for each in transition[active][char]:
                    if(each < len(transition)):
                        active = each
                        if(j == len(input) - 1):
                            for state in accept:
                                if(active == state):
                                    amount += 1
                        transition_function(transition, input[i+1:], accept, active, i)
                i += 1

        if(amount > 0):
            print("Accepted")
        else:
            print("Rejected")
            
# Taking in the input string of transitions
    def input_string() -> None:
        print("Enter the input string to run the NFA, if you want to make a new NFA type EXIT: ", end = "")
        transition_input = input()
        if(transition_input == "EXIT"):
            start()
        i = 0
        transition_function(transition, transition_input, accepted_states, start_state, i)
        input_string()


    def check_doubles(transition) -> None:
        for transition in transition:
            for tran in transition:
                # if(transition[k] == tran[k]):
                print(transition)
                print(trans)

# Moving transition collection to bring input_string into its scope
    while(len(transition) < len(states) * len(alphabet)):
        print("Enter the transition, type LEAVE if you are done entering transitions(origin, transition, destination): ", end = "")
        temp = input()
        trans = temp.split()
        if(temp == "LEAVE"):
            input_string()
            check_doubles(transition)
        else:
            transition[trans[0], trans[1]] = trans[2]
            print(transition)

    input_string()

start()