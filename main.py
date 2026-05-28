from utils.openspace import Openspace


file = open("utils/new_colleagues.txt", "r")
colleagues = file.read().splitlines()
file.close()

openspace = Openspace()
openspace.organize(colleagues)
openspace.display()
openspace.store("utils/seating_arrangement.txt")
