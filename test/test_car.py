import unittest
from datetime import date
from car_services import (
    CapuletEngineService,
    WilloughbyEngineService,
    SternmanEngineService,
    SpindlerBatteryService,
    NubbinBatteryService,
)

class TestCarServices(unittest.TestCase):
    def test_capulet_engine_service_needs_service(self):
        capulet_service = CapuletEngineService()

        # Test when mileage is below 30,000
        self.assertFalse(capulet_service.needs_service(20000, 10000))

        # Test when mileage is exactly 30,000
        self.assertFalse(capulet_service.needs_service(30000, 0))

        # Test when mileage is above 30,000
        self.assertTrue(capulet_service.needs_service(40000, 10000))

    def test_willoughby_engine_service_needs_service(self):
        willoughby_service = WilloughbyEngineService()

        # Test when mileage is below 60,000
        self.assertFalse(willoughby_service.needs_service(40000, 10000))

        # Test when mileage is exactly 60,000
        self.assertFalse(willoughby_service.needs_service(60000, 0))

        # Test when mileage is above 60,000
        self.assertTrue(willoughby_service.needs_service(70000, 10000))

    def test_sternman_engine_service_needs_service(self):
        sternman_service = SternmanEngineService()

        # Test when warning light is off
        self.assertFalse(sternman_service.needs_service(False))

        # Test when warning light is on
        self.assertTrue(sternman_service.needs_service(True))

    def test_spindler_battery_service_needs_service(self):
        spindler_service = SpindlerBatteryService()
        last_service_date = date(2021, 1, 1)
        current_date = date(2023, 1, 1)

        # Test when battery needs service after 2 years (365 * 2 days)
        self.assertTrue(spindler_service.needs_service(last_service_date, current_date))

        # Test when battery does not need service before 2 years
        self.assertFalse(spindler_service.needs_service(last_service_date, date(2022, 1, 1)))

    def test_nubbin_battery_service_needs_service(self):
        nubbin_service = NubbinBatteryService()
        last_service_date = date(2021, 1, 1)
        current_date = date(2025, 1, 1)

        # Test when battery needs service after 4 years (365 * 4 days)
        self.assertTrue(nubbin_service.needs_service(last_service_date, current_date))

        # Test when battery does not need service before 4 years
        self.assertFalse(nubbin_service.needs_service(last_service_date, date(2023, 1, 1)))

if __name__ == '__main__':
    unittest.main()
