class TransactionStructure:
    def __init__(self,init,trans,fv):
        self.initial = init
        self.transaction = trans
        self.finalValue = fv

    def getInitial(self):
        return self.initial

    def setInitial(self,init):
        self.initial=init

    def getTransaction(self):
        return self.transaction

    def setTransaction(self,trans):
        self.transaction = trans

    def getFinalValue(self):
        return self.finalValue

    def setFinalValue(self,fv):
        self.finalValue=fv

    def __str__(self):
        return '{' + self.initial + ", " + self.transaction + ", " + self.finalValue + '}'
