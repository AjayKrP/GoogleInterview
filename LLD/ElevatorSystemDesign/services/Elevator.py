from heapq import heappush, heappop
from LLD.ElevatorSystemDesign.models.Direction import Request, RequestType, Direction


class Elevator:
    def __init__(self, current_floor):
        self.current_floor = current_floor
        self.direction = Direction.IDLE
        self.upStops = []
        self.downStops = []

    def sendUpStopRequest(self, upRequest):
        if upRequest.typeR == Direction.UP:
            heappush(self.upStops, (upRequest.origin, upRequest.origin))
        heappush(self.upStops, (upRequest.target, upRequest.origin))

    def sendDownRequest(self, downRequest):
        if downRequest.typeR == Direction.DOWN:
            heappush(self.upStops, (-downRequest.origin, downRequest.origin))
        heappush(self.upStops, (-downRequest.target, downRequest.origin))

    def run(self):
        while self.upStops or self.downStops:
            pass

    def processRequests(self):
        if self.direction in [Direction.UP, Direction.IDLE]:
            self.processUpRequests()
            self.processDownRequest()
        else:
            self.processDownRequest()
            self.processUpRequests()

    def processDownRequest(self):
        while self.downStops:
            target, origin = heappop(self.upStops)
            self.current_floor = target

            if target == origin:
                print("Stopping at floor {} to pick up people".format(target))
            else:
                print("stopping at floor {} to let people out".format(target))

        if self.upStops:
            self.direction = Direction.UP
        else:
            self.direction = Direction.IDLE

    def processUpRequests(self):
        while self.upStops:
            target, origin = heappop(self.upStops)
            self.current_floor = target

            if target == origin:
                print("Stopping at floor {} to pick up people".format(target))
            else:
                print("stopping at floor {} to let people out".format(target))

        if self.downStops:
            self.direction = Direction.DOWN
        else:
            self.direction = Direction.IDLE