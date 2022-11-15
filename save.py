import json
import pandas as pd

class SaveJson:
    def __init__(self, path:str, file:dict) -> None:
        self.path = path 
        self.file = file

    def save(self):

        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.file, f, ensure_ascii=False, indent=4)

class SaveExcel:

    def __init__(self, path:str, df:object) -> None:
        self.path = path
        self.df = df

    def save(self):


        writer = pd.ExcelWriter(self.path,
                        engine='xlsxwriter',
                        engine_kwargs={'options': {'strings_to_urls': False}})
        self.df.to_excel(writer, index = False)

        writer.close()