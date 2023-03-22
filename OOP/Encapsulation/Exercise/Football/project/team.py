from typing import List
from project.player import Player

class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players: List[Player] = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> str or Player:
        try:
            player = next(filter(lambda p: p.name == player_name, self.__players))  #from self.__players list check every player's name and if is same with the given give it
        except StopIteration:  #if there is no player with this name give error with "text"
            return f"Player {player_name} not found"

        self.__players.remove(player) # if there is a player with this name remove it from the list

        return player

    # def remove_player(self, player_name):
    #     for player in self.__players:
    #         if player_name == player:
    #             self.__players.remove(player)
    #             return player
    #
    #     return f"Player {player_name} not found"
    #

