class WorkPlaceIsFull(Exception):
    def __str__(self):
        return "work place is full!"


class Consts:
    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}
    BASE_PLACE_COST = 2500
    LEVEL_MUL = 50


class WorkPlace(Consts):
    instances=[]
    def __init__(self, name: str) -> None:
        self.name=name
        self.level=1
        self.expertise=""
        self.employees=[]
        self.capacity=1
        self.instances.append(self)
        

    def get_price(self) -> int:
        if self.expertise=="mine":
            return self.BASE_PRICE["mine"]
        if self.expertise=="school":
            return self.BASE_PRICE["school"]
        if self.expertise=="company":
            return self.BASE_PRICE["company"]

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self) -> None:
        self.level+=1
        self.calc_capacity()

    def hire(self, person) -> None:
        if (self.capacity <= len(self.employees)):
            raise WorkPlaceIsFull()
        else:
            self.employees.append(person)
            person.work_place=self    #person is a obj of Person 

    def get_expertise(self) -> str:
        return self.expertise

    def calc(self) -> int:
        return - self.calc_costs()

    @staticmethod
    def calc_all() -> int:
        totall=0
        for w_place in WorkPlace.instances:
            totall+= w_place.calc()
            
        return totall