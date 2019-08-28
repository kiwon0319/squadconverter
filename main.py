import json
import CalcStat
import pathlib

try:
    with open ("modify/original.gun") as data_file:
        data = json.load(data_file);
except FileNotFoundError as e:
    print("original.gun파일을 찾을 수 없습니다.")
    exit()

id = data ["gun1"] ["gun_id"]
lv = data ["gun1"] ["gun_level"]

stat = CalcStat.CalcStat(int(id), int(lv)).calc()

data ["gun1"] ["life"] = stat ["hp"] * int (data["gun1"] ["number"])
data ["gun1"] ["pow"] = stat ["pow"]
data ["gun1"] ["hit"] = stat ["hit"]
data ["gun1"] ["dodge"] = stat ["dodge"]
data ["gun1"] ["rate"] = stat ["rate"]

data ["gun2"] ["life"] = stat ["hp"] * int (data["gun2"] ["number"])
data ["gun2"] ["pow"] = stat ["pow"]
data ["gun2"] ["hit"] = stat ["hit"]
data ["gun2"] ["dodge"] = stat ["dodge"]
data ["gun2"] ["rate"] = stat ["rate"]

data ["gun3"] ["life"] = stat ["hp"] * int (data["gun3"] ["number"])
data ["gun3"] ["pow"] = stat ["pow"]
data ["gun3"] ["hit"] = stat ["hit"]
data ["gun3"] ["dodge"] = stat ["dodge"]
data ["gun3"] ["rate"] = stat ["rate"]

data ["gun4"] ["life"] = stat ["hp"] * int (data["gun4"] ["number"])
data ["gun4"] ["pow"] = stat ["pow"]
data ["gun4"] ["hit"] = stat ["hit"]
data ["gun4"] ["dodge"] = stat ["dodge"]
data ["gun4"] ["rate"] = stat ["rate"]

data ["gun5"] ["life"] = stat ["hp"] * int (data["gun5"] ["number"])
data ["gun5"] ["pow"] = stat ["pow"]
data ["gun5"] ["hit"] = stat ["hit"]
data ["gun5"] ["dodge"] = stat ["dodge"]
data ["gun5"] ["rate"] = stat ["rate"]

print (data["gun1"])
print (data["gun2"])


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

file = pathlib.Path('result/result.gun')
file.write_text(dict_to_json(data, data_to_json), encoding='utf-8')

print("Done!")
