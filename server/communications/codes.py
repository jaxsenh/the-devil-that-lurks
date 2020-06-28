# MAIN MENU CODES
REQUEST_GAME = 0
DELIVER_GAME = 1
DELIVER_PID = 2
KICKED_FROM_GAME = 3
KILLED = 4

# KICKED CODES
# 3
GAME_DELETED = 31
ALREADY_IN_GAME = 32
GENERAL = 33
LEFT_GAME = 34

# IN-GENERAL
# 4
HEARTBEAT = 41
KILLED_CONNECTION = 42
GOODBYE = 43

# LOBBY CODES
# 10
ADD_PLAYER = 101
REMOVE_PLAYER = 102
UPDATE_VOTE_COUNT = 103
VOTE_TO_START = 104
START_GAME = 105
LEAVE_LOBBY = 106
UPDATE_NAME = 107

# GAME VARIABLES
TIME = 10
MAX_PLAYERS = 9
MAX_DAYS = 3
HEARTBEAT_SERVER = 11
HEARTBEAT_PLAYER = 5

# GAME CODES
# 20
GOTO_DAY = 201
GOTO_NIGHT = 202
YOU_ARE_KILLER = 203
KILL_FAILED_EMPTY_ROOM = 204
SET_KILL = 205
HAS_DIED = 206
NUM_IN_ROOM = 207

# ROOM CODES
# 21
SET_ROOM = 211
KITCHEN = 212
LIVING_ROOM = 213
BEDROOM = 214
PORCH = 215
DINING_ROOM = 216

ROOMS = [
    KITCHEN,
    LIVING_ROOM,
    BEDROOM,
    PORCH,
    DINING_ROOM
]