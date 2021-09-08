
from sqlalchemy import create_engine
import pandas as pd
import json


class DataBase():
    def __init__(self):
        with open("data/config.json") as f:
            config = json.load(f)
        self.username = config['username']
        self.password = config['password']
        self.host = config['host']
        url = "mysql+pymysql://{}:{}@{}/genshine_impact_wishes".format(
            self.username, self.password, self.host
        )
        self.engine = create_engine(url)

    def append(self, table: str, source: str = "df"):
        if source not in ["df", "csv"]:
            raise RuntimeError("Unknown data source.")

        def append_from_dataframe(df: pd.DataFrame):
            df.to_sql(table, con=self.engine, if_exists='append', index=False)

        def append_from_csv(file: str):
            df = pd.read_csv(file)
            append_from_dataframe(df)

        return append_from_dataframe if source == "df" else append_from_csv
