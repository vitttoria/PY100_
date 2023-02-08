from abc import abstractmethod


class Car:

    @abstractmethod
    def check_condition_for_sale(self):
        pass

    @abstractmethod
    def check_mileage_for_sale(self):
        pass


class CarForSale(Car):
    def __init__(self, model: str, mileage: int, condition: str):
        self._model = model
        self.mileage = mileage
        self.condition = condition

    @property
    def model(self):
        return self._model

    def check_condition_for_sale(self):
        if self.condition == "Хорошее" or "Очень хорошее" or "Отличное":
            print(f'Сообщаем, что мы заинтересованы в вашей машине {self.model}')
        else:
            print(f'К сожалению мы не заинтересованы в вашей машине {self.model}')

    def check_mileage_for_sale(self):
        if self.mileage < 100000:
            print(f'Мы готовы выкупить вашу машину {self.model}')
        elif not isinstance(self.mileage, int):
            print("Вы ввели не число или не целое число")
        else:
            print(f'К сожалению мы не заинтересованы в вашей машине {self.model}')


class PassengerCar(CarForSale):
    def __init__(self, model: str, mileage: int, condition: str, capacity: int):
        super().__init__(model, mileage, condition)
        self._capacity = capacity

    @classmethod
    def get_car_model(cls):
        print(f'Модель машины {cls.model}')

    def set_mileage(self, mileage):
        if isinstance(mileage, int):
            if mileage > 0:
                self.mileage = mileage
            else:
                print("Пробег не может быть меньше нуля")
        else:
            print("Пробег измеряется в целых числах")

    def get_mileage(self):
        return self.mileage

    def check_condition_for_sale(self):
        if self.condition == "Хорошее" or "Очень хорошее" or "Отличное":
            print(f'Сообщаем, что мы заинтересованы в вашей машине {self.model}, при условии, что другие параметры '
                  f'нас устроят')
        else:
            print("К сожалению мы не заинтересованы в вашей машине")

    def check_mileage_for_sale(self):
        if self.mileage < 100000:
            print(f'Мы готовы выкупить вашу машину {self.model}, при условии, что другие параметры нас устроят')
        elif not isinstance(self.mileage, int):
            print("Вы ввели не число или не целое число")
        else:
            print(f"К сожалению мы не заинтересованы в вашей машине {self.model}")

    @property
    def car_capacity(self):
        return self._capacity

    @car_capacity.setter
    def car_capacity(self, _capacity):
        self._capacity = _capacity

    @staticmethod
    def idealcar(self):
        if 0 < self.mileage < 10000:
            if self.condition == "Отличное":
                print("Ваша машина идеальна, предлагаем максимальную цену")


class TruckCar(CarForSale):
    def __init__(self, model: str, mileage: int, condition: str, tonnage: int):
        super().__init__(model, mileage, condition)
        self._tonnage = tonnage

    def set_mileage(self, mileage):
        if isinstance(mileage, int):
            if mileage > 0:
                self.mileage = mileage
            else:
                print("Пробег не может быть меньше нуля")
        else:
            print("Пробег измеряется в целых числах")

    def get_mileage(self):
        return self.mileage

    def check_condition_for_sale(self):
        if self.condition == "Хорошее" or "Очень хорошее" or "Отличное":
            print(
                f'Сообщаем, что мы заинтересованы в вашей машине {self.model}, при условии, что другие параметры нас '
                f'устроят')
        else:
            print(f'К сожалению мы не заинтересованы в вашей машине {self.model}')

    def check_mileage_for_sale(self):
        if self.mileage < 100000:
            print(f'Мы готовы выкупить вашу машину {self.model}')
        elif not isinstance(self.mileage, int):
            print("Вы ввели не число или не целое число")
        else:
            print(f'К сожалению мы не заинтересованы в вашей машине {self.model}')

    @staticmethod
    def idealcar(self):
        if 0 < self.mileage < 10000:
            if self.condition == "Отличное":
                print(f'Ваша машина {self.model} идеальна, предлагаем максимальную цену')

    @property
    def car_tonnage(self):
        return self._tonnage

    @car_tonnage.setter
    def car_tonnage(self, _tonnage):
        self._tonnage = _tonnage


# class GetCarsForSale:
#     def __int__(self):
#         self.cars = []
#
#     def cars_for_sale(self, car: Car):  # Зависимость на абстакции LibraryBook
#         self.cars.append(car)
#         print(f'Машина {self.cars} добавлена в список на продажу')

    # def check_car_for_sale(self, mileage: int):
    #     if

if __name__ == "__main__":
    # cars_for_sale = GetCarsForSale()
    pass_car = PassengerCar("BMW X5", 3000, "Отличное", 5)
    truck_car = TruckCar("MAN", 120000, "Хорошее", 3000)

    pass_car.get_car_model()
    pass_car.check_mileage_for_sale()
    pass_car.check_condition_for_sale()
    truck_car.check_mileage_for_sale()
    truck_car.check_condition_for_sale()

    # cars_for_sale.cars_for_sale(pass_car)
    # pass_car.idealcar()
