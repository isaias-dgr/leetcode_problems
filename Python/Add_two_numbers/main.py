# Name: Add two numbers
# You are given two non-empty linked lists representing two non-negative
# integers.
# The digits are stored in reverse order, and each of their nodes contains a
# single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.

def equalized_size(add_1: list, add_2: list):
    size_add_1 = len(add_1)
    size_add_2 = len(add_2)
    diff_size = abs(size_add_1 - size_add_2)
    if size_add_2 < size_add_1:
        add_2.extend([0]*diff_size)
    else:
        add_1.extend([0]*diff_size)


def add_two_numbers(add_1: list, add_2: list) -> list:
    total = list()
    carry: int = 0
    equalized_size(add_1, add_2)
    for index, item in enumerate(add_2):
        add = add_1[index] + add_2[index] + carry
        if add >= 10:
            total.append(add % 10)
            carry = 1
        else:
            total.append(add)
            carry = 0
    if carry:
        total.append(carry)
    return total


if __name__ == "__main__":
    add_1 = [9, 9]
    add_2 = [9, 9, 1]
    output = add_two_numbers(add_1, add_2)
    print("Add two numbers.")
