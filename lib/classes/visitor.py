from .trip import Trip

class Visitor:

    def __init__(self, name):
        if type(name) == str and ( 1 <= len(name) <= 15):
            self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "_name"):
            self._name = name
        else:
            print("Cannot change the name")

    def trips(self):
        return [ trip for trip in Trip.all if trip.visitor == self]
    
    def nationalparks(self):
        return list(set([ trip.national_park for trip in self.trips() ]))
    ##I'm not passing the test for this one but when I test, it works.

    def create_trip(self, national_park, start_date, end_date):
        return Trip(self, national_park, start_date, end_date)

    