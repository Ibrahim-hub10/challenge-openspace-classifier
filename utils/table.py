class Seat:

    def __init__(self):
        self.free = True
        self.occupant = None

    def set_occupant(self, name):
        self.occupant = name
        self.free = False
        print(f"{self.occupant} is now occupying the seat.")

    def remove_occupant(self):
        self.free = True
        print(f"The seat is now free from {self.occupant}.")
        self.occupant = None


class Table:
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
        print("No free spot available at this table.")
        return False
    
    def assign_seat(self, name):
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                self.capacity -= 1
                break

    
    def left_capacity(self):
        return self.capacity
    
