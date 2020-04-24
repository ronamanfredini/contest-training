<?php

function getMaxSlice($arr) {
	$maxEnding = $maxSlice = $endingIndex = 0;
	$minNum = PHP_INT_MAX;
	$starterIndex = 1;
	if (count($arr) <= 3) {
		return 0;
	}
	for ($i = 1; $i < count($arr) - 1; $i++) {
		$maxEnding = max(0, $maxEnding + $arr[$i]);
		if ($maxEnding > $maxSlice) {
			$maxSlice = $maxEnding;
			$maxEndingIndex = $i;
			$endingIndex = $i;
		} else if (!($maxEnding > $maxSlice) && $i < $endingIndex) {
			$starterIndex = $i;
		}
	}

	for ($i = $starterIndex; $i < $endingIndex; $i++) {
		if ($arr[$i] < $minNum) {
			$minNum = $arr[$i];
		}
	}
	return $maxSlice - $minNum;
}

function solution($A) {
	return getMaxSlice($A);
}

var_dump(solution([3,2,6,-1,4,5,-1,2]));
