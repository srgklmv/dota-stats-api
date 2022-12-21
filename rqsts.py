import requests as rq


"""Opendota section"""
player_info = "https://api.opendota.com/api/players/"


"""Functions"""


def get_player_info(id32: str):

    info = rq.get(player_info + id32)

    return info.json()
