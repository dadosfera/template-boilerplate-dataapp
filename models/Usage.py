class Usage(object):
    def __init__(self, name, percentage: int, description='') -> None:
        self.name = name
        self.description = description
        self.data = [
            {'name': 'available', 'percentage': (100-percentage)/100},
            {'name': 'used', 'percentage': (percentage)/100}]
        
    def get_data(self):
        return self.data
