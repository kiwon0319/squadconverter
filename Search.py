import json

with open("Data/doll.json") as data_file:
    data = json.load(data_file)

class ById:
    def __init__(self, _id):
        self.id = _id
        self.denied = True

        with open("Data/doll.json") as self.data_file:
            self.data = json.load(self.data_file)

    def search(self):

        for i in range(0,len(self.data)):
            if data[i]["id"] == self.id:
                _codename = self.data[i]["codename"]
                _type = self.data[i]["type"]
                _rank = self.data[i]["rank"]
                _buidTime = self.data[i]["buildTime"]
                self.denied = False

        if self.denied:
            print("아직 데이터가 업데이트되지 않은인형입니다.")
            return 0

        else:
            return (self.id, _codename, _type, _rank, _buidTime)

class ByCodeName:
    def __init__(self, _name):
        self.name = _name
        self.denied = True

    def search(self):
        for i in range(0,len(data)):
            if data[i]["codename"] == self.name:
                _id = data[i]["id"]
                self.denied = False

        if self.denied:
            return -1
        else:
            return ById(_id).search()

class ByBuildTime:
    def __init__(self, _sec):
        self.sec = _sec
        self.denied = True

    def get(self):
        self.id_list = [data[n]["id"] for n in range(0, len(data)) if data[n]["buildTime"] == self.sec]# if문 뒤에 and연산자로 id가 제조제외리스트에 포함되지 않을 때 추가예정

        if self.id_list == []:
            return 0
        else:
            return self.id_list
