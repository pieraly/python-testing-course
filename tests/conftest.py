from classes.menu import Menu
import pytest

# Fixture pour créer une instance de Menu et ajouter un élément au menu
@pytest.fixture(params=[
    ("Pizza", "calzone"),
    ("Sushi", "tempura"),
    ("Crêperie", "galette"),
    ("Tacos", "quesadilla")

])
def menu_manager_with_item(request):
    menu_manager = Menu()
    restaurant_name, item_name, description, price = request.param
    menu_manager.add_menu_item(restaurant_name, item_name, description, price)
    return menu_manager, restaurant_name, item_name

def test_add_menu_item(menu_manager_with_item):
    menu_manager, restaurant_name, item_name = menu_manager_with_item
    result = menu_manager.get_menu_item_description(restaurant_name, item_name)
    assert result == menu_manager_with_item[0].get_menu_item_description(restaurant_name, item_name)
