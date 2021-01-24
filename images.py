"""

Using a database from nasa to upload photos to instagram

Database link: https://www.datastro.eu/explore/dataset/nasahubble/

"""


import pandas as pd
import requests
import random
import os

class Photos():

    def __new__(cls, *args, **kwargs):

        cls.dataset_nasa = 'files/nasahubble.csv'

        return super().__new__(cls)

    def __init__(self, name):

        self.__name = name + '.jpg'

    @property
    def name(self):

        return self.__name

    @classmethod
    def get_photo(cls):

        df_photo = pd.read_csv(cls.dataset_nasa, sep=';')

        rndn_index = random.randint(0, len(df_photo))

        photo_url = df_photo['Photo URL'].unique().tolist()[rndn_index]

        # Only when the file is ready
        df_photo.drop(df_photo.index[rndn_index])
        df_photo.to_csv(f'{cls.dataset_nasa}', sep=';')

        return photo_url

    def download_photo(self):

        p_url = Photos.get_photo()

        requsts = requests.get(p_url)

        with open(f'images/{self.__name}', 'wb') as f:

            f.write(requsts.content)

    def remove_images(self):

        os.remove(self.__name)