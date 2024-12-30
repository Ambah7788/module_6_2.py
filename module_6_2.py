class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'green', 'white', 'black']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        # Validate color against the available variants
        self.__color = color if color.lower() in [c.lower() for c in Vehicle.__COLOR_VARIANTS] else 'black'

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power} л.с."

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self) -> None:
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str) -> None:
        if new_color.lower() in [c.lower() for c in Vehicle.__COLOR_VARIANTS]:
            self.__color = new_color
            print(f"Цвет успешно изменен на {new_color}.")
        else:
            print(f"Нельзя сменить цвет на {new_color}.")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        super().__init__(owner, model, engine_power, color)


if __name__ == "__main__":
    my_sedan = Sedan(owner="Иван", model="Toyota Camry", engine_power=150, color="blue")
    my_sedan.print_info()

    my_sedan.set_color("green")
    my_sedan.print_info()

    my_sedan.set_color("purple")