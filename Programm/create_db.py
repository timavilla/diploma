from tinytag import TinyTag
import os
import pandas as pd
import predict



def create_db(path):
    id = 1
    db_set = pd.DataFrame()

    path_vector = pd.Series()
    genre_vector = pd.Series()
    title_vector = pd.Series()
    artist_vector = pd.Series()
    album_vector = pd.Series()
    year_vector = pd.Series()

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:

            file_path = os.path.join(dirpath, f)
            genre = predict.predict_genre_of_song(file_path,f)

            tag = TinyTag.get(file_path)
            title, artist, album, year = tag.title, tag.artist, tag.album, tag.year

            path_vector.at[id] = file_path
            genre_vector.at[id] = genre
            title_vector.at[id] = title
            artist_vector.at[id] = artist
            album_vector.at[id] = album
            year_vector.at[id] = year
            id+=1

    db_set["path"] = path_vector
    db_set["genre"] = genre_vector
    db_set["title"] = title_vector
    db_set["artist"] = artist_vector
    db_set["album"] = album_vector
    db_set["year"] = year_vector

    db_set.to_csv("metadata.csv", index_label="id")
    

if __name__ == "__main__":
    create_db(r'C:\Users\Timavilla\Downloads\tima')