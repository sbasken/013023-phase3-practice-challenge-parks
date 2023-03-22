#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip


p1 = NationalPark("Yosemmette")
p2 = NationalPark("Rocky Mountain")
vis = Visitor('Steve')
vis2 = Visitor('joe')
vis3 = Visitor('emily')

t_1 = Trip(vis, p1, "May 5th", "May 9th")
t_2 = Trip(vis2, p1, "May 20th","May 27th")
t_3 = Trip(vis2, p1, "Feb 5th","January 20th")
t_4 = Trip(vis3, p1, "March 5th","January 20th")
t_5 = Trip(vis, p2, "April 5th","January 20th")

ipdb.set_trace()