class Extract:

    '''
    klucz API -> .env -> dotenv library -> enviromental variables
    endpoints -> strings
    request method -> (pobiera endpoint -> waliduje output -> zwraca json object) -> try/except -> pusty JSON/throw error

    1 funkcja = 1 funkcjonalnosc -> unittest
    '''
    def __init__(self):
        self.API_KEY = None
        self.ENDPOINT_MAIN = "https://api.sportsdata.io/v3/"
        self.endpoint_matches = None
        self.endpoint_stadiums = None
        self.endpoint_teams = None


    def example_func(self):
        '''
        example description

        :param:
        :return:
        '''
        pass

