def canUnlockAll(boxes):
    num_of_boxes = []
    for i in range(len(boxes)):
        num_of_boxes.append(i)
    print(num_of_boxes)

    obtained_keys = [0]
    opened_boxes = []
    new_boxes_to_open = [0]

    def openBox(number_of_box):
        opened_boxes.append(number_of_box)
        new_boxes_to_open.remove(number_of_box)
        for key in boxes[number_of_box]:
            if key not in obtained_keys:
                obtained_keys.append(key)
                new_boxes_to_open.append(key)

    openBox(0)
    print("obtained_keys", obtained_keys)
    print("opened_boxes", opened_boxes)
    print("new_boxes_to_open", new_boxes_to_open)

    # while new_boxes_to_open:
    #     if num_of_boxes == sorted(obtained_keys):
    #         print("Yes, tu as ouvert toutes les boites")
    #         return True
    #     elif sorted(opened_boxes) != sorted(obtained_keys):
    #         for key in obtained_keys:
    #             if key not in opened_boxes:
    #                 openBox(key)
    #         print("obtained_keys int he while loop", obtained_keys)
    #     else:
    #         print("il manque encore des boites")
    #         return False

    while new_boxes_to_open:
        for key in obtained_keys:
            if key not in opened_boxes:
                openBox(key)
            print("obtained_keys int he while loop", obtained_keys)

    if num_of_boxes == sorted(obtained_keys):
        print("Yes, tu as ouvert toutes les boites")
        return True
    else:
        print("il manque encore des boites")
        return False 


boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
canUnlockAll(boxes)
