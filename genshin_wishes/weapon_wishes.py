from .wishes_base import WishesBase

class WeaponWishes(WishesBase):
    def init_params(self):
        self.params['gacha_type'] = '302'
        self.file_name = 'genshine_weapon_wishes.csv'

    def to_remote_storage(self):
        pass

