class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:
    pass


class Guitarist(Band):
    def __str__(self, name="Joan Jett"):
        self.name = name
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Band):
    def __str__(self, name="Meshell Ndegeocello"):
        self.name = name
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Band):
    def __str__(self, name="Sheila E."):
        self.name = name
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
