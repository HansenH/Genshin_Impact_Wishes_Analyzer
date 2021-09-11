
from sqlalchemy import create_engine, desc
import pandas as pd
import json
from .mapped_classes import \
    CharacterWishes, NoviceWishes, WeaponWishes, StandardWishes
from sqlalchemy.orm import sessionmaker

model_map = {
    "character_wishes": CharacterWishes,
    "novice_wishes": NoviceWishes,
    "weapon_wishes": WeaponWishes,
    "standard_wishes": StandardWishes
}


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
        self.Session = sessionmaker(bind=self.engine)

    def __get_max_timestamp(self, table: str):
        session = self.Session()
        model = model_map[table]
        lastest_time = session.query(model.time) \
            .order_by(desc(model.id)) \
            .first()
        session.close()
        return lastest_time if lastest_time is None else lastest_time[0]

    def append(self, table: str, source: str = "df"):
        if source not in ["df", "csv"]:
            raise RuntimeError("Unknown data source.")

        def append_from_dataframe(df: pd.DataFrame):
            lastest_time = self.__get_max_timestamp(table=table)
            # to make sure no extra rows are appended
            if lastest_time is not None:
                df = df[df.time > lastest_time.strftime("%Y-%m-%d %H:%M:%S")]
            df.to_sql(table, con=self.engine, if_exists='append', index=False)

        def append_from_csv(file: str):
            df = pd.read_csv(file)
            append_from_dataframe(df)

        return append_from_dataframe if source == "df" else append_from_csv
