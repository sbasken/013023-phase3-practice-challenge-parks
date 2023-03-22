
class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        if type(start_date) == str:
            self.start_date = start_date
        else:
            print("start_date needs to be a string!")
        if type(end_date) == str:
            self.end_date = end_date
        else:
            print("end_date needs to be a string!")

        Trip.all.append(self)
