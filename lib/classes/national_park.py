from .trip import Trip

class NationalPark:

    def __init__(self, name):
        if type(name) == str:
            self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "_name"):
            self._name = name
        else:
            print("Cannot change the name of the NationalPark")

    def trips(self):
        return [ trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return set([ trip.visitor for trip in self.trips() ])
    #test for this one is also throwing an error but it works find when I test in debug.py.
    
    def total_visits(self):
        return len(self.trips())
    #the built in test was throwing an error for this but it worked fine when I run tests in debug.py
    #fixed the test from testing (len(p1.total_visits()== 3) to (p.total_visits() ==3)
    
    def most_frequent(list):
        return max(set(list), key = list.count)

    def best_visitor(self):
        visitors_list = [ trip.visitor for trip in self.trips() ]
        return max(set(visitors_list), key = visitors_list.count)