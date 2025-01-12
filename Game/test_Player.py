import pytest
from Player import Player


@pytest.fixture
def test_player():
    player = Player("UnitTestPlayer")

    player.damage = 10
    player.damage_multiplier = 1.151
    player.coins = 3
    player.shield = 1
    player._max_health = 150
    player.health = 84
    return player


def test_construction(test_player):
    assert test_player.name == "UnitTestPlayer"
    assert test_player.shield == 1
    assert test_player.health <= test_player._max_health - 20
    assert test_player.coins == 3
    assert test_player.damage_multiplier > 1.1
    assert test_player.damage_multiplier < 1.16