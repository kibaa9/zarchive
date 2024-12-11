from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class AlphaValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Ensure this value contains only letters"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if not all(c.isalpha() or c == ',' for c in value):
            raise ValidationError(self.message)


@deconstructible
class LetterAndCommaValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Ensure this value contains only letters and commas"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if not all(c.isalpha() or c == ',' for c in value):
            raise ValidationError(self.message)
