from rea.models import *


# Events

class Sale(Event):
    pass

class Purchase(DecrementEvent):
    '''Sale or Purchase Line'''
    pass

class Payment(IncrementEvent):
    '''Payent Line for Purchase'''
    pass