from .wishes_base import WishesBase


class NoviceWishes(WishesBase):
    def init_params(self):
        self.params['gacha_type'] = '100'
        self.file_name = 'genshine_novice_wishes.csv'
        self.rst_file_name = 'novice_analysis.txt'
        self.table = 'novice_wishes'
