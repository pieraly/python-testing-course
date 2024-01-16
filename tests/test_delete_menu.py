from classes.menu import Menu
import pytest

@pytest.mark.parametrize(
    "restaurant_name, item_name, expected_result",
    [
        ("Pizza", "calzone", f"Menu item 'calzone' deleted for Pizza."),
        ("Sushi", "tempura", f"Menu item 'tempura' deleted for Sushi."),
        ("Crêperie", "galette", f"Menu item 'galette' deleted for Crêperie."),
        ("Tacos", "quesadilla", f"Menu item 'quesadilla' deleted for Tacos.")
    ]
)
def test_delete_restaurant_menu(menu_manager_with_item, restaurant_name, item_name, expected_result):
    menu_manager, _, _ = menu_manager_with_item
    result = menu_manager.delete_menu_item(restaurant_name, item_name)
    assert result == expected_result

    menu = menu_manager.get_menu(restaurant_name)
    deleted_menu_item = {'item_name': item_name, 'description': "my menu description", 'price': 10.00}
    assert deleted_menu_item not in menu
