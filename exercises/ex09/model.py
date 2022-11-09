"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730561113"  # TODO


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> int:
        """Calculates distance between two points."""
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """What the model does for each 'tick' of the program (1/30 of a second)."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()  

    # def color(self) -> str:
        # """Return the color representation of a cell."""
        # return "black"
    
    def contract_disease(self):
        """Gives a cell the infected value."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Checks if a cell is assigned the vulnerable value."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Checks if a cell is assigned the infected value."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def color(self) -> str:
        """Determines color of cell depending on state (vulnerable, infected, immune)."""
        if self.is_infected():
            return "green"
        if self.is_vulnerable():
            return "gray"
        if self.is_immune():
            return "blue"

    def contact_with(self, other: Cell) -> None:
        """Transmits disease to cells if one is vulnerable and one is infected."""
        if self.is_vulnerable() and other.is_infected():
            self.contract_disease()
        if other.is_vulnerable() and self.is_infected():
            other.contract_disease() 
    
    def immunize(self) -> None:
        """Gives a cell the immune value."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Checks if a cell is assigned the immune value."""
        return self.sickness == constants.IMMUNE


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        infected_num: int = 0
        immune_num: int = 0
        infected_goal: int = infected
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if infected > 0:
                cell.contract_disease()
                infected -= 1
                infected_num += 1
            if infected_num == infected_goal and immune > 0:
                cell.immunize()
                immune -= 1
                immune_num += 1
            self.population.append(cell)
        if infected_num <= 0:
            raise ValueError("There are not enough infected cells.")
        if infected_num >= len(self.population):
            raise ValueError("There are too many infected cells.")
        if immune_num >= len(self.population):
            raise ValueError("There are too many infected and immune cells.")

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        i: int = 0
        infected_num: int = 0
        while i < len(self.population):
            if self.population[i].is_infected():
                infected_num += 1
            i += 1
        if infected_num == 0:
            return True
        else:
            return False
                
    def check_contacts(self) -> None:
        """Checks if cells are near each other at each tick."""
        i: int = 0
        while i < len(self.population):
            j: int = i + 1
            while j < len(self.population):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])
                j += 1
            i += 1