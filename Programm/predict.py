import feature_extraction
import warnings
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
from pydub import AudioSegment
warnings.filterwarnings("ignore")

def predict_genre_of_song(file_path,f):
    


    

    
    sound = AudioSegment.from_mp3(file_path)
    sound.export(fr"C:\testing\wav_songs\{f[:-4]}.wav" , format="wav")
    path_to_wav = fr"C:\testing\wav_songs\{f[:-4]}.wav"

    
    print('\n Extracting features of selected song : {0}'.format(path_to_wav))
    feature_extraction.extract_feature(path_to_wav)
    
    #unpickling our object
    infile = open('svm_classifier','rb')
    new_clf = pickle.load(infile)
    infile.close()
    
    #finding genre of our song
    original_dataset = pd.read_csv(r'C:\testing\yandex.csv').values[:,2:]
    original_dataset = original_dataset
    new_song_data = pd.read_csv(r'C:\testing\song_genre.csv').values[:,1:]
    
    X = np.concatenate((original_dataset,new_song_data))
    
    #scaling our features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    genre = new_clf.predict(X[-1:])
    return genre
    
    print('\ngenre of Song is : {0}'.format(genre))
    



if __name__ == "__main__":
    predict_genre_of_song(r"C:\Users\Timavilla\Downloads\tima")