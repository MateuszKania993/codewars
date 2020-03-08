def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        diff = v2 - v1  # różnica prędkości
        time = (g * 3600) / diff  # czas w sekundach
        result = [int(time / 3600), int(time % 3600 / 60), int(time % 3600 % 60)]
        print(result)
        return result

race(720,850,70)
race(80,91,37)
race(80,100,40)
