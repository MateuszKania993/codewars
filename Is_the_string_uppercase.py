import string
def is_uppercase(inp):
    up = string.ascii_uppercase
    c = True
    for element in inp:
        while c:
            if element in up:
                print("prawda")
                c = True
            else:
                print("fałsz")
                c = False
    return c



is_uppercase("hello I AM DONALD")