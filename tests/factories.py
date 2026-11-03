import factory
from factory.fuzzy import FuzzyChoice, FuzzyFloat
from models.product import Product, Category

class ProductFactory(factory.Factory):
    """Creates fake products for testing"""
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = FuzzyChoice(choices=['Hat', 'Pants', 'Shirt', 'Apple', 'Mac'])
    description = factory.Faker('text')
    price = FuzzyFloat(10.0, 50.0)
    available = FuzzyChoice(choices=[True, False])
    category = FuzzyChoice(choices=[Category.UNKNOWN, Category.CLOTHS, Category.FOOD, Category.HOUSEWARES, Category.AUTOMOTIVE, Category.TOOLS])
