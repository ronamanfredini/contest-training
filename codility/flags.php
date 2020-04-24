<?php

function getMaximumDivisor($n) {
	for ($i = $n - 1; $i > 1; $i--) {
		if ($n % $i == 0) {
			return $i;
		}
	}
	return 1;
}

function solution($A) {
	$peaks = [];
	for ($i = 1; $i < count($A) - 1; $i++) {
		if ($A[$i - 1] < $A[$i] && $A[$i + 1] < $A[$i]) {
			array_push($peaks, $i);
		}
	}

	$maximumFlags = count($peaks);
	if ($maximumFlags == 1) {
		return 1;
	}

	for ($maximumTempFlags = 2; $maximumTempFlags <= $maximumFlags; $maximumTempFlags++) {
		$lastSettedFlag = 0;
		$flagsAvailable = $maximumTempFlags;
		$settedFlags = 0;
		for ($i = 0; $i < $maximumFlags && $settedFlags < $maximumTempFlags; $i++) {
			if ($lastSettedFlag != 0 && $peaks[$i] - $lastSettedFlag >= $maximumTempFlags && $flagsAvailable > 0) {
				$lastSettedFlag = $peaks[$i];
				$settedFlags++;
			}

			if ($lastSettedFlag == 0) {
				$lastSettedFlag = $peaks[$i];
				$settedFlags++;
			}
		}

	}

	return $maximumFlags - $flagsAvailable;
}

echo solution([1,5,3,4,3,4,1,2,3,4,6,2]);
