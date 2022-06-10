from automata.pda.npda import NPDA

# 5-Tuple Collection

states = []
alphabet = []
stack_alphabet = []
start_state = ""
accepted_states = ""
transition = {}
inp = ""

def start() -> None:

    # Collecting the 5-tuple
    print("Enter the states of the PDA spearated by spaces: ", end = "")
    states = input().split()

    print("Enter the input alphabet for the PDA separated by spaces: ", end = "")
    alphabet = input().split()
    alphabet.append("ep")

    print("Enter the stack alphabet for the PDA separated by spaces: ", end = "")
    stack_alphabet = input().split()

    print("Enter the start state of the PDA: ", end = "")
    start_state = input()

    print("Enter the accept states of the PDA separated by spaces: ", end = "")
    accepted_states = input().split()
    
            
# Taking in the input string of transitions
    def input_string() -> None:
        print("Enter the input string to run the PDA, if you want to make a new PDA type EXIT: ", end = "")
        transition_input = input()
        inp = transition_input
        if(transition_input == "EXIT"):
            start()
        elif npda.accepts_input(inp):
            print("accepted")
        else:
            print("rejected")
        input_string()


# Moving transition collection to bring input_string into its scope
    while(len(transition) < len(states) * len(alphabet) * len(stack_alphabet)):
        print("Enter the transition, type LEAVE if you are done entering transitions(origin, input string, pop, destination, push)(epsilon = ''): ", end = "")
        temp = input()
        trans = temp.split()
        if(temp == "LEAVE"):
            input_string()
        else:
            trn = {}
            t = {}
            trn[trans[2]] = [trans[3], trans[4]]
            t[trans[1]] = trn
            transition[trans[0]] = t

    input_string()

    npda = NPDA(
        states=states,
        input_symbols=alphabet,
        stack_symbols=stack_alphabet,
        transitions=transition,
        initial_state=start_state,
        initial_stack_symbol='',
        final_states=accepted_states,
        acceptance_mode='final_state'
    )

    npda.read_input_stepwise

start()