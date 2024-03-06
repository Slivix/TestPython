
from unittest.mock import Mock
from pizza import Pizza
from carte_pizza import CartePizzeria
import pytest

def test_is_empty():
    cp = CartePizzeria()
    assert (cp.is_empty())

def test_is_not_empty():
    cp = CartePizzeria()
    p = Mock()
    cp.add_pizza(p)
    assert not (cp.is_empty())
  
def test_nb_pizza():
    cp =CartePizzeria()
    p1 = Mock(spec=Pizza)
    p2 = Mock(spec=Pizza)
    cp.pizzas = [p1,p2]
    cp.nb_pizzas()

def test_error_nb_pizza():
    cp =CartePizzeria()
    p1 = Mock(spec=Pizza)
    p2 = Mock(spec=Pizza)
    cp.pizzas = [p1,p2]
    cp.nb_pizzas()

def test_remove_existing_pizza():
    cp =CartePizzeria()
    p =Mock(spec=Pizza)
    p.nom = "Margarita"
    cp.pizzas = [p]
    cp.remove_pizza("Margarita")
    
def test_remove_not_existing_pizza():
    cp = CartePizzeria()
    with pytest.raises(CartePizzeriaException):
        cp.remove_pizza("Quatre Fromages")
    
    
