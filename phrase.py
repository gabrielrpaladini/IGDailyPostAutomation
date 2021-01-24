"""Using Wiki Quote API to generate quotes from famous philosophers

List need to be increased"""

import wikiquote
import random


class Quote():

    def __init__(self):

        self.famous_philosophers = ['Tomas Aquinas', 'Aristotle', 'Confucius', 'René Descartes', 'Ralph Waldo Emerson'
                                    , 'Michael Focault', 'David Hume', 'Immanuel Kant', 'Lao-Tzu', 'John Locke', 'Niccolo Machiavelli'
                                    , 'Karl Marx', 'John Stuart Mill', 'Friedrich Nietzsche', 'Plato', 'Jean-Jacques Rousseau', 'Jean-Paul Sartre'
                                    , 'Socrates']

    def get_quote(self):

        rndn = random.randint(0, len(self.famous_philosophers))

        philosopher = self.famous_philosophers[rndn]

        quote = wikiquote.quotes(philosopher)[0]     

        quote = quote + " - " + philosopher 

        return quote  