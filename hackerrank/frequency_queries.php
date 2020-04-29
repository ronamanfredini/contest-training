<?php

function freqQuery($queries) {
	$dict = [];
	$out = [];
	$frequencies = [];
	for ($i = 0; $i < count($queries); $i++) {
		$operation = $queries[$i][0];
		$number = $queries[$i][1];
		if ($operation == 1) {
			if (!isset($dict[$number])) {
				$dict[$number] = [];
			}
			$lateFrequencyCount = count($dict[$number]);
			array_push($dict[$number], $number);
			if (!isset($frequencies[count($dict[$number])])) {
				$frequencies[count($dict[$number])] = 1;
			} else {
				$frequencies[count($dict[$number])]++;
			}
			if (isset($frequencies[$lateFrequencyCount])) {
				$frequencies[$lateFrequencyCount]--;
			}
		}
		if ($operation == 2) {
			if (isset($dict[$number])) {
				$frequencies[count($dict[$number])]--;
				array_pop($dict[$number]);
				if (count($dict[$number]) > 0) {
					$frequencies[count($dict[$number])]++;
				}
			}
			
		}

		if ($operation == 3) {
			$isValid = isset($frequencies[$number]) && $frequencies[$number]>0? 1: 0;
			array_push($out, $isValid);
		}

	}
	return $out;
}
$results = [[1,3],[2,3], [3,2], [1,4], [1,5], [1,5], [1,4], [3,2], [2,4], [3,2]];
$resultStr = implode(freqQuery($results), PHP_EOL);
echo $resultStr;
