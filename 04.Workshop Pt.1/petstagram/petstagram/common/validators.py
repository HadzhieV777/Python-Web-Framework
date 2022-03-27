from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f'Max file size is {self.max_size:.2f} MB'


@deconstructible
class MinDateValidator:
    def __init__(self, min_date):
        self.min_date = min_date

    def __call__(self, value):
        if value < self.min_date:
            raise ValidationError(f'Date must be greater than {self.min_date}')


@deconstructible
class MaxDateValidator:
    def __init__(self, max_date):
        self.max_date = max_date

    def __call__(self, value):
        if self.max_date < value:
            raise ValidationError(f'Date must be earlier than {self.max_date}')
