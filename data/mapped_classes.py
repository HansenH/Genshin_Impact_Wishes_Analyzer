from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP


Base = declarative_base()


class CharacterWishes(Base):
    __tablename__ = 'character_wishes'

    id = Column(Integer, primary_key=True)
    item_type = Column(String)
    name = Column(String)
    rank_type = Column(Integer)
    time = Column(TIMESTAMP)

    def __repr__(self):
        return "<CharacterWish(name='%s', type='%s', rank='%s', time='%s')>" % (
            self.name, self.item_type, self.rank_type, self.time
        )


class NoviceWishes(Base):
    __tablename__ = 'novice_wishes'

    id = Column(Integer, primary_key=True)
    item_type = Column(String)
    name = Column(String)
    rank_type = Column(Integer)
    time = Column(TIMESTAMP)

    def __repr__(self):
        return "<NoviceWish(name='%s', type='%s', rank='%s', time='%s')>" % (
            self.name, self.item_type, self.rank_type, self.time
        )


class StandardWishes(Base):
    __tablename__ = 'standard_wishes'

    id = Column(Integer, primary_key=True)
    item_type = Column(String)
    name = Column(String)
    rank_type = Column(Integer)
    time = Column(TIMESTAMP)

    def __repr__(self):
        return "<StandardWish(name='%s', type='%s', rank='%s', time='%s')>" % (
            self.name, self.item_type, self.rank_type, self.time
        )


class WeaponWishes(Base):
    __tablename__ = 'weapon_wishes'

    id = Column(Integer, primary_key=True)
    item_type = Column(String)
    name = Column(String)
    rank_type = Column(Integer)
    time = Column(TIMESTAMP)

    def __repr__(self):
        return "<WeaponWish(name='%s', type='%s', rank='%s', time='%s')>" % (
            self.name, self.item_type, self.rank_type, self.time
        )
