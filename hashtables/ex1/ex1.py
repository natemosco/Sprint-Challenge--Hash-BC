#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    compliment_list = []
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    for i in range(length):
        compliment_index = hash_table_retrieve(ht, limit-weights[i])
        if compliment_index is not None:
            if compliment_index > i:
                compliment_list.append(compliment_index)
                compliment_list.append(i)
            else:
                compliment_list.append(i)
                compliment_list.append(compliment_index)
    if len(compliment_list) > 0:
        return compliment_list
    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
