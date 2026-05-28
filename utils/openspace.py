from utils.table import Table
from utils.table import Seat


# Your code here
import random
class Openspace:
    
    def __init__(self):
        self.number_of_tables = 6 # nombre de tables libres dans l'openspace
        self.tables = []
        for _ in range(self.number_of_tables):
            self.tables.append(Table())
    
    def organize (self, names):
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
    def display (self):
        for i, table in enumerate(self.tables):
            print(f"Table {i+1}:")
            for seat in table.seats:
                if seat.free:
                    print("  - Free")
                else:
                    print(f"  - {seat.occupant}")
    
    def store(self, filename):
        with open(filename, 'w') as file:
            for i, table in enumerate(self.tables):
                file.write(f"Table {i+1}:\n")
                for seat in table.seats:
                    if seat.free:
                        file.write("  - Free\n")
                    else:
                        file.write(f"  - {seat.occupant}\n")



