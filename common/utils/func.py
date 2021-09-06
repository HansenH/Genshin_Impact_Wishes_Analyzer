# helper functions

from functools import reduce
from operator import concat


def get_url_from_file(file: str) -> str:
    f = open(file, "r")
    url = reduce(concat, map(lambda xs: xs[:-1] if xs[-1] == '\n' else xs, f.readlines()))
    f.close()
    return url
