from random import random

from keys import keys

gen = []
def generate_ran_li_ele(length):
    for ran in range(length,):
        new = random();
        ran = int(new*len(keys))
        gen.append(keys[ran])
