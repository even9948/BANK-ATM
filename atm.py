
class atm(object):

    def __init__(self,total_balance,card_number,color,company):
        self.total_balance=total_balance
        self.card_number=card_number
        self.color=color
        self.company=company


    def insertCardInAtm(self):
        print("Card is inserted in ATM machine !!")

    def takeOutCartFromAtm(self):
        print("Card is extracted from ATM machine!!")

    def withdrawCash(sefl):
        print("Cash is withdrawed from Atm!!")


card=atm(1000000,"400300200400","blue","CaneraBank")

print(card.total_balance)
card.withdrawCash()