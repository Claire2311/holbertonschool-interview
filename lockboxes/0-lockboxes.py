#!/usr/bin/python3
"""
This is the solution to solve the Lockboxes algorithm
"""


def canUnlockAll(boxes):
    """This is a function to solve the Lockboxes algorithm"""
    num_of_boxes = []
    for i in range(len(boxes)):
        num_of_boxes.append(i)

    obtained_keys = [0]
    opened_boxes = []
    new_boxes_to_open = [0]

    def openBox(number_of_box):
        opened_boxes.append(number_of_box)
        new_boxes_to_open.remove(number_of_box)
        for key in boxes[number_of_box]:
            if key >= len(num_of_boxes):
                pass
            elif key not in obtained_keys:
                obtained_keys.append(key)
                new_boxes_to_open.append(key)

    openBox(0)

    while new_boxes_to_open:
        for key in obtained_keys:
            if key not in opened_boxes:
                openBox(key)

    if num_of_boxes == sorted(obtained_keys):
        return True
    else:
        return False
