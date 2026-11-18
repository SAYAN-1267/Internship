
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product.get_total()

        return total

    def calculate_tax(self):
        return self.calculate_total() * self.tax_rate / 100

    def display_bill(self):
        print("\n" + "=" * 65)
        print("                 CUSTOMER BILL")
        print("=" * 65)

        print(f"{'Product':<15}{'Price':>12}{'Quantity':>12}{'Total':>15}")
        print("-" * 65)

        for product in self.products:
            print(f"{product.name:<15}"
                  f"{product.price:>12.2f}"
                  f"{product.quantity:>12}"
                  f"{product.get_total():>15.2f}")

        print("-" * 65)

        subtotal = self.calculate_total()
        tax = self.calculate_tax()
        final_total = subtotal + tax

        print(f"{'Subtotal:':>45} {subtotal:>10.2f}")
        print(f"{'Tax (' + str(self.tax_rate) + '%):':>45} {tax:>10.2f}")
        print("=" * 65)
        print(f"{'Final Amount:':>45} {final_total:>10.2f}")
        print("=" * 65)


# Main program
bill = Bill(18)

p1 = Product("Laptop", 50000, 1)
p2 = Product("Mouse", 500, 2)
p3 = Product("Keyboard", 1000, 1)

bill.add_product(p1)
bill.add_product(p2)
bill.add_product(p3)

bill.display_bill()
