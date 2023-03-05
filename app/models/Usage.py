class Usage(object):
    def __init__(self, name, percentage: int, description='') -> None:
        """
        A class representing resource usage data, including the name of the resource, 
        the percentage of usage, and an optional description.
        
        :param name: A string representing the name of the resource.
        :param percentage: An integer representing the percentage of resource usage.
        :param description: An optional string describing the resource usage.
        """
        self.name = name
        self.description = description
        
        # Create a list of dictionaries representing the usage data for the resource
        self.data = [
            {'name': 'available', 'percentage': (100-percentage)/100},
            {'name': 'used', 'percentage': (percentage)/100}]
        
    def get_data(self):
        """
        Returns the usage data for the resource as a list of dictionaries.
        
        :return: A list of dictionaries representing the usage data for the resource.
        """
        return self.data
