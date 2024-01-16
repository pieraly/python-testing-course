import pytest
from classes.menu import Menu

# Paramètres pour le test paramétré
@pytest.mark.parametrize(
    "restaurant_name, item_name, description, price",
    [
        ("Pizza", "calzone", "farce délicieuse et fromage fondant", 12.99),
        ("Sushi", "tempura", "crevettes croustillantes et légumes", 15.00),
        ("Crêperie", "galette", "jambon, fromage et œuf", 7.50),
        ("Tacos", "quesadilla", "poulet grillé et fromage fondant", 9.50)
    ]
)
def test_get_restaurant_menu(restaurant_name, item_name, description, price):
    menu_manager = Menu()
    menu_manager.add_menu_item(restaurant_name, item_name, description, price)
    menu = menu_manager.get_menu(restaurant_name)
    expected_menu_item = {'item_name': item_name, 'description': description, 'price': price}
    assert expected_menu_item in menu
