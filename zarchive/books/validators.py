from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MinimalNumberValidator:
    def __init__(self, number, message=None):
        self.number = number
        self.message = message

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"Minimum value should be less than {self.number}"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if value <= self.number:
            raise ValidationError(self.message)


@deconstructible
class MaximalNumberValidator:
    def __init__(self, number, message=None):
        self.number = number
        self.message = message

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"Maximum value should more than {self.number}"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if value >= self.number:
            raise ValidationError(self.message)
