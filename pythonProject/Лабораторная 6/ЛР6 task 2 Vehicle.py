class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def get_info(self):
        return f'{self.make} {self.model}'
class Car(Vehicle):#создание класса Car, наследующего от Vehicle
    def __init__(self,make,model,fuel_type):
        super().__init__(make,model)#метод супер для доступа к методам и атрибутам родительского класса, позволяет не указывать его имя явно, нужно чтоб в дочернем вызвать метод рк и изменить его поведение
        self.fuel_type=fuel_type
    def get_info(self):#Переопределение метода для включения информации о типе топлива
        return f'{super().get_info()},  {self.fuel_type}'
vehicle=Vehicle('Toyota','Camry')
print(f'Марка и модель автомобиля: {vehicle.get_info()}')
car=Car('Toyota','Land cruiser prado','diesel')
print(f'Марка, модель, топливо : {car.get_info()}')