import csv
import random


with open('krx.csv', newline='') as f:
    reader = csv.reader(f)
    stock3m = []
    for line in reader:
        code = line[0]  # 종목코드
        name = line[1]  # 종목명
        market = line[2]  # 시장구분
        flct = line[6]  # 등락률
        stock = [code, name, market, flct]

        print(stock)
        stock3m.append(stock)

    print("종목 3개 랜덤: ")
    print(random.sample(stock3m, 3))  # stock3m 리스트에 있는 것중 3개 리스트 형식으로 반환중복 없음

    f.close()
