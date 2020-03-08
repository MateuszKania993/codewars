from collections import Counter


def delete_nth(order, max_e):
    new_list = []
    for num in order:
        if num not in new_list:
            new_list.append(num)
        else:
            c = Counter(new_list)
            if c[num] < max_e:
                new_list.append(num)

    return new_list

print(delete_nth([1,1,1,1],2))
print(delete_nth([20,37,20,21],1))