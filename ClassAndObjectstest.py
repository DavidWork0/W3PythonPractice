import pytest
from ClassAndObjects import Character  # Import your Character class from the correct module

@pytest.fixture
def character():
    return Character("Test", 10, 20, 30)

def test_initial_values(character):
    assert character.name == "Test"
    assert character.health == 10
    assert character.damage == 20
    assert character.speed == 30

def test_double_health(character):
    character.double_health()
    assert character.health == 20

def test_double_damage(character):
    character.double_damage()
    assert character.damage == 40

def test_double_speed(character):
    character.double_speed()
    assert character.speed == 60

def test_ultra_buff(character):
    character.ultra_buff()
    assert character.health == 20
    assert character.damage == 40
    assert character.speed == 60

def test_print_char_details(character, capsys):
    character.print_char_details()
    captured = capsys.readouterr()  # Captures the output of print statements
    assert "Name: Test" in captured.out
    assert "Health: {10}" in captured.out
    assert "Damage: {20}" in captured.out
    assert "Speed: {30}" in captured.out