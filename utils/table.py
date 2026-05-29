class Seat:
    """
    The Seat class represents a seat in the open space.
    It can be occupied by a person or be free. It has methods to set and remove an occupant, and to check if it is free.
    """

    def __init__(self):
        self.free = True
        self.occupant = None

    def set_occupant(self, name):
        self.occupant = name
        self.free = False
        

    def remove_occupant(self):
        self.free = True
        self.occupant = None
    
    def __str__(self):
        if self.free:
            return "Free"
        else:
            return f"Occupied by {self.occupant}"


class Table:
    """
    The Table class represents a table in the open space. It contains seats and manages the allocation of people to those seats
    """
    def __init__(self):
        self.capacity = 4 # nombre de places libres dans la table
        self.seats = []
        for _ in range(self.capacity):
            self.seats.append(Seat())# on a créé une boucle for d'une taille de la capacité imposée de 4
   
    #on veut savoir savoir si il y a une place libre dans la table 
    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
        return False
    
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                self.capacity -= 1
                break

    
    def left_capacity(self):
        return self.capacity
    
    def __str__(self):
        result = "Table status:\n"
        for i, seat in enumerate(self.seats):
            result += f"Seat {i + 1}: {seat}\n"
        return result
    
