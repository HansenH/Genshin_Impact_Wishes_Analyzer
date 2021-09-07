
from sqlalchemy import create_engine
import pandas as pd
# import json


class DataBase():
    def __init__(self):
        self.username = "hyf"
        self.password = "dNcRod87283,"
        self.host = "localhost"
        url = "mysql+pymysql://{}:{}@{}/genshine_impact_wishes".format(
            self.username, self.password, self.host
        )
        self.engine = create_engine(url)

    def append(self, table: str):
        def append_to_table(df: pd.DataFrame):
            df.to_sql(table, con=self.engine, if_exists='append')
        return append_to_table
