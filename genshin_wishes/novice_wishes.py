from .wishes_base import WishesBase


class NoviceWishes(WishesBase):
    def init_params(self):
        self.params['gacha_type'] = '100'
        self.file_name = 'genshine_novice_wishes.csv'

    def to_remote_storage(self):
        pass
