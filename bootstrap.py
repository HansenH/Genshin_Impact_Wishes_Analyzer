from genshin_wishes import \
    CharacterWishes, StandardWishes, NoviceWishes, WeaponWishes
import logging
import argparse
from common.utils.func import get_url_from_file
from common.idl.const_thrift import Tasks


def get_tasks(task_id, url):
    if task_id == Tasks.CharacterWishes:
        task = CharacterWishes(url)
    elif task_id == Tasks.WeaponWishes:
        task = WeaponWishes(url)
    elif task_id == Tasks.StandardWishes:
        task = StandardWishes(url)
    elif task_id == Tasks.NoviceWishes:
        task = NoviceWishes(url)
    elif task_id == Tasks.AllWishes:
        return [
            CharacterWishes(url),
            WeaponWishes(url),
            StandardWishes(url),
            NoviceWishes(url)
        ]
    else:
        raise Exception("task id not found")
    return [task]


if __name__ == '__main__':
    help_message = '0 -> Character Wishes; ' \
        '1 -> WeaponWishes Wishes; ' \
        '2 -> Standard Wishes; ' \
        '3 -> Novice Wishes; ' \
        '4 -> All four Wishes.'
    parser = argparse.ArgumentParser(description='Genshine Impact Wishes Data Analyzer')
    parser.add_argument('task_id', type=int, help=help_message)
    parser.add_argument('url_file', type=str, help='Genshine Impact request url, README for detail.')
    args = parser.parse_args()

    try:
        tasks = get_tasks(args.task_id, get_url_from_file(args.url_file))
        for task in tasks:
            task.run()
    except Exception as ex:
        logging.error(ex)
        exit(1)
