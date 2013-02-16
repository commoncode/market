from rea.models import *


# Commitments

class SalesOrder(Commitment):
    '''
    Sales Order is a commitment to purchase a Product Resource
    in exhange for Cash Resource at a later date.

    Sales Order Commitments result later in a Sale Event.
    '''
    pass

class SalesLine(DecrementCommitment):
    pass

class PaymentLine(IncrementCommitment):
    pass