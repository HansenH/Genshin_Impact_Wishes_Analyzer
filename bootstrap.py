from genshin_wishes import \
    CharacterWishes, StandardWishes, NoviceWishes, WeaponWishes
import logging
import argparse
from common.utils.func import get_url_from_file
from common.idl import Tasks


def get_tasks(task_id, url):
    if task_id == Tasks.CharacterWishes.value:
        task = CharacterWishes(url)
    elif task_id == Tasks.WeaponWishes.value:
        task = WeaponWishes(url)
    elif task_id == Tasks.StandardWishes.value:
        task = StandardWishes(url)
    elif task_id == Tasks.NoviceWishes.value:
        task = NoviceWishes(url)
    elif task_id == Tasks.AllWishes.value:
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
    help_message = '0 -> All four Wishes; ' \
        '1 -> Character Wishes; ' \
        '2 -> Novice Wishes; ' \
        '3 -> Standard Wishes; ' \
        '4 -> Weapon Wishes.'
    parser = argparse.ArgumentParser(description='Genshine Impact Wishes Data Analyzer')
    parser.add_argument('task_id', type=int, help=help_message)
    parser.add_argument('url_file', type=str, help='Genshine Impact request url, README for detail.')
    args = parser.parse_args()

    try:
        tasks = get_tasks(args.task_id, get_url_from_file(args.url_file))
        logging.info('Current tasks: {}'.format(tasks))
        for task in tasks:
            task.run()
    except Exception as ex:
        logging.error(ex)
        exit(1)
