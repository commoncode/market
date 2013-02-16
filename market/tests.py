import datetime

from django.test import TestCase

from rea.models import *

from .agents.models import *
from .carts.models import *
from .commitments.models import *
from .events.models import *
from .ledger.models import *
from .products.models import *
from .resources.models import *


class MarketTest(TestCase):

    def test_event(self):


        # Creat Resources


        food = Food(**{
            'title': 'Fish',
            'slug': 'fish'
            })
        food.save()
        print "Created resource: %s " % food

        cash = Cash(**{
            'title': 'Cash',
            'slug': 'cash',
            })
        cash.save()
        print "Created resource: %s " % cash


        # Create Agents


        customer = Customer(**{
            'title': 'Daryl',
            'slug': 'daryl',
            })
        customer.save()
        print "Created customer: %s" % customer

        store = Store(**{
            'title': 'Brunswick Heads Fish-Coop',
            'slug': 'brunswick-heads-fish-coop',
            })
        store.save()
        print "Created store: %s" % store


        # Contracts


        contract = Contract(**{
            'title': 'Simple purchase contract',
            'slug': 'simple-purchase',
            })
        contract.save()
        print "Created contract: %s" % contract

        clause = Clause(**{
            'text': 'Agree to purchase and make payment of items by Sales Order',
            })
        clause.save()
        print "Created clause: %s" % clause

        contract_clause = ContractClause(**{
            'contract': contract,
            'clause': clause
            })
        print "    Added sales order contract clause: %s" % contract_clause


        # The Cart


        cart = Cart(**{
            'store': store,
            })
        cart.save()
        print "Created cart: %s" % cart

        cartitem = CartItem(**{
            'cart': cart,
            'product': food,
            })
        cartitem.save()
        print "Created cartitem: %s" % cartitem


        # Sales Order


        i = 0
        while i < 20:

            sales_order = SalesOrder(**{
                'contract': contract,
                })
            sales_order.save()
            print "    Created sales order: %s" % sales_order

            sales_line = SalesLine(**{
                'commitment': sales_order,
                'agent': store,
                'quantity': 2,
                'resource': food,
                })
            sales_line.save()
            print "    Created sales line: %s" % sales_line

            payment_line = PaymentLine(**{
                'commitment': sales_order,
                'agent': customer,
                'quantity': 10,
                'resource': cash,
                })
            payment_line.save()
            print "    Created payment line: %s" % payment_line

            # Ledger
            # Enter the Sales Order in the ledger

            ledger_line = LedgerLine(**{
                'increment': payment_line,
                'decrement': sales_line,
                })
            ledger_line.save()
            print "Create ledger line: %s" % ledger_line

            i+=1


        # The Sales Order becomes a real Event, a Sale


        sale = Sale(**{
            'related_commitment': SalesOrder.objects.all().order_by('?')[0],
            'occured_at': 'Brunswick Heads Fish Co-op',
            })
        sale.save()
        print "Created Sale: %s against SalesOrder: %s" % (sale, sale.related_commitment)

        purchase = Purchase(**{
            'event': sale,
            'agent': store,
            'resource': food,
            'quantity': 2,
            })
        purchase.save()
        print purchase

        payment = Payment(**{
            'event': sale,
            'agent': customer,
            'resource': cash,
            'quantity': 10,
            })
        payment.save()
        print payment

        # Ledger
        # Enter the Sale in the ledger

        ledger_line = LedgerLine(**{
            'increment': payment,
            'decrement': purchase,
            })
        ledger_line.save()
        print "Create ledger line: %s" % ledger_line

        import ipdb; ipdb.set_trace()


        print [e for e in Event.objects.all()]
        print [a for a in Agent.objects.all()]
        print [r for r in Resource.objects.all()]

        print [(l.increment, l.decrement) for l in LedgerLine.objects.all()]

        self.assertEqual(1 + 1, 2)



