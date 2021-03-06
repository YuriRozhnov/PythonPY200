from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):

        self.__capacity_volume = self.__check_capacity_volume(capacity_volume)
        self.__occupied_volume = self.__check_occupied_volume(occupied_volume)

        self.__check_overflow(self.__capacity_volume, self.__occupied_volume)

    @staticmethod
    def __check_capacity_volume(value) -> Union[int, float]:
        """
        :param value:
        :return:
        """
        if not isinstance(value, (int, float)):
            raise TypeError
        if value <= 0:
            raise ValueError
        return value

    @staticmethod
    def __check_occupied_volume(value) -> Union[int, float]:
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        return value

    @staticmethod
    def __check_overflow(capacity, occupied):
        if capacity < occupied:
            raise OverflowError('Стакан не резиновый')

    def get_capacity_volume(self) -> Union[int, float]:
        """
        Функция возвращает объём стакана
        :return: значение объёма стакана
        """
        return self.__capacity_volume

    def get_occupied_volume(self) -> Union[int, float]:
        """
        Функция возвращает занятый объём стакана
        :return: значение занятого объёма стакана
        """
        return self.__occupied_volume

    def add_water(self, value: Union[int, float]) -> None:
        self.__check_occupied_volume(value)
        self.__check_overflow(self.__capacity_volume, self.__occupied_volume + value)
        self.__occupied_volume += value


if __name__ == "__main__":
    glass1 = Glass(200, 100)  # экземпляр класса
    print(glass1.get_capacity_volume(), glass1.get_occupied_volume())
    glass1.add_water(50)
    print(glass1.get_capacity_volume(), glass1.get_occupied_volume())

    glass2 = Glass(500, 200)
    print(glass2)
    #
    # print("Доливаем воды в первый стакан...")
    # #  TODO доливаем воды в первый стакан
    # print(glass1.capacity_volume, glass1.occupied_volume)
    # print(glass2.capacity_volume, glass2.occupied_volume)
    #
    # #  TODO сравнить id объектов





#from typing import Union
##
#class Glass:

    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):

        self.__capacity_volume = self.__check_capacity_volume(capacity_volume)
        self.occupied_volume = self.__check_occupied_volume(occupied_volume)

        # self.__check_overflow(self.capacity_volume, self.occupied_volume)
        self.__check_overflow()

    @staticmethod
    def __check_capacity_volume(value) -> Union[int, float]:
        """
        :param value:
        :return:
        """
        if not isinstance(value, (int, float)):
            raise TypeError
        if value <= 0:
            raise ValueError
        return value

    @staticmethod
    def __check_occupied_volume(value) -> Union[int, float]:
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        return value

    # @staticmethod
    # def __check_overflow(capacity, occupied):
    #     if capacity < occupied:
    #         raise OverflowError('Стакан не резиновый')
    def __check_overflow(self):
        if self.__capacity_volume < self.occupied_volume:
            raise OverflowError('Стакан не резиновый')


if __name__ == "__main__":
    glass1 = Glass(200, 100)  # экземпляр класса
    print(glass1.__capacity_volume, glass1.occupied_volume)

#    glass2 = ...
#    print(...)  # TODO распечатать атрибуты экземпляра glass2
#
#    print("Доливаем воды в первый стакан...")
#
#    print(glass1.capacity_volume, glass1.occupied_volume)
#    print(glass2.capacity_volume, glass2.occupied_volume)




