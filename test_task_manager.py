import pytest
from priority_ai import assign_priority

#Код тестування assign_priority
def test_assign_priority():
    assert assign_priority("Терміново зробити звіт") == "Високий"
    assert assign_priority("Зробити сьогодні домашнє") == "Середній"
    assert assign_priority("Погодувати кота") == "Низький"
