import math
from person import Person,Consts
class Worker(Person,Consts):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.job="worker"

    def get_price(self):
        price=math.floor(Consts.BASE_PRICE[self.job]*(Consts.MIN_AGE /self.age))
        return int(price)

    def calc_life_cost(self):
        a= Consts.BASE_COST[self.job]
        b= (self.age/Consts.MIN_AGE)
        costs= math.floor(a*b)
        return costs

    def calc_income(self):
        income=math.floor(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()]*(Consts.MIN_AGE/self.age))
        return int(income)
