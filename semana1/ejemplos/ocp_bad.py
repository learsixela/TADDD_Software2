class DiscountCalculator:
    def calculate(self, amount, customer_type):
        if customer_type == "regular":
            return amount * 0.9
        elif customer_type == "vip":
            return amount * 0.8
