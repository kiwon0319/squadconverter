import json
from tkinter import filedialog, Tk

import CalcStat
import pathlib
import json

class load:
    def __init__(self,path):
        try:
            with open (path) as data_file:
                self.data = json.load(data_file)
        except FileNotFoundError as e:
            print("파일을 찾을 수 없습니다.")
            exit()

        for key in self.data:
            if key == "BossHP":
                continue
            if key == "enemyGroupID":
                continue

            id = self.data [key] ["gun_id"]
            lv = self.data [key] ["gun_level"]

            stat = CalcStat.CalcStat(int(id), int(lv)).calc()

            self.data[key]["life"] = stat["hp"] * int(self.data[key]["number"])
            self.data[key]["pow"] = stat["pow"]
            self.data[key]["hit"] = stat["hit"]
            self.data[key]["dodge"] = stat["dodge"]
            self.data[key]["rate"] = stat["rate"]
    def get(self):
        return self.data


def data_to_json(data) :
    if type(data) is str : # 타입이 문자열이라면
        return '"' + data + '"' # 문자열을 "로 묶어주고
    elif type(data) is list : # 타입이 리스트라면
        return list_to_json(data, data_to_json) # 함수 호출
    elif type(data) is int or type(data) is float : # 타입이 숫자라면
        return data.__str__() # 그대로 반환
    elif type(data) is dict : # 타입이 dict라면
        return dict_to_json(data, data_to_json) # 함수 호출
    else :
        print("type은 {}".format(type(data)))
        return '""'

def list_to_json(list, func):
    out_str = "[\n" # [(대괄호)를 연다
    for val in list:
        out_str += func(val)
        out_str += ", " # ,(쉼표)로 데이터를 구분

    if len(out_str) > 2:
        out_str = out_str[:-2]

    out_str += "]\n" # ](대괄호)를 닫는다
    return out_str

def dict_to_json(dict, func) :
    out_str = "{\n" # {(중괄호)를 연다
    for key in dict.keys() :
        out_str += ('"' + key.__str__() + '"') # 키 값에 "(큰 따옴표)를 씌운다
        out_str += ": " # :(콜론)으로 Key와 Value를 분리
        out_str += func(dict[key])
        out_str += ", " # ,(쉼표)로 쌍과 쌍을 분리
    if len(out_str) > 2:
        out_str = out_str[:-2]

    out_str += "}\n" # }(중괄호)를 닫는다
    return out_str

class save:
    def __init__(self,a):
        root = Tk().withdraw
        file = filedialog.asksaveasfile(mode='w', defaultextension=".gun")
        print(a)
        json_data = json.dumps(a)

        print(json_data)
        if file:
            file.write(json_data)
            file.close()
        print("Done!")