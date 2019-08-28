import json
import math

import Search

with open("Data/doll.json") as data_file:
    data = json.load(data_file)

def getFavorRatio(favor):
    if favor < 10:
        return -0.05
    elif favor < 90:
        return 0
    elif favor < 140:
        return 0.05
    elif favor < 190:
        return 0.1
    else:
        return 0.15

class SearchBaseStat:
    def __init__(self, _id):
        self.id = _id
        for i in range (0, len(data)):
            if self.id == data[i]["id"]:
                self.stat_dict = data[i]["stats"]

                self.grow = data[i]["grow"] #성장 가중치

    def get(self):
        return self.stat_dict

class GridEffect:
    def __init__ (self, _id):
        self.id = _id
    def get(self):
        for i in range(0, len(data)):
            if data[i]["id"] == self.id:
                return data[i]["effect"]
        return -1

class CalcStat:
    def __init__(self,_id, _level):
        self.id = _id
        self.level = _level
        self.type = Search.ById(self.id).search()[2]

    def calc(self):

        with open("Data/dollAttribute.json") as attribute_file:
            attribute = json.load(attribute_file)

        with open("Data/dollGrow.json") as grow_file:
            grow = json.load(grow_file)

        stats = SearchBaseStat(self.id).get()
        growRatio = SearchBaseStat(self.id).grow

        if self.level <= 100:
            basicStats = grow["normal"]["basic"]
            growStats = grow["normal"]["grow"]
        else:
            basicStats =grow["normal"]["basic"]
            growStats =grow["normal"]["grow"]

            basicStats.update(grow["after100"]["basic"])
            growStats.update(grow["after100"]["grow"])

        newStat = stats.copy()

        #기초스탯 생성
        for key in basicStats.keys():
            try:
                newStat[key] = math.ceil((basicStats[key][0] + ((self.level - 1) * basicStats[key][1])) * attribute[self.type][key] * stats[key] / 100) if len(basicStats[key]) > 1 else math.ceil(basicStats[key][0] * attribute[self.type][key] * stats[key] / 100)
                #print(f"{key} : {newStat[key]}")
            except:
                pass

        #강화스탯 생성
        for key in growStats.keys():
            try:
                newStat[key] += math.ceil(growStats[key][1] + ((self.level - 1) * growStats[key][0]) * attribute[self.type][key] * stats[key] * growRatio / 100 / 100)
            except:
                pass

        return newStat