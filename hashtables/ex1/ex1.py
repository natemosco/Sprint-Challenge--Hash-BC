#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    tuple_list = []
    for i in range(length):
        ht.hash_table_insert(ht, weights[i], i)
    for i in weights:
        compliment = ht.hash_table_retrieve(ht, limit-i)

    if len(tuple_list) > 0:
        return tuple_list
    else:
        return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
