'''
Created on Jul 14, 2015
 
@author: beimer
'''
 
from sqlalchemy import Column, Integer, String, Date, Binary, Float
from py3anidb.anidbmodel import AnidbModel
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
 
class Anime(AnidbModel, Base):
    '''
    Represents a single table in the database
    '''
    __tablename__ = 'anime'
    anidb_id = Column(Integer, primary_key = True)
    series_name = Column(String)
 
    episode_count = Column(Integer)
 
    start_date = Column(Date)
    poster = Column(Binary)
    description = Column(String)
    rating = Column(Float)