import pytest
import pygame

from janzeng.game import Game


def test_engine_instantiation():
    game = Game()


def test_quit_event(mocker):
    def side_effect():
        return [pygame.event.Event(pygame.QUIT, {})]

    mocked_get = mocker.patch('pygame.event.get')
    mocked_get.side_effect = side_effect

    game = Game()
    assert game.running is False

    game.run()

    assert game.running is False
