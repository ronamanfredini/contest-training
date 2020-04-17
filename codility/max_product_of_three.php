<?php

function solution($A) {
	sort($A);
	$aLength = count($A);
	
	$firstMultiply = $A[$aLength - 3] * $A[$aLength - 2];
	if ($A[0] < 0 && $A[1] < 0 && abs($A[0] + $A[1]) > $A[$aLength - 2] + $A[$aLength - 3] && $A[$aLength - 1] > 0) {
		$firstMultiply = $A[0] * $A[1];
	}
	return $firstMultiply *  $A[$aLength - 1];
}

echo solution([4,7,3,2,1,-3,-5]);