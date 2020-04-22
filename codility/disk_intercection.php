<?php


function solution($A) {
	$intersectingPairsCount = 0;
	$alreadyIntersectedDisks = [];

	for ($i = 0; $i < count($A); $i++) {
		for ($j = 0; $j < count($A); $j++) {
			if ($j == $i) {
				continue;
			}

			$iPositiveLimit = $i + $A[$i];
			$iNegativeLimit = $i - $A[$i];

			$jPositiveLimit = $j + $A[$j];
			$jNegativeLimit = $j - $A[$j];

			if (
				($iPositiveLimit >= $jNegativeLimit && $jNegativeLimit >= $iNegativeLimit)
				||
				($iNegativeLimit <= $jPositiveLimit && $jPositiveLimit <= $iPositiveLimit)
				) {
				$intersectCheckerArr = [$i, $j];
				sort($intersectCheckerArr);
				$intersectCheckerStr = $intersectCheckerArr[0] . '_' . $intersectCheckerArr[1];

				if (!isset($alreadyIntersectedDisks[$intersectCheckerStr])) {
					$intersectingPairsCount++;
					$alreadyIntersectedDisks[$intersectCheckerStr] = true;
					continue;
				}
			}
		}
	}

	if ($intersectingPairsCount > 10000000) {
		return -1;
	}
	return $intersectingPairsCount;
}

echo solution([1,5,2,1,4,0]);