class Movie:

    ratings = {'G': 'kids', 'PG13': 'teenage', 'R': 'adult'}
    producer = ''

    def __init__(self, **kwargs):
        self.title = kwargs['title']
        self.year = kwargs['year']
        self.genre = kwargs['genre']
        self.rating = kwargs['ratings']

    def goodForKids(self):
        if self.rating == 'G':
            outcome = 'The movie ' + self.title + ' is good for kids.'
        if self.rating == 'PG13':
            outcome = 'The movie ' + self.title + ' is not good for kids.'
        return outcome

    def __str__(self):
        return 'The movie ' + self.title + ' is a ' + self.rating + ' movie'

    movie1 = Movie(title='Avengers', year='2018', rating='PG13')
    movie2 = Movie(title='Star Wars', year='2017', rating='G')

