import requests
import pandas as pd
from dotenv import load_dotenv
import os
from time import sleep
import time
from save import SaveJson, SaveExcel
from getApi import GetUserMeta, GetUsers
from lists import GetList, DevideList
from clearData import ClearUsersMeta
from converData import ConvertToDF






groups = GetList("groups copy.csv").makeList()

users = GetUsers("groups.getMembers").getUsers(groups)

save_users = SaveJson("data_users.json", users).save()

for k, v in users.items():

    dividedList = list(DevideList(v, 1000).divide())
    users[k] = dividedList
  
usersMeta= GetUserMeta("users.get").getMeta(users)

usersMetaClean = ClearUsersMeta.clear(usersMeta)

save_users_meta = SaveJson("users_meta.json", usersMetaClean).save()

df = ConvertToDF(usersMetaClean).convert()


save_excel = SaveExcel("itog_main.xlsx", df).save()



