<?php

function solution($A) {
	$permutation = [];
	$maxValue = max($A);
	for ($i = 0; $i < count($A); $i++) {
		if ($A[$i] >= 1 && $A[$i] <= $maxValue && !isset($permutation[$A[$i]])) {
			$permutation[$A[$i]] = true;
		} else {
			return 0;
		}
	}
	if (count($permutation) == $maxValue)
		return 1;
	return 0;
}


echo solution([4,1,2,2,3]);