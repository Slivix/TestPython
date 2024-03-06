import pizza

class CartePizzeria:
    def __init__(self):
        self.pizzas = []

    def is_empty(self):
        if len(self.pizzas) == 0:
            return True
        return False

    def nb_pizzas(self):
        return len(self.pizzas)

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name):
        for pizza in self.pizzas:
            if pizza.nom == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException(f"La pizza '{name}' n'existe pas dans la carte de la pizzeria.")