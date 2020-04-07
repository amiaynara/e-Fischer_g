#!/bin/bash


result=0

mv_count=1
human_move=$(python human_mv_detector.py)
var=$mv_count". "$human_move" "
echo $var >> ~/Projects/e-Fishcer/template
echo $(python next_move_finder.py)>> ~/Projects/e-Fishcer/template
cat template
cat temp > template
