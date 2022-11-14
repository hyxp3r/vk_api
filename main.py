import requests
import pandas as pd
from dotenv import load_dotenv
import os
import json
from time import sleep
import time
load_dotenv(".env")

class Connection():

    v = "5.131"

    def __init__(self, method:str) -> None:
        self.api_key = os.environ.get("api")
        self.url = f"https://api.vk.com/method/{method}"


class GetList:

    def __init__(self, csv:str) -> None:
        self.groups = pd.read_csv(csv)

    def makeList(self):
            list = pd.DataFrame(data = self.groups)["groups"].to_list()
            return list

class GetUsers(Connection):

    def __init__(self, method: str) -> None:
        super().__init__(method)

    def getUsers(self, groups:list):


        users = {}

        for group in groups:
            print(group)

            offset = 0
            users[group] = []

            params = {
                "access_token": self.api_key,
                "v": self.v,
                "group_id": group,
                "offset": offset
            }
            r = requests.get(url = self.url, params=params).json()

            pages = r["response"]["count"]//1000 + 1

            for page in range(pages):
                offset +=1000
                
                r = requests.get(url = self.url, params=params).json()
                
                for item in r["response"]["items"]:
                    users[group].append(item)
                print(page, offset)
                sleep(0.5)
            

            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(users, f, ensure_ascii=False, indent=4)
            
        return users

class getUserMeta(Connection):

        def __init__(self, method: str) -> None:
            super().__init__(method)

        def getMeta(self, users:dict):

            usersMeta = {}
 
        
            for k, v in users.items():
                usersMeta[k] = {}

                for user in v:

                    params = {
                    "access_token": self.api_key,
                    "v": self.v,
                    "user_ids":{user},
                    "fields": """activities, about, bdate, can_be_invited_group, career, common_count, connections, 
                    contacts, city, country, domain, education, exports, followers_count, friend_status, has_photo, has_mobile, home_town, photo_200, photo_200_orig, sex, site, schools, screen_name, status, verified,  is_favorite, is_hidden_from_feed, last_seen, maiden_name,  nickname, occupation, 
                    personal, photo_id, photo_max, quotes, relation, timezone, tv, universities"""
                    }
                    r = requests.get(url = self.url, params=params).json()
                    usersMeta[k].update( {r["response"][0]["id"]:{} })
                    print(usersMeta)
                    usersMeta[k][r["response"][0]["id"]].update({"Фамилия":r["response"][0]["last_name"]})
                    usersMeta[k][r["response"][0]["id"]].update({"Имя":r["response"][0]["first_name"]})
                    usersMeta[k][r["response"][0]["id"]].update({"Домен": r["response"][0]["domain"]})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Дата рождения": r["response"][0]["bdate"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Дата рождения": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Страна": r["response"][0]["country"]["title"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Страна": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Город": r["response"][0]["city"]["title"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Город": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Родной город": r["response"][0]["home_town"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Родной город": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Часовой пояс": r["response"][0]["timezone"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Часовой пояс": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Аватарка": r["response"][0]["photo_200"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Аватарка": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Есть аватарка?": "Да" if r["response"][0]["has_photo"] == 1 else "Нет"})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Есть аватарка?": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Входит с мобильного устройства?": "Да" if r["response"][0]["has_mobile"] == 1 else "Нет"})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Входит с мобильного устройства?": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Можно приглашать в группы?": "Да" if r["response"][0]["can_be_invited_group"] == 1 else "Нет"})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Можно приглашать в группы?": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Номер телефона": r["response"][0]["mobile_phone"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Номер телефона": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Сайт/другая соц. сеть": r["response"][0]["site"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Сайт/другая соц. сеть": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Статус": r["response"][0]["status"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Статус": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Заходил в сеть": time.strftime('%H:%M:%S', time.gmtime(r["response"][0]["last_seen"]["time"]))})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Заходил в сеть": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Работа": r["response"][0]["occupation"]["name"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Работа": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Университет": r["response"][0]["university_name"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Университет": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Факультет": r["response"][0]["faculty_name"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Факультет": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Школа": r["response"][0]["schools"][0]["name"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Школа": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Тип школы": r["response"][0]["schools"][0]["type_str"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Тип школы": ""})
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Год начала обучения в школе": r["response"][0]["schools"][0]["year_from"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Год начала обучения в школе": ""})
                        
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Год завершения обучения в школе": r["response"][0]["schools"][0]["year_to"]})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Год завершения обучения в школе": ""})
                    
                    try:
                        usersMeta[k][r["response"][0]["id"]].update({"Открытый профиль?": "Да" if r["response"][0]["is_closed"] == False else "Нет"})
                    except:
                        usersMeta[k][r["response"][0]["id"]].update({"Открытый профиль?": ""})


                        
                        

                    with open('user.json', 'w', encoding='utf-8') as f:
                        json.dump(usersMeta, f, ensure_ascii=False, indent=4)
                        print(usersMeta)
                    sleep(0.5)
                return usersMeta


class ToExcel:

    def __init__(self, usersMeta:dict) -> None:
        self.usersMeta = usersMeta


    def saveFile(self):

        data = pd.DataFrame.from_dict(self.usersMeta).reset_index()
        df = pd.concat({k: pd.Series(v) for k, v in data.items()}).reset_index()
        df_0 = df[0].to_dict()
        df_0 = pd.DataFrame.from_dict(df_0).T
        df = df.drop([0], axis=1)
        df = df.rename(columns = {"level_0": "Группа", "level_1":"ID"})
        df = pd.concat([df, df_0], axis=1)

        df.to_excel("result.xlsx")



groups = GetList("groups.csv").makeList()

users = GetUsers("groups.getMembers").getUsers(groups)

meta = getUserMeta("users.get").getMeta(users)

"""
with open('user.json', encoding="UTF-8") as f:
    d = json.load(f)
"""

saveFile = ToExcel(meta).saveFile()

