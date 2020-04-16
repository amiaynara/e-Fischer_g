#!/bin/bash


# start a new enviroment this new game
cat ./games/template > ./games/current_game
rm -r ./test_images/{imc1.png,imc2.png} || true # remove the pre-existing positions
cp ./test_images/move_zero.png ./test_images/imc1.png  # restart move zero
cp ./test_images/move_zero_w.png ./test_images/imc2.png
mv_count=1 human_move=$(python human_mv_detector.py) # detect the human move 
var=$mv_count". "$human_move" "
echo $var >> ~/Projects/e-Fishcer/games/current_game # feed that move to a file called template
echo $(python next_move_finder.py)>> ~/Projects/e-Fishcer/games/current_game 
cat ./games/current_game

for((mv_count=2;mv_count<=3;mv_count++))
do
	mv ./test_images/imc1.png ./test_images/operate/ia$mv_count.png # clean the source and store the move elsewhere
	mv ./test_images/imc2.png ./test_images/operate/ib$mv_count.png
	mv ./test_images/operate/im_$((mv_count*2-1)) ./test_images/imc1.png # bring next two moves to the source
	mv ./test_images/operate/im_$((mv_count*2)) ./test_images/imc2.png
	human_move=$(python human_mv_detector.py) # detect the human move
	var=$mv_count". "$human_move" "
	echo $var >> ~/Projects/e-Fishcer/games/current_game # feed that move to a file called template
	echo $(python next_move_finder.py)>> ~/Projects/e-Fishcer/games/current_game
	cat ./games/current_game

done

rm -r ./test_images/operate/* # clean the image repository
cp  ./test_images/back_up/* ./test_images/operate/

