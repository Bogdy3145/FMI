class FA:

    def __init__(self, filepath):
        self.states = []
        self.alphas = []
        self.initialState = ''
        self.finalStates = []
        self.transactions = []
        self.transactioNGraph = {}
        self.filePath = filepath

        self.readFromFile()

    def readFromFile(self):
        try:
            with open(self.filePath, 'r') as file:
                lines = file.readlines()

                # Read initial state
                self.initialState = lines[0].strip()

                # Read final states
                self.finalStates = lines[1].strip().split()

                # Read alphas
                self.alphas = lines[2].strip().split()

                # Read all states
                self.states = lines[3].strip().split()

                # Read transactions
                self.transactions = [tuple(line.strip().split()) for line in lines[4:]]
        except IOError as e:
            print(e)

    def displayStates(self):
        print(self.states)

    def displayInitialState(self):
        print(self.initialState)

    def displayFinalState(self):
        print(self.finalStates)

    def displayAlphas(self):
        print(self.alphas)

    def displayTransaction(self):
        print(self.transactions)


    #Checking if the string s is a sequence of valid transactions or not
    def check(self, s):
        current_state = self.initialState

        for c in s:
            transition_found = False
            for transition in self.transactions:
                source_state, destination_state, symbol = transition
                if source_state == current_state and symbol == c:
                    current_state = destination_state
                    transition_found = True
                    break

            if not transition_found:
                return False

        return current_state in self.finalStates


