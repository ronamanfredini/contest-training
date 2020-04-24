<?php

function solution($A) {
	$indexTracker = [];
	for ($i  = 0; $i < count($A); $i++) {
		if (!isset($indexTracker[$A[$i]])) {
			$indexTracker[$A[$i]] = [$i];
		} else {
			array_push($indexTracker[$A[$i]], $i);
		}
	}
	var_dump($indexTracker);die();
	$dominatorCount = count($A) / 2;
	foreach ($indexTracker as $key => $value) {
		if (count($value) > $dominatorCount) {
			return $value[0];
		}
	}
	return -1;
}

var_dump(solution([3,2,3,4,3,3,3,-1]));
