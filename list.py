
from li_to_str import list_to_str
from ran_li import gen, generate_ran_li_ele


def randomize_pass(length,item):

    generate_ran_li_ele(length)

    print(list_to_str(item))
    
randomize_pass(128,gen)
