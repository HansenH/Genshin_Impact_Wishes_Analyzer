from genshin_wishes import WishesBase, CharacterWishes, StandardWishes, NoviceWishes, WeaponWishes
import logging
import argparse
from functools import reduce
from operator import concat

def get_job(job_id, url):
    if job_id == 0:
        return CharacterWishes(url)
    elif job_id == 1:
        return WeaponWishes(url)
    elif job_id == 2:
        return StandardWishes(url)
    elif job_id == 3:
        return NoviceWishes(url)
    elif job_id == 4:
        return [CharacterWishes(url), WeaponWishes(url), StandardWishes(url), NoviceWishes(url)]
    else:
        raise Exception("job id not found")

if __name__ == '__main__':
    help_message = '0 -> Character Wishes; ' \
        '1 -> WeaponWishes Wishes; ' \
        '2 -> Standard Wishes; ' \
        '3 -> Novice Wishes; ' \
        '4 -> All four Wishes.'
    parser = argparse.ArgumentParser(description='Genshine Impact Wishes Data Analyzer')
    parser.add_argument('job_id', type=int, help=help_message)
    parser.add_argument('url_file', type=str, help='Genshine Impact request url, README for detail.')
    args = parser.parse_args()

    f = open(args.url_file, "r")
    url = reduce(concat, f.readlines())
    f.close()
    
    try:
        job = get_job(args.job_id, url)
        if type(job) != list:
            job.run()
        else:
            for j in job:
                j.run()
    except Exception as ex:
        logging.error(ex)
        exit(1)
