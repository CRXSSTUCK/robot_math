from decimal import Decimal


class Gear(object):

    def __init__(self, tooth_count):
        self.tooth_count = tooth_count


def get_final_speed(gears, first_gear_speed):
    """
    This method takes an ordered list of gears and the
    speed (rpm) for the first gear in the list.
    The speed of the last gear in the list will be returned.
    """
    current_speed = first_gear_speed

    for index in range(len(gears) -1):
        gear1 = gears[index]
        gear2 = gears[index + 1]

        dividend = Decimal(gear1.tooth_count) / Decimal(gear2.tooth_count)
        current_speed = dividend * current_speed

    return current_speed

