# 集合（set）
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(1)
s.remove(2)
print(s)

# 辞書型
dist = {"kona": "U", 12: "DEC"}
print(dist[12])

# 文字列は文字の配列なのでforで回せる
name = "Harry"
for c in name:
    print(c)

# 関数とimport


def times(num):
    from functions import square
    print(f"{num}の累乗結果: {square(num)}")


for i in range(5):
    times(i)

# OOP


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(2, 8)
print(p.x)
print(p.y)


print("================航空便を表すクラス")


class Flight():
    # キャパを与えるとともに作成するメソッド
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # flightに乗客を加える
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    # 搭乗可能かチェック
    def open_seats(self):
        return self.capacity > len(self.passengers)


flight = Flight(3)
people = ["kna", "sei", "ma", "naka"]
for person in people:
    if flight.add_passenger(person):
        print(f"{person}が搭乗しました。")
    else:
        print(f"{person} は制限オーバーのため搭乗できませんでした。")

print("================関数型プログラミング")


def announce(f):
    def wrapper():
        print(("Start Functions"))
        f()
        print(("End Functions"))
    return wrapper


@announce
def Hello():
    print('hello')


Hello()

print("================ラムダ関数")
people = [
    {"name": "kona", "Like": "Nogi"},
    {"name": "shota", "Like": "Nogi"},
    {"name": "ai", "Like": "Sakura"},
]

people.sort(key=lambda person: person["name"])
print(people)
