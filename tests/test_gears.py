from unittest import TestCase
from robot_math.gears import Gear, get_final_speed


class GravityTests(TestCase):

    def test_get_final_speed_two_gears(self):
        """
        Test that the correct value is returned for the final
        speed of two connected gears.
        """
        first_gear = Gear(30)
        second_gear = Gear(40)

        gear_list = [first_gear, second_gear]

        speed_of_first_gear = 100 # rpm

        self.assertEqual(
            get_final_speed(gear_list, speed_of_first_gear),
            75
        )

    def test_final_speed_multiple_equal_gears(self):
        """
        Test that the sum of the speed of three gears with
        equal numbers of teeth will remain constant.
        """
        gear_list = [Gear(50), Gear(50), Gear(50)]
        first_gear_speed = 500 # 500 rpm

        self.assertEqual(
            get_final_speed(gear_list, first_gear_speed),
            500
        )

    def test_get_final_speed_single(self):
        """
        Test that the final speed of a single gear
        is the same as the gear's current speed.
        """
        # A gear with 50 teeth
        gear = Gear(50)

        # The speed of the gear will be 100 rpm
        speed = 100

        self.assertEqual(
            get_final_speed([], speed),
            speed
        )

