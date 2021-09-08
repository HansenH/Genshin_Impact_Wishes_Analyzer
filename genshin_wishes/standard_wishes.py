
from .wishes_base import WishesBase


class StandardWishes(WishesBase):
    def init_params(self):
        self.params['gacha_type'] = '200'
        self.file_name = 'genshine_standard_wishes.csv'
        self.rst_file_name = 'standard_analysis.txt'
        self.table = 'standard_wishes'
