import json
import time
from datetime import datetime
import requests
import pandas as pd
from urllib import parse

ADDRESS = 'https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog'
TIMESLEEP = 0.2
PAGE_SIZE = 6

class WishesBase():
    def __init__(self, url):
        resolved = dict(
            parse.parse_qsl(parse.urlsplit(url.strip()).query)
        )
        self.params = {
            'authkey_ver': resolved['authkey_ver'],
            'sign_type': resolved['sign_type'],
            'auth_appid': resolved['auth_appid'],
            'init_type': resolved['init_type'],
            'gacha_id': resolved['gacha_id'],
            'timestamp': resolved['timestamp'],
            'lang': resolved['lang'],
            'device_type': resolved['device_type'],
            'ext': resolved['ext'],
            'game_version': resolved['game_version'],
            'region': resolved['region'],
            'authkey': resolved['authkey'],
            'game_biz': resolved['game_biz'],
            'gacha_type': '',
            'page': '1',
            'size': str(PAGE_SIZE),
            'end_id': '0'
        }

        self.wishes = []
        self.file_name = ''
        self.df = None

    def run(self):
        raise NotImplementedError

    def init_params(self):
        raise NotImplementedError

    def check_params(self):
        if self.params['gacha_type'] == '':
            raise ValueError("gacha type should be set.")
        if self.file_name == '':
            raise ValueError("file name should be set.")

    def fetch_request(self):
        while True:
            resp = requests.get(ADDRESS, params = self.params)
            if resp.status_code != 200:
                raise RuntimeError("Request Failed: {}.".format(resp.status_code))
            response = json.loads(resp.text)
            if response['message'].upper() != 'OK':
                raise RuntimeError("Request Failed: {}.".format(response['message']))
            self.wishes += response['data']['list']
            if len(response['data']['list']) < PAGE_SIZE:
                break
            self.params['page'] = str(int(self.params['page']) + 1)
            self.params['end_id'] = response['data']['list'][-1]['id']
            time.sleep(TIMESLEEP)

    def process_data(self):
        data = []
        for i in range(len(self.wishes) - 1, -1, -1):
            data.append({
                'item_type': self.wishes[i]['item_type'],
                'name': self.wishes[i]['name'],
                'rank_type': self.wishes[i]['rank_type'],
                'time': self.wishes[i]['time']
            })
        self.df = pd.DataFrame(
            data, columns = ('item_type', 'name', 'rank_type', 'time')
        )
    
    def to_local_file(self):
        '''
        write to local csv file for view.
        '''
        self.df.to_csv(self.file_name, index=False)

    def to_remote_storage(self):
        '''
        write to local/remote db for record.
        '''
        raise NotImplementedError

