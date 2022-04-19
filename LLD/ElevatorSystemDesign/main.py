from LLD.ElevatorSystemDesign.models.Direction import Request, RequestType, Direction
from LLD.ElevatorSystemDesign.services.Elevator import Elevator

elevator = Elevator(0)
upRequest1 = Request(elevator.current_floor, 5, RequestType.internal, Direction.up)
upRequest2 = Request(elevator.current_floor, 3, RequestType.internal, Direction.up)

downRequest1 = Request(elevator.current_floor, 1, RequestType.internal, Direction.down)
downRequest2 = Request(elevator.current_floor, 2, RequestType.internal, Direction.down)

upRequest3 = Request(4, 8, RequestType.external, Direction.up)
downRequest3 = Request(6, 3, RequestType.external, Direction.down)

elevator.sendUpStopRequest(upRequest1)
elevator.sendUpStopRequest(upRequest2)

elevator.sendDownRequest(downRequest1)
elevator.sendDownRequest(downRequest2)

elevator.sendUpStopRequest(upRequest3)
elevator.sendDownRequest(downRequest3)

elevator.run()
