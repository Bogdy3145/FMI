from fa import FA

class Menu:
    def uiDisplayStates(self, fa):
        fa.displayStates()

    def uiDisplayAlphas(self, fa):
        fa.displayAlphas()

    def uiDisplayInitialState(self, fa):
        fa.displayInitialState()

    def uiDisplayFinalState(self, fa):
        fa.displayFinalState()

    def uiDisplayTransaction(self, fa):
        fa.displayTransaction()

    def uiCheck(self, fa, s):
        return fa.check(s)

    def displayMenu(self):
        print("Choose an option: \n")
        print("--1-- Display states.")
        print("--2-- Display alphas.")
        print("--3-- Display initial states.")
        print("--4-- Display final states.")
        print("--5-- Display transactions.")
        print("--6-- Enter transactions.")
        print("--0-- Exit.")
        print("\n")

    def run(self, fa):

        fa.readFromFile()

        self.displayMenu()

        while (True):
            opt = input("Option: ")

            if opt == "1":
                self.uiDisplayStates(fa)
            elif opt == "2":
                self.uiDisplayAlphas(fa)
            elif opt== "3":
                self.uiDisplayInitialState(fa)
            elif opt == "4":
                self.uiDisplayFinalState(fa)
            elif opt == "5":
                self.uiDisplayTransaction(fa)
            elif opt == "6":
                pass
            elif opt == "0":
                return
            else:
                print("Invalid option! Try again.")



