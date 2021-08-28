from genshin_wishes import WishesBase, CharacterWishes, StandardWishes, NoviceWishes, WeaponWishes
import logging
import argparse

def get_job(job_id, url):
    if job_id == 0:
        return CharacterWishes(url)
    elif job_id == 1:
        return WeaponWishes(url)
    elif job_id == 2:
        return StandardWishes(url)
    elif job_id == 3:
        return NoviceWishes(url)
    else:
        raise Exception("job id not found")

if __name__ == '__main__':
    help_message = '1 -> Character Wishes' \
        '2 -> WeaponWishes Wishes' \
        '3 -> Standard Wishes' \
        '4 -> Novice Wishes'
    parser = argparse.ArgumentParser(description='Genshine Impact Wishes Data Analyzer')
    parser.add_argument('job_id', type=int, help=help_message)
    parser.add_argument('url', type=str, help='Genshine Impact request url, README for detail.')
    args = parser.parse_args()

    try:
        job = get_job(args.job_id, args.url)
        job.run()
    except Exception as ex:
        logging.error(ex)
        exit(1)
