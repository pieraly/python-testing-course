from classes.menu import Menu 
import pytest

@pytest.mark.parametrize(
    "restaurant_name, item_name, description, price, expected_result",
    [
        ("Pizza", "calzone", "farce délicieuse et fromage fondant", 12.99, 
         f"Menu item 'calzone' added for Pizza."),

        ("Sushi", "tempura", "crevettes croustillantes et légumes", 15.00, 
         f"Menu item 'tempura' added for Sushi."),

        ("Crêperie", "galette", "jambon, fromage et œuf", 7.50, 
         f"Menu item 'galette' added for Crêperie."),

        ("Tacos", "quesadilla", "poulet grillé et fromage fondant", 9.50, 
         f"Menu item 'quesadilla' added for Tacos.")
        
    ]
)
def test_add_menu_item(restaurant_name, item_name, description, price,expected_result):
    menu_manager = Menu()
    result = menu_manager.add_menu_item(restaurant_name, item_name, description, price)
    assert result == expected_result 
    menu = menu_manager.get_menu(restaurant_name)
    expected_menu_item = {'item_name': item_name, 'description': description, 'price': price}
    assert expected_menu_item in menu

