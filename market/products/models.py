from rea.models import *


# Resources for Purchase


class Product(Resource):
    '''Super class'''
    pass

class Book(Product):

    isbn = models.CharField(
        max_length=255)


class Food(Product):
    pass


class Media(Product):
    pass