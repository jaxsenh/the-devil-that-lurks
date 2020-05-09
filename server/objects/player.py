class Player:
    def __init__(self, _local_id, _connection=None, _pid=None, _ai=False):
        self.voted_to_start = False
        self.room = None
        self.blocking = None
        self.connection = _connection
        self.pid = _pid
        self.alive = True
        self.ai = _ai
        self.local_id = _local_id

    def get_pid(self):
        return self.pid

    def get_local_id(self):
        return self.local_id

    def get_connection(self):
        return self.connection

    # self.voted_to_start
    def set_voted_to_start(self, _voted_to_start):
        self.voted_to_start = _voted_to_start

    def get_voted_to_start(self):
        return self.voted_to_start

    # self.room
    def set_room(self, _room):
        self.room = _room

    def get_room(self):
        return self.room

    # self.blocking
    def set_block(self, _blocking):
        self.blocking = _blocking

    def get_block(self):
        return self.blocking

    # self.alive
    def set_alive(self, _alive):
        self.alive = _alive

    def get_alive(self):
        return self.alive