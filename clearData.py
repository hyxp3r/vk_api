import time

class ClearUsersMeta:

    def clear(usersInfo):
        
        usersMeta = {}
        for k, v in usersInfo.items():

            print(k)

            usersMeta[k] = []

            for resp in v:
                
                for key, _value in resp.items():

                    for value in _value:


                        inside_dict = {}

                        inside_dict.update( {"ID":value["id"]})
                    
                        try:
                            inside_dict.update({"Фамилия":value["last_name"]})
                        except:
                            inside_dict.update({"Фамилия":""})
                        try:
                            inside_dict.update({"Имя":value["first_name"]})
                        except:
                            inside_dict.update({"Имя":""})
                        try:
                            inside_dict.update({"Домен": value["domain"]})
                        except:
                            inside_dict.update({"Домен": ""})
                        try:
                            inside_dict.update({"Дата рождения": value["bdate"]})
                        except:
                            inside_dict.update({"Дата рождения": ""})
                        try:
                            inside_dict.update({"Страна": value["country"]["title"]})
                        except:
                            inside_dict.update({"Страна": ""})
                        try:
                            inside_dict.update({"Город": value["city"]["title"]})
                        except:
                            inside_dict.update({"Город": ""})
                        try:
                            inside_dict.update({"Родной город": value["home_town"]})
                        except:
                            inside_dict.update({"Родной город": ""})
                        try:
                            inside_dict.update({"Часовой пояс": value["timezone"]})
                        except:
                            inside_dict.update({"Часовой пояс": ""})
                        try:
                            inside_dict.update({"Аватарка": value["photo_200"]})
                        except:
                            inside_dict.update({"Аватарка": ""})
                        try:
                            inside_dict.update({"Есть аватарка?": "Да" if value["has_photo"] == 1 else "Нет"})
                        except:
                            inside_dict.update({"Есть аватарка?": ""})
                        try:
                            inside_dict.update({"Входит с мобильного устройства?": "Да" if value["has_mobile"] == 1 else "Нет"})
                        except:
                            inside_dict.update({"Входит с мобильного устройства?": ""})
                        try:
                            inside_dict.update({"Можно приглашать в группы?": "Да" if value["can_be_invited_group"] == 1 else "Нет"})
                        except:
                            inside_dict.update({"Можно приглашать в группы?": ""})
                        try:
                            inside_dict.update({"Номер телефона": value["mobile_phone"]})
                        except:
                            inside_dict.update({"Номер телефона": ""})
                        try:
                            inside_dict.update({"Сайт/другая соц. сеть": value["site"]})
                        except:
                            inside_dict.update({"Сайт/другая соц. сеть": ""})
                        try:
                            inside_dict.update({"Статус": value["status"]})
                        except:
                            inside_dict.update({"Статус": ""})
                        try:
                            inside_dict.update({"Заходил в сеть": time.strftime('%H:%M:%S', time.gmtime(value["last_seen"]["time"]))})
                        except:
                            inside_dict.update({"Заходил в сеть": ""})
                        try:
                            inside_dict.update({"Работа": value["occupation"]["name"]})
                        except:
                            inside_dict.update({"Работа": ""})
                        try:
                            inside_dict.update({"Университет": value["university_name"]})
                        except:
                            inside_dict.update({"Университет": ""})
                        try:
                            inside_dict.update({"Факультет": value["faculty_name"]})
                        except:
                            inside_dict.update({"Факультет": ""})
                        try:
                            inside_dict.update({"Школа": value["schools"][0]["name"]})
                        except:
                            inside_dict.update({"Школа": ""})
                        try:
                            inside_dict.update({"Тип школы": value["schools"][0]["type_str"]})
                        except:
                            inside_dict.update({"Тип школы": ""})
                        try:
                            inside_dict.update({"Год начала обучения в школе": value["schools"][0]["year_from"]})
                        except:
                            inside_dict.update({"Год начала обучения в школе": ""})
                            
                        try:
                            inside_dict.update({"Год завершения обучения в школе": value["schools"][0]["year_to"]})
                        except:
                            inside_dict.update({"Год завершения обучения в школе": ""})
                        
                        try:
                            inside_dict.update({"Открытый профиль?": "Да" if value["is_closed"] == False else "Нет"})
                        except:
                            inside_dict.update({"Открытый профиль?": ""})  

                        usersMeta[k].append(inside_dict)

        return usersMeta