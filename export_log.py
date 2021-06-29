# -*- coding: UTF-8 -*-
# 导出抽卡记录

ADDRESS = 'https://hk4e-api.mihoyo.com/event/gacha_info/api/getGachaLog'
TIMESLEEP = 0.2
PAGE_SIZE = 6

import json
import time
from datetime import datetime
import requests
import pandas
from urllib import parse

def export_log(url):
    resolved = dict(parse.parse_qsl(parse.urlsplit(url.strip()).query))
    params = {
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

    # 角色祈愿
    character_wishes = []
    params['gacha_type'] = '301'
    params['page'] = '1'
    params['end_id'] = '0'
    while True:
        r = requests.get(ADDRESS, params=params)
        if r.status_code != 200:
            print('ERROR')
            return
        response = json.loads(r.text)
        if response['message'].upper() != 'OK':
            print('ERROR')
            return
        character_wishes += response['data']['list']
        if len(response['data']['list']) < PAGE_SIZE:
            break
        params['page'] = str(int(params['page']) + 1)
        params['end_id'] = response['data']['list'][-1]['id']
        time.sleep(TIMESLEEP)
    print('角色祈愿', len(character_wishes))
    print(character_wishes)

    # 武器祈愿
    weapon_wishes = []
    params['gacha_type'] = '302'
    params['page'] = '1'
    params['end_id'] = '0'
    while True:
        r = requests.get(ADDRESS, params=params)
        if r.status_code != 200:
            print('ERROR')
            return
        response = json.loads(r.text)
        if response['message'].upper() != 'OK':
            print('ERROR')
            return
        weapon_wishes += response['data']['list']
        if len(response['data']['list']) < PAGE_SIZE:
            break
        params['page'] = str(int(params['page']) + 1)
        params['end_id'] = response['data']['list'][-1]['id']
        time.sleep(TIMESLEEP)
    print('武器祈愿', len(weapon_wishes))
    print(weapon_wishes)

    # 常驻祈愿
    standard_wishes = []
    params['gacha_type'] = '200'
    params['page'] = '1'
    params['end_id'] = '0'
    while True:
        r = requests.get(ADDRESS, params=params)
        if r.status_code != 200:
            print('ERROR')
            return
        response = json.loads(r.text)
        if response['message'].upper() != 'OK':
            print('ERROR')
            return
        standard_wishes += response['data']['list']
        if len(response['data']['list']) < PAGE_SIZE:
            break
        params['page'] = str(int(params['page']) + 1)
        params['end_id'] = response['data']['list'][-1]['id']
        time.sleep(TIMESLEEP)
    print('常驻祈愿', len(standard_wishes))
    print(standard_wishes)

    # 新手祈愿
    novice_wishes = []
    params['gacha_type'] = '100'
    params['page'] = '1'
    params['end_id'] = '0'
    while True:
        r = requests.get(ADDRESS, params=params)
        if r.status_code != 200:
            print('ERROR')
            return
        response = json.loads(r.text)
        if response['message'].upper() != 'OK':
            print('ERROR')
            return
        novice_wishes += response['data']['list']
        if len(response['data']['list']) < PAGE_SIZE:
            break
        params['page'] = str(int(params['page']) + 1)
        params['end_id'] = response['data']['list'][-1]['id']
        time.sleep(TIMESLEEP)
    print('新手祈愿', len(novice_wishes))
    print(novice_wishes)

    # 整理数据
    data1 = []
    for i in range(len(character_wishes)-1, -1, -1):
        data1.append({
            '类型': character_wishes[i]['item_type'], 
            '名称': character_wishes[i]['name'], 
            '星级': character_wishes[i]['rank_type'], 
            '时间': character_wishes[i]['time']
        })
    df1 = pandas.DataFrame(data1, columns=('类型', '名称', '星级', '时间'))

    data2 = []
    for i in range(len(weapon_wishes)-1, -1, -1):
        data2.append({
            '类型': weapon_wishes[i]['item_type'], 
            '名称': weapon_wishes[i]['name'], 
            '星级': weapon_wishes[i]['rank_type'], 
            '时间': weapon_wishes[i]['time']
        })
    df2 = pandas.DataFrame(data2, columns=('类型', '名称', '星级', '时间'))

    data3 = []
    for i in range(len(standard_wishes)-1, -1, -1):
        data3.append({
            '类型': standard_wishes[i]['item_type'], 
            '名称': standard_wishes[i]['name'], 
            '星级': standard_wishes[i]['rank_type'], 
            '时间': standard_wishes[i]['time']
        })
    df3 = pandas.DataFrame(data3, columns=('类型', '名称', '星级', '时间'))

    data4 = []
    for i in range(len(novice_wishes)-1, -1, -1):
        data4.append({
            '类型': novice_wishes[i]['item_type'], 
            '名称': novice_wishes[i]['name'], 
            '星级': novice_wishes[i]['rank_type'], 
            '时间': novice_wishes[i]['time']
        })
    df4 = pandas.DataFrame(data4, columns=('类型', '名称', '星级', '时间'))

    # 写入Excel
    filename = 'wishes_{}.xlsx'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    xlsx_writer=pandas.ExcelWriter(filename)
    df1.to_excel(xlsx_writer, sheet_name="角色祈愿", index=False)
    df2.to_excel(xlsx_writer, sheet_name="武器祈愿", index=False)
    df3.to_excel(xlsx_writer, sheet_name="常驻祈愿", index=False)
    df4.to_excel(xlsx_writer, sheet_name="新手祈愿", index=False)
    xlsx_writer.save()


if __name__ == '__main__':
    print('原神祈愿记录导出（至Excel文件）')
    url = input('请输入URL:')
    export_log(url)
