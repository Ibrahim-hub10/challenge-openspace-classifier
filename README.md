# challenge-openspace-classifier

The purpose of the code : to allow for a random rotation of the 24 collleagues across the 6 tables, each of which has 4 seats. 

In the main.py, We carried out the following steps to generate our final output (seating_arrangement.txt) : 

- Import our class Openspace from the openspace.py file located in the utils folder 
    - We can see my final script which generates my class Openspace where we imported the previous class (Table and Seat) and the random module created by following notebook_guide

- Create a variable file to open (using the open function) the file new_colleagues.txt located in the utils folder 

- Create a variable colleagues to read the entire contents (using the read function) and extract each element of the text file line by line (using the splitlines function), then close the file (using the close function)

- Create the openspace object from the Openspace class, which 

- Call the organise() method and pass it the colleagues list as an argument, which randomly assigns colleagues in the different table. 

- Call the display() method, which displays the different tables and there occupants in a nice and readable way 

- Call the store() method, which saves the result to the seating_arrangement.txt file located in the utils folder 