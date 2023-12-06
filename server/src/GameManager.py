import logging
import time
from typing import Union

from Game import Game
from Player import Player


class GameManager:
    __instance = None

    @staticmethod
    def __new__(cls, *args, **kwargs):
        if GameManager.__instance is None:
            GameManager.__instance = super(GameManager, cls).__new__(
                cls, *args, **kwargs
            )

            GameManager.__instance.games = {}
            GameManager.__instance.players = {}
        return GameManager.__instance

    def tick(self):
        for _, game in self.games.items():
            game.tick()
        for _, player in self.players.items():
            pass

    def get_game(self, id: str) -> Union[Game, None]:
        if id in self.games.keys():
            return self.games[id]
        return None

    def register_game(self, game: Game) -> bool:
        if game.id not in self.games:
            self.games[game.id] = game
            return True
        return False
    
    def register_player(self, sock) -> None:
        if sock not in self.players:
            self.players[sock] = Player(sock)
    
    def unregister_player(self, sock) -> None:
        if sock in self.players:
            del self.players[sock]

    def data_sent_from(self, sock, data) -> None:
        if sock in self.players:
            logging.info(f"getted: {data}")
