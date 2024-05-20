import pytest
import unittest.mock as mock

from src.controllers.recipecontroller import RecipeController

# add your test case implementation here
@pytest.mark.unit
def test_normal_recipe(diet = "NORMAL", take_best = True, expected = "Pancakes"):
    mocked_recipecontroller = mock.MagicMock()
    mocked_recipecontroller.find.return_value = "Pancakes"
    sut = RecipeController(mocked_recipecontroller)
    result = sut.get_recipe(diet, take_best)
    assert result[] == expected