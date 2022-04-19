from queue import PriorityQueue

from LLD.CallCenter.models.Employee import Employee, Level

resp = PriorityQueue()
for i in range(10):
    resp.put((0, Employee(i + 1, f'emp-{i + 1}', f'name-{i + 1}', Level.RESPONDENT)))

manager = PriorityQueue()
for i in range(2):
    manager.put((0, Employee(100 * (i + 1), f'emp_m-{i + 1}', f'name_m-{i + 1}', Level.MANAGER)))
director = PriorityQueue()
for i in range(1):
    director.put((0, Employee(1000 * (i + 1), f'emp_d-{i + 1}', f'name_d-{i + 1}', Level.DIRECTOR)))

respondent = [resp, manager, director]
