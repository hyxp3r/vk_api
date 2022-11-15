import pandas as pd


class GetList:

    def __init__(self, csv:str) -> None:
        self.groups = pd.read_csv(csv)

    def makeList(self) -> list:
            list = pd.DataFrame(data = self.groups)["groups"].to_list()
            return list

class DevideList:

    def __init__(self, list:list, n:int) -> None:
         self.list = list
         self.n = n


    def divide(self )->GeneratorExit:

        for i in range(0, len(self.list), self.n):
            yield self.list[i : i + self.n]