class Band:
    """Create a Band class"""
    def __init__(self, name):
        """Initialize a Band"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add musician to musicians list"""
        self.musicians.append(musician)

    def play(self):
        """Print musician playing instrument"""
        for musician in self.musicians:
            print(musician.play())

    def __str__(self):
        """Return musicians string"""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"
