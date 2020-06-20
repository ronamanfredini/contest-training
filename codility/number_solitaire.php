<?php

function solution($A) {
	$sum = $A[0] + $A[count($A) - 1];
	$i = 1;
	while ($i < count($A)) {
		$sliceLength = 6;
		if ($i + $sliceLength > count($A) - 1) {
			$sliceLength = count($A) - 1 - $i;
		}

		$slice = array_slice($A, $i, $sliceLength, true);

		$nextVal = max($slice);
		$nextKey = array_keys($slice, $nextVal)[0];

		$sum += $nextVal;
		$i = $nextKey;
	}
	return $sum;
}

echo solution([1,-2,0,9,-1,-2, 8, 5,2,1,6,7]);
