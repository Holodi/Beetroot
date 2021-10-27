
class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker: 'Worker'):
        self._workers.append(worker)

    @property
    def worker(self):
        return f'Boss("{self.id}",' \
               f'"{self.name}",' \
               f'"{self.company}",' \
               f'"{self._workers}")'

    def __repr__(self):
        return f'Boss({self.id},' \
               f'"{self.name}",' \
               f'"{self.company}",' \
               f'"{self._workers}")'

    def __str__(self):
        return f'id = {self.id},' \
               f'name = {self.name},' \
               f'company = {self.company},' \
               f'workers = {self._workers}'

class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss: Boss):
        if isinstance(boss, Boss):
            self._boss = boss
            boss.add_worker(self)

    def __repr__(self):
        return f'Worker({self.id},' \
               f'"{self.name}",' \
               f'"{self.company}",' \
               f'"{self._boss}")'

    def __str__(self):
        return f'Worker:(id = {self.id},' \
               f'name = {self.name},' \
               f'company = {self.company},' \
               f'boss = {self._boss})'


boss1 = Boss(1, "Boss1", "Work1")
boss2 = Boss(3, "Boss3", "Work4")
worker1 = Worker(123, "Oleksii", "home", boss1)
worker2 = Worker(321, "Anton", "home", boss1)
worker3 = Worker(321, "Viktor", "work", boss2)
worker1.boss = boss1
worker2.boss = boss2

print(boss1, boss2, sep="\n")
