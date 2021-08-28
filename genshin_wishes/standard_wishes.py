
from wishes_base import WishesBase

class StandardWishes(WishesBase):
    def init_params(self):
        self.params['gacha_type'] = '200'
        self.file_name = 'genshine_standard_wishes.csv'

    def to_remote_storage(self):
        pass

