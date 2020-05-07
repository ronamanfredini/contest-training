<?php

function solution($A) {
	$peaks = [];
	$distances = 0;

	for ($i = 1; $i < count($A) - 1; $i++) {
		if ($A[$i - 1] < $A[$i] && $A[$i] > $A[$i + 1]) {
			if (count($peaks) != 0) {
				$distances += abs($peaks[count($peaks) - 1] - $i);
			}
			array_push($peaks, $i);
		};
	}

	if (count($peaks) == 0) return 0;
	if ($distances == 0) return 1;

	$totalFlagsToPut = $flagsRemaining = intval(sqrt($peaks[count($peaks) - 1] - $peaks[0]) + 1);

	$lastFlagPutOn = -1;
	foreach ($peaks as $peak) {
		if ($flagsRemaining == 0) break;
		if (($lastFlagPutOn == -1 || abs($lastFlagPutOn - $peak) >= $totalFlagsToPut)) {
			$lastFlagPutOn = $peak;
			$flagsRemaining--;
		}
	}
	return intval($totalFlagsToPut - $flagsRemaining);
}

// echo solution([1,5,3,4,3,4,1,2,3,4,6,2]);
echo solution([1,2,1,2,1,2]);
