import pandas as pd

class ConvertToDF:

    def __init__(self, usersMetaClear:dict) -> None:
        self.usersMetaClear = usersMetaClear
        self.df = pd.DataFrame()


    def convert(self):

        for k, v in self.usersMetaClear.items():
            if self.df.empty:
                self.df = pd.DataFrame(v)
                self.df["Группа в ВК"]  = k
            else:
                df_2 = pd.DataFrame(v)
                df_2["Группа в ВК"]  = k
                self.df = pd.concat([self.df, df_2], axis=0)

        self.df = self.df.drop_duplicates(subset=["ID"])

        return self.df