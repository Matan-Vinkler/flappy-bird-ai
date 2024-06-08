# Automated Flappy Bird with Genetic Algorithm

This project implements an automated Flappy Bird game using a genetic algorithm to train the bird to play. The project demonstrates the use of genetic algorithms for training agents in a game environment.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Flappy Bird game is a simple yet challenging game where the player controls a bird that must navigate through pipes without crashing. In this project, a genetic algorithm is used to evolve a population of birds, enabling them to learn and improve their performance over generations.

## Installation

To run this project, you need to have Python installed on your machine. You can install the required dependencies using `pip` and the `requirements.txt` file provided.

1. Clone the repository:
    ```bash
    git clone flappy-bird-ai.git
    cd flappy-bird-ai
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the game and watch the genetic algorithm in action, simply run the following command:

```bash
python src/main.py
```
The program will initialize a population of birds and begin the training process, displaying the progress in real-time.

## Dependencies
The project dependencies are listed in the requirements.txt file. Here are some of the key libraries used:

`pygame`: For rendering the Flappy Bird game.

`neat-python`: For implementing the genetic algorithm.

You can install all dependencies with:

```bash
pip install -r requirements.txt
```

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.