<?php

function binSearch($arr, $x, $start, $end){ 
	$mid = floor(($start + $end) / 2); 

	if ($start > $end) return [$mid, false]; 
	if ($arr[$mid] === $x) return [$mid, true]; 
	if($arr[$mid] < $x) return binSearch($arr, $x, $start, $mid - 1); 
	else return binSearch($arr, $x, $mid + 1, $end); 
} 

$scoresMapped = [];

function searchScore($scores, $alice) {
	global $scoresMapped;
	$alicePos = binSearch($scores, $alice, 0, count($scores) - 1);
	$endingPivot = $alicePos[0];

	if ($alicePos[1]) {
		return $scoresMapped[$endingPivot];
	}

	if ($scores[$endingPivot] > $alice) {
		for ($i = $endingPivot; $i < count($scores) - 1; $i++) {
			if ($alice < $scores[$i] && $alice > $scores[$i + 1]) {
				return $scoresMapped[$i] + 1;
			}
		}
		return $scoresMapped[count($scoresMapped) - 1] + 1;
	}

	for ($i = $endingPivot; $i > 0; $i--) {
		if ($alice > $scores[$i] && $alice < $scores[$i - 1]) {
			return $scoresMapped[$i];
		}
	}
	return 1;
}


function climbingLeaderboard($scores, $alice) {
	global $scoresMapped;

	$scoreCounter = 1;
	$lastScore = $scores[0];
	$scoresMapped[0] = 1;
	for ($i = 1; $i < count($scores); $i++) {
		if ($scores[$i] < $lastScore) {
			$lastScore = $scores[$i];
			$scoreCounter++;
		}
		$scoresMapped[$i] = $scoreCounter;
	}

	$results = [];
	foreach($alice as $score) {
		array_push($results, searchScore($scores, $score));
	}
	return $results;
}

var_dump(climbingLeaderboard([100,100,50,40,40,20,10], [5]));
