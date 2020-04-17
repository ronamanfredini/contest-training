<?php

function solution($A) {
	$intersectCount = 0;
	$intersectedPairs = [];
	for ($i = 0; $i < count($A); $i++) {
		for ($j = 0; $j < count($A); $j++) {
			if ($i == $j)
				continue;
			if ($j + $A[$j] >= $i - $A[$i] || $j - $A[$j] <= $i + $A[$i]) {
				$intersecterPair = [$i, $j];
				sort($intersecterPair);
				$intersecterPairStr = $intersecterPair[0] . '-' . $intersecterPair[1];
				if (!isset($intersectedPairs[$intersecterPairStr])) {
					$intersectedPairs[$intersecterPairStr] = true;
					$intersectCount++;
				}
			}
		} 
	}
	if ($intersectCount > 10000000)
		return -1;

	return $intersectCount;
}

echo solution([1,5,2,1,4,0]);