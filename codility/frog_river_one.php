<?php



function solution($X, $A) {
	$rangeToJumpLeaves = [];
	for ($i = 0; $i < count($A); $i++) {
		if ($A[$i] >= 1 && $A[$i] <= $X && !isset($rangeToJumpLeaves[$A[$i]])) {
			$rangeToJumpLeaves[$A[$i]] = true;

			if (count($rangeToJumpLeaves) == $X) {
				return $i;
			}
		}
	}
	return -1;
}

echo solution(5, [1,3,1,4,2,3,5,4]);

