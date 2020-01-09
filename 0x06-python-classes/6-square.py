#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__position = position
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        area = self.__size ** 2
        return area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) > 2:
            if (isinstance(value[0], int) and isinstance(value[1], int)):
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
             raise TypeError("position must be a tuple of 2 positive integers")


    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                    print("")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
            