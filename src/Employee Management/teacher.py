from person import Person,Consts
class Teacher(Person,Consts):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.job = "teacher"

    def get_price(self):
        price =Consts.BASE_PRICE[self.job]-(self.age-Consts.MIN_AGE)* Consts.AGE_MUL
        return int(price)

    def calc_life_cost(self):
        a=Consts.BASE_COST[self.job]
        b=self.age-Consts.MIN_AGE
        c=Consts.AGE_MUL
        costs= a+b*c
        return costs

    def calc_income(self):
        a=Consts.BASE_INCOME[self.job][self.work_place.get_expertise()]
        b = self.age-Consts.MIN_AGE
        c = Consts.AGE_MUL
        income =a-(b)*c
        return income