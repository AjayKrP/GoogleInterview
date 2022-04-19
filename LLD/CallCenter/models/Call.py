from LLD.CallCenter.models.Employee import Level


class Call:
    def __init__(self, rank, caller):
        self.rank = rank
        self.caller = caller
        self.handler = None

    def set_handler(self, handler):
        self.handler = handler

    def get_rank(self):
        return self.rank

    def set_rank(self, rank):
        self.rank = rank

    def disconnect(self):
        self.caller = None
        self.handler = None
        self.rank = None

    def get_caller(self):
        return self.caller

    def set_caller(self, caller):
        self.caller = caller

    def increment_rank(self):
        if self.rank == Level.RESPONDENT:
            self.rank = Level.MANAGER
        elif self.rank == Level.MANAGER:
            self.rank = Level.DIRECTOR
        elif self.rank == Level.DIRECTOR:
            # Can't handle this call Please call after some time
            return False
        return True
