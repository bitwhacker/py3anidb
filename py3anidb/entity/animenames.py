'''
Created on Jul 14, 2015
 
@author: beimer
'''
from sqlalchemy import Column, Integer, String
from py3anidb.anidbmodel import AnidbModel
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
 
class AnimeNames(AnidbModel, Base):
    '''
    Represents a single table in the database
    '''
    __tablename__ = 'anime_names'
    anidb_id = Column(Integer, primary_key = True)
    name_type = Column(Integer)
    season_number = Column(Integer)
    name = Column(String)