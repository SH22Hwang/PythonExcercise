from account import *


def main():
    accList = []
    accNum = 0
    while True:
        showMenu()
        choice = input("선택: ")

        if choice == 1:
            accList.append(openAcc(accList, accNum))
            accNum += 1
        elif choice == 2:
            depositAcc(accList, accNum)
        elif choice == 3:
            withdrawalAcc(accList, accNum)
        elif choice == 4:
            showAllAcc(accList, accNum)
            return
        else:
            print("범위에서 벗어난 값!")


if __name__ == "__main__":
    main()
