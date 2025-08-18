class DiscountStrategy:
    def apply_discount(self, amount):
        return amount

class RegularDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.9

class VIPDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.8

# Uso
def get_discounted_price(strategy: DiscountStrategy, amount):
    return strategy.apply_discount(amount)

print(get_discounted_price(RegularDiscount(), 100))
print(get_discounted_price(VIPDiscount(), 100))
