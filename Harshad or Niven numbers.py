class Harshad:
    @staticmethod
    def is_valid(number):
        list_num = []
        for i in str(number):
            list_num.append(int(i))
        suma = sum(list_num)
        if suma == 0:
            pass
        else:
            if number % suma == 0:
                return True
            else:
                return False

    @staticmethod
    def get_next(number):
        result = Harshad.get_series(1, number)
        return result[0]

    @staticmethod
    def get_series(count, start=0):
        series = []
        for number in range(start + 1, start + 100000):
            if len(series) < count:
                har = Harshad.is_valid(number)
                if har:
                    series.append(number)
        return series


zad = Harshad
print(zad.is_valid(19))
print(zad.get_series(10))
print(zad.get_series(20))
print(zad.get_series(10, 1000))
print(zad.get_next(0))
print(zad.get_next(1))
print(zad.get_next(17))
