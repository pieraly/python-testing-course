from classes.menu import Menu
import pytest

@pytest.mark.parametrize(
    "restaurant_name, item_name, new_description, new_price, expected_result",
    [
        ("Pizza", "calzone", "farce délicieuse et fromage fondant", 12.50, f"Menu item 'calzone' updated for Pizza."),
        ("Sushi", "tempura", "crevettes croustillantes et légumes", 9.00, f"Menu item 'tempura' updated for Sushi."),
        ("Crêperie", "galette", "jambon, fromage et œuf", 6.50, f"Menu item 'galette' updated for Crêperie."),
        ("Tacos", "quesadilla", "poulet grillé et fromage fondant", 12.00, f"Menu item 'quesadilla' updated for Tacos.")
    ]
)

@pytest.fixture
def menu_manager_with_item():
    menu_manager = Menu()
    restaurant_name = "Pizza"
    item_name = "calzone"
    menu_manager.add_menu_item(restaurant_name, item_name, "my menu description", 10.00)
    return menu_manager, restaurant_name, item_name

def test_update_restaurant_menu(restaurant_name, item_name, new_description, new_price, expected_result):
    menu_manager = Menu()
    menu_manager.add_menu_item(restaurant_name, item_name, "my menu description", 10.00)
    result = menu_manager.update_menu_item(restaurant_name, item_name, new_description, new_price)
    assert result == expected_result

    menu = menu_manager.get_menu(restaurant_name)
    updated_menu_item = {'item_name': item_name, 'description': new_description, 'price': new_price}
    assert updated_menu_item in menu
