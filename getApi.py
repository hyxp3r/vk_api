from connect import Connection
import requests
from time import sleep






class GetUsers(Connection):

    def __init__(self, method: str) -> None:
        super().__init__(method)

    def getUsers(self, groups:list) -> dict:


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

                params = {
                "access_token": self.api_key,
                "v": self.v,
                "group_id": group,
                "offset": offset
                }
        
                
                r = requests.get(url = self.url, params=params).json()
                
                for item in r["response"]["items"]:
                    users[group].append(item)
                
                sleep(0.5)
                offset +=1000
            
            
        return users

class GetUserMeta(Connection):

        def __init__(self, method: str) -> None:
            super().__init__(method)

        def getMeta(self, users:dict)->dict:

            usersMeta = {}
 
        
            for k, v in users.items():

                usersMeta[k] = []

                print(k)

                for item in v:

                    raspak = ','.join([str(x) for  x in item])
                    
                    params = {
                        "access_token": self.api_key,
                        "v": self.v,
                        "user_ids":f"{raspak}",
                        "fields": """activities, about, bdate, can_be_invited_group, career, common_count, connections, 
                        contacts, city, country, domain, education, exports, followers_count, friend_status, has_photo, has_mobile, home_town, photo_200, photo_200_orig, sex, site, schools, screen_name, status, verified,  is_favorite, is_hidden_from_feed, last_seen, maiden_name,  nickname, occupation, 
                        personal, photo_id, photo_max, quotes, relation, timezone, tv, universities"""
                        }
                    try:           
                        r = requests.get(url = self.url, params=params).json()
                        usersMeta[k].append(r)
                    except:
                        n = 0
                        while n!=5:
                            try:
                                sleep(1)
                                r = requests.get(url = self.url, params=params, verify=False).json()
                                usersMeta[k].append(r)
                                n = 5
                            except:
                                n+=1
                                print(n)

 
                    sleep(0.5)

            return usersMeta