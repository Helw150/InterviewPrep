class PurchaseHashEntry:
    def __init__(self, location, time):
        self.time = time
        self.location = location
def StringSplitter(LogFile):
    LogFile = list(LogFile)
    for i, char in enumerate(LogFile):
        if char == ' ':
            if not list(LogFile)[i-1].isnumeric():
                LogFile[i] = ''
    Purchases = ''.join(LogFile)
    Purchases = Purchases.split(' ')
    for i, Purchase in enumerate(Purchases):
        Purchases[i] = Purchase.split("|")
    return Purchases
def CheckForFraud(Purchases):
    PurchaseHash = {}
    Criminals = []
    for Purchase in Purchases:
        FraudFound = False
        if int(Purchase[1]) > 3000:
            print(Purchase[1])
            FraudFound = True
        if Purchase[0] in PurchaseHash:
            if Purchase[2] != PurchaseHash[Purchase[0]].location:
                if int(Purchase[3]) - int(PurchaseHash[Purchase[0]].time) > 60:
                    FraudFound = True
        PurchaseHash[Purchase[0]] = PurchaseHashEntry(Purchase[2], Purchase[3])
        if FraudFound == True:
            if not Purchase[0] in Criminals:
                print(Purchase)
                Criminals.append(Purchase[0])
    return Criminals
def main():
    LogFile = input()
    Purchases = StringSplitter(LogFile)
    Criminals = CheckForFraud(Purchases)
    print(Criminals)

main()
