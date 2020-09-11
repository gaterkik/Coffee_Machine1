class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100

#
# new_pig = PiggyBank(0, 99)
# new_pig.add_money(1, 1)
# print(new_pig.dollars, new_pig.cents)