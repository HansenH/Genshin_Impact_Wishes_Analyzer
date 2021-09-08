from .wishes_base import WishesBase


class WeaponWishes(WishesBase):
    def init_params(self):
        self.params['gacha_type'] = '302'
        self.file_name = 'genshine_weapon_wishes.csv'
        self.rst_file_name = 'weapon_analysis.txt'
        self.table = 'weapon_wishes'
