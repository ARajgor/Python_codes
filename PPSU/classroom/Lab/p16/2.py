class date:
    def __init__(self, day):
        self.day=day
        try:
            Day=int(day)
            print('Enter date is: ',Day)
        except ValueError:
            print("Given value is not integer")

d1 = date('a')
d2 = date(10)