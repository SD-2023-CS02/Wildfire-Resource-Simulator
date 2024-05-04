from tanker_fire_proximity import *
from db_retrieval import *

bases, fires = connect_to_db()

calculator = ProximityCalculator()
calculator.load_data(fires, bases)
calculator.fire_distances()
calculator.average()
