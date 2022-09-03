import re
from const import TRANS


def normalize(name: str):
    trl_name = re.sub(r"\W", "_", name.translate(TRANS))
    return trl_name