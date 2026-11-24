import unittest

from src.subnet_calculator import calculate_subnet


class TestSubnetCalculator(unittest.TestCase):

    def test_network_address(self):
        result = calculate_subnet("192.168.1.10/24")
        self.assertEqual(result["network_address"], "192.168.1.0")

    def test_broadcast_address(self):
        result = calculate_subnet("192.168.1.10/24")
        self.assertEqual(result["broadcast_address"], "192.168.1.255")

    def test_subnet_mask(self):
        result = calculate_subnet("192.168.1.10/24")
        self.assertEqual(result["subnet_mask"], "255.255.255.0")

    def test_usable_hosts(self):
        result = calculate_subnet("192.168.1.10/24")
        self.assertEqual(result["usable_hosts"], 254)

    def test_private_network(self):
        result = calculate_subnet("10.0.0.1/8")
        self.assertEqual(result["total_addresses"], 16777216)

    def test_single_host_network(self):
        result = calculate_subnet("192.168.1.10/32")
        self.assertEqual(result["usable_hosts"], 1)

    def test_invalid_cidr(self):
        result = calculate_subnet("999.999.999.999/24")
        self.assertFalse(result["valid"])


if __name__ == "__main__":
    unittest.main()