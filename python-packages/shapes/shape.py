'''
.. module:: shape

Shape is a interface class. See other packages for Implementation
'''
class Shape:
    def __init__(self):
        '''
        Placeholder for Shape constructor    
        Raises:
            Exception
        '''
        raise Exception('Shape is a interface class. It cant be initialized')

    def perimeter(self):
        '''
        Perimeter for a given shape

        :raises: Exception
        '''
        raise Exception('Shape is a interface class')

    def area(self):
        '''
        Area occupied for a given shape

        :returns: float -- area of shape
        '''
        raise Exception('Shape is a interface class')

    def name(self):
        '''
        Name of the shape

        :returns: str -- name of the shape
        '''
        raise Exception('Shape is a interface class')
