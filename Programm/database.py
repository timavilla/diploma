from sqlalchemy import create_engine, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd



SQLALCHEMY_DATABASE_URL = "sqlite:///./songs.db"

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})



class Songs(Base):
   __tablename__ = "songs"
   id = Column(Integer, primary_key=True, index=True)
   path = Column(String)
   title = Column(String)
   artist = Column(String)
   album = Column(String)
   genre = Column(String)
   year = Column(String)

Base.metadata.create_all(engine)


def to_sql():
   df = pd.read_csv(r"C:\testing\metadata.csv")
   df.to_sql(con=engine, name=Songs.__tablename__ , if_exists="append", index=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

def get_all(field):
   
   res = db.query(Songs).all()
   res_list = []
   if field == "all":
      for obj in res:
         res_list.append(f"{obj.artist} - {obj.title}")
   elif field == "artist":

      for obj in res:
         if not obj.artist in res_list:
            res_list.append(obj.artist)

   elif field == "album":
      for obj in res:
         if not obj.album in res_list:
            res_list.append(obj.album)
   
   elif field == "genre":
      for obj in res:
         if not obj.genre in res_list:
            res_list.append(obj.genre)

   elif field == "year":
      for obj in res:
         if not str(obj.year) in res_list:
            res_list.append(str(obj.year))
   

   return res_list



def get_by_artist(artist):
   res = db.query(Songs).filter(Songs.artist == artist)
   res_list = []
   for obj in res:
      res_list.append(f"{obj.artist} - {obj.title}")
   return res_list

def get_by_album(album):
   res = db.query(Songs).filter(Songs.album == album)
   res_list = []
   for obj in res:
      res_list.append(f"{obj.artist} - {obj.title}")
   return res_list

def get_by_year(year):
   res = db.query(Songs).filter(Songs.year == year)
   res_list = []
   for obj in res:
      res_list.append(f"{obj.artist} - {obj.title}")
   return res_list

def get_by_genre(genre):
   res = db.query(Songs).filter(Songs.genre == genre)
   res_list = []
   for obj in res:
      res_list.append(f"{obj.artist} - {obj.title}")
   return res_list

def to_play(name):
   res = db.query(Songs).filter(Songs.title == name).first()
   return res.path






