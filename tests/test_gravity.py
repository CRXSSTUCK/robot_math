from unittest import TestCase
from decimal import Decimal, ROUND_DOWN
from robot_math.gravity import gravitational_acceleration
from robot_math.astronomy.planets import Earth


class GravityTests(TestCase):

    def test_gravitational_acceleration_earth(self):
        """
        Test that the value calculated for gravitational
        acceleration on Earth equates to 9.81 meters per
        second squared. (This value should be accurate
        within two decimal places.
        """
        g_acceleration = gravitational_acceleration(
            Earth.mass,
            Earth.radius
        )

        # Truncate the result to two decimal places
        truncated = Decimal(g_acceleration).quantize(
            Decimal((0, (1,), -2)),
            rounding=ROUND_DOWN
        )

        self.assertEqual(float(truncated), 9.81)
