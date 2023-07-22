from datetime import date
from abc import ABC, abstractmethod

# Abstract classes and Engine service implementations
class EngineService(ABC):
    @abstractmethod
    def needs_service(self, current_mileage: int, last_service_mileage: int) -> bool:
        pass

class CapuletEngineService(EngineService):
    def needs_service(self, current_mileage: int, last_service_mileage: int) -> bool:
        return current_mileage - last_service_mileage >= 30000

class WilloughbyEngineService(EngineService):
    def needs_service(self, current_mileage: int, last_service_mileage: int) -> bool:
        return current_mileage - last_service_mileage >= 60000

class SternmanEngineService(EngineService):
    def needs_service(self, warning_light_on: bool) -> bool:
        return warning_light_on

# Abstract class for Battery service criteria and Battery service implementations
class BatteryService(ABC):
    @abstractmethod
    def needs_service(self, last_service_date: date, current_date: date) -> bool:
        pass

class SpindlerBatteryService(BatteryService):
    def needs_service(self, last_service_date: date, current_date: date) -> bool:
        return (current_date - last_service_date).days >= 365 * 2

class NubbinBatteryService(BatteryService):
    def needs_service(self, last_service_date: date, current_date: date) -> bool:
        return (current_date - last_service_date).days >= 365 * 4

# Car class to represent each car model with its corresponding engine and battery service criteria
class Car:
    def __init__(self, model, engine_service, battery_service):
        self.model = model
        self.engine_service = engine_service
        self.battery_service = battery_service

    def needs_engine_service(self, current_mileage: int, last_service_mileage: int, warning_light_on=False) -> bool:
        if isinstance(self.engine_service, SternmanEngineService):
            return self.engine_service.needs_service(warning_light_on)
        else:
            return self.engine_service.needs_service(current_mileage, last_service_mileage)

    def needs_battery_service(self, last_service_date: date, current_date: date) -> bool:
        return self.battery_service.needs_service(last_service_date, current_date)

# Functions to create car instances based on car models
def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    capulet_engine_service = CapuletEngineService()
    spindler_battery_service = SpindlerBatteryService()

    return Car("Calliope", capulet_engine_service, spindler_battery_service)

def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    willoughby_engine_service = WilloughbyEngineService()
    spindler_battery_service = SpindlerBatteryService()

    return Car("Glissade", willoughby_engine_service, spindler_battery_service)

def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
    sternman_engine_service = SternmanEngineService()
    spindler_battery_service = SpindlerBatteryService()

    return Car("Palindrome", sternman_engine_service, spindler_battery_service)

def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    willoughby_engine_service = WilloughbyEngineService()
    nubbin_battery_service = NubbinBatteryService()

    return Car("Rorschach", willoughby_engine_service, nubbin_battery_service)

def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
    capulet_engine_service = CapuletEngineService()
    nubbin_battery_service = NubbinBatteryService()

    return Car("Thovex", capulet_engine_service, nubbin_battery_service)

# Example usage
current_date = date.today()
last_service_date = date(2023, 1, 1)
current_mileage = 20000
last_service_mileage = 18000
warning_light_on = False

calliope_car = create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
glissade_car = create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
palindrome_car = create_palindrome(current_date, last_service_date, warning_light_on)
rorschach_car = create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
thovex_car = create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
