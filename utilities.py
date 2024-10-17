from enum import Enum


class Config(Enum):


    PLAYERS = {

        'raw_column_name' : 'new_column_name'
    }


class Config:

    def __init__(self, func):

        self.players = {
            'UsaTodayHeadshotNoBackgroundUpdated' : func
        }