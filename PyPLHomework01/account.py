class Account:
    def __init__(self, myId, name, money):
        self.accId = myId
        self.cusName = name
        self.balance = money

    def getId(self):
        return self.accId

    def getName(self):
        return self.cusName

    def getBalance(self):
        return self.balance

    def deposit(self, money):
        self.balance -= money

    def withdrawal(self, money):
        self.balance += money


def showMenu():
    print("-----Menu-----\n1. 계좌개설\n2. 입금\n3. 출금\n4. 전체 고객 조회\n5. 종료\n\n")


def openAcc(accList, accNum):
    print("[계좌 개설]\n")

    myId = input("id: ")
    name = input("이름: ")
    money = input("입금액: ")

    accList[accNum] = Account(myId, name, money)

    return accList[accNum]


def depositAcc(accList, accNum):
    print("[입금]\n")
    myId = input("id: ")
    money = input("입금액: ")

    for i in range(accNum):
        if accList[i].getId() == myId:
            accList[i].deposit(money)
            print("입금 완료\n")
            return
        
    print("없는 ID\n")


def withdrawalAcc(accList, accNum):
    print("[출금]\n")
    myId = input("id: ")
    money = input("입금액: ")

    for i in range(accNum):
        if accList[i].getId() == myId:
            accList[i].withdrawal(money)
            print("출금 완료\n")
            return

    print("없는 ID\n")


def showAllAcc(accList, accNum):
    print("전체 고객 조회\n")
    for i in range(accNum):
        print("사용자 id: ", accList[i].getId())
        print("\n사용자 이름: ", accList[i].getName())
        print("\n잔액: ", accList[i].getBalance(), "\n\n")


if __name__ == "__main__":
    pass
