# Rock, paper, scissors coding challenge

1. [Overview](#overview)
2. [Setup](#setup)
3. [Approach](#approach)


## 1. Overview

This application supplies an API that allows two players to participate in a game of Rock-Paper-Scissors.


## 2. Setup

1. Ensure you have Docker installed and configured
2. From a terminal, change to the directory of this project and run the following:

    `$ docker-compose up`

3. Once the docker instances are up and running, visit the schema documenation here: http://127.0.0.1:8000/docs


## 3. Approach


Below are the list of requirements with the ones met marked as such:

- [x] Allow two players to enter their names
    - Each player supplies a name when creating a game: [Create Game](http://127.0.0.1:8000/docs#/default/create_game_game_post)
- [x] One of the players can also be the computer, i.e. player vs computer
    - When creating a game, there is the option to make `player_2` a computer player with the `is_player_2_cpu` attribute: [Create Game](http://127.0.0.1:8000/docs#/default/create_game_game_post)
- [-] Allow each to play a turn, one at a time, during which the player selects one of the option
from rock, paper, scissors
    - The API expects both player plays (`player_1_play`, `player_2_play`) to be submitted on the same request: [Create Round](http://127.0.0.1:8000/docs#/default/create_round_game__game_id__round_post)
- [x] During each turn notify who has won and increment the scores
    - The API returns the outcome of the turn or round: [Create Round](http://127.0.0.1:8000/docs#/default/create_round_game__game_id__round_post)
    - The game tally can be retrieved from the Game resource: [Get Game](http://127.0.0.1:8000/docs#/default/get_game_game__game_id__get)
- [x] In addition to implementing basic gameplay, the user must be able to save their game
    - Each turn (or round) is persisted allowing the game details to be recalled:
        - [Get Game](http://127.0.0.1:8000/docs#/default/get_game_game__game_id__get)
        - [Get Round](http://127.0.0.1:8000/docs#/default/get_round_game__game_id__round__round_id__get)


As a primarily backend engineer, I decided to focus on the API functionality to generate a good developer experience for the API consumers. I chose FastAPI and Pydantic for my implementation due to their respective strengths.

Pydantic was selected for its ease of schema declaration and the robust validation it provides, which serves as documentation for integrating clients and facilitates future maintenance. FastAPI was chosen for its lightweight nature, flexibility (it supports a "bring-your-own-library" approach), and its multi-paradigm support for both blocking and asynchronous architectures. This flexibility allows for potential retrofitting when necessary.

If provided more time, I would focus on the robustness of the application. The first priority would be to implement unit and integration tests to ensure the application meets expectations in known scenarios and can fail gracefully in unexpected situations. Additionally, I would design and implement a simple UI to serve as an example of an API consumer and better explain the user workflow I had intended. 