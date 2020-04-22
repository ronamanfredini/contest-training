<?php

function solution($A) {
	$passingCarsCount = 0;
	$zerosCount = 0;
	for ($i = 0; $i < count($A); $i++) {
		if ($A[$i] == 0) {
			$zerosCount++;
		} else {
			$passingCarsCount += $zerosCount;
		}
	}


	if ($passingCarsCount > 1000000000) {
		return -1;
	}
	return $passingCarsCount;
}


echo solution([0,1,0,1,1]);