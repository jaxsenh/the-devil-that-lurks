# creates datagrams to send to server
from direct.distributed.PyDatagram import PyDatagram
from codes import *


# Main menu
def dg_deliver_pid(pid):
    dg = PyDatagram()
    dg.addUint8(DELIVER_PID)
    dg.addUint16(pid)
    return dg


def dg_deliver_game(game):
    dg = PyDatagram()
    dg.addUint8(DELIVER_GAME)
    dg.addUint8(game.get_player_count())
    dg.addUint8(game.get_vote_count())
    return dg


# Lobby
def dg_update_player_count(num):
    dg = PyDatagram()
    dg.addUint8(UPDATE_PLAYER_COUNT)
    dg.addUint8(num)
    return dg


def dg_update_vote_count(num):
    dg = PyDatagram()
    dg.addUint8(UPDATE_VOTE_COUNT)
    dg.addUint8(num)
    return dg


def dg_start_game():
    dg = PyDatagram()
    dg.addUint8(START_GAME)
    return dg
