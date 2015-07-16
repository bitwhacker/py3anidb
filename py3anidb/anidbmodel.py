'''
Created on Jul 14, 2015
 
@author: beimer
'''
 
class AnidbModel(object):
    '''
    Represents a single table in the database
    '''
 
    def __init__(self, engine):
        '''
        Constructor
        '''
        self.engine = engine
       
    def get(self, key):
        '''
        Returns a single record using key
        '''
 
    def setup(self):
        pass
   
    def __repr__(self):
        str_list = ["<%s(" % self.__tablename__]
        first = True
        for column in self.__table__.columns:
            if not first:
                str_list.append(' | ')
            str_list.append(column.name + " = '" + str(getattr(self, column.name)) + "'")
            first = False
        str_list.append(")>")
        return ''.join(str_list)