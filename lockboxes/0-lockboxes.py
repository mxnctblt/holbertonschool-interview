#!/usr/bin/python3
""" canUnlockAll """


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened

    Args:
        - boxes: list of lists
    """
    # check if boxes is a list of lists
    if not isinstance(boxes, list) or not all(
            isinstance(box, list) for box in boxes):
        return False
    # check if list is empty
    if len(boxes) == 0:
        return False

    # dictionary of all boxes, set to locked
    unlock = {k: False for k in range(len(boxes))}
    # unlock the first box
    unlock[0] = True
    # create the set of keys with the keys of box 0
    keys = list(boxes[0])
    # unlocking boxes
    while keys:
        new_key = []
        for key in keys:
            if key in unlock.keys() and unlock[key] is False:
                unlock[key] = True
                new_key += boxes[key]
        # return true if all boxes are unlocked
        if all(unlock.values()):
            return True
        # update the set of keys
        keys = new_key
    # return false if not all boxes are unlocked
    return False
