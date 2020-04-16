<?php

function solution($A) {
	$aLength = count($A) + 1;

	$expectedSum = $aLength * ($aLength +1) / 2;
	$gotValue = array_sum($A);

	return $expectedSum - $gotValue;
}

echo solution([2,3,1,5]);
