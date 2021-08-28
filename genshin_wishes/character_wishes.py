from wishes_base import WishesBase

class CharacterWishes(WishesBase):
    def init_params(self):
        self.params['gacha_type'] = '301'
        self.file_name = 'genshine_character_wishes.csv'

    def to_remote_storage(self):
        pass

