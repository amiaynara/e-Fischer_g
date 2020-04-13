#!/bin/bash


# start a new enviroment this new game
cat ./games/template > ./games/current_game



mv_count=1
human_move=$(python human_mv_detector.py) # detect the human move
var=$mv_count". "$human_move" "
echo $var >> ~/Projects/e-Fishcer/games/current_game # feed that move to a file called template
echo $(python next_move_finder.py)>> ~/Projects/e-Fishcer/games/current_game

cat ./games/current_game
