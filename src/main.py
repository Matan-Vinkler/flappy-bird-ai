import neat
import os

from gnome import genome_function
from globals.constants.ml import GENERATION_NUMBER

def run(config_path: str):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, 
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))

    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(genome_function,GENERATION_NUMBER)

def main():
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "../resources/config_feedforward.txt")

    run(config_path)

if __name__ == "__main__":
    main()