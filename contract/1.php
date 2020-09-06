<?php

function solution($T, $R) {
	$tFlipped = array_flip($T);
	$tests = [];
	$prefixEndingIndex = 0;
	$numberStartingIndex = 0;
	$numberEndingIndex = $T[0][strlen($T[0]) - 2];
	$foundFirstIndex = false;

	for ($i = 0; $i < strlen($T[0]); $i++) {
		if (is_numeric($T[0][$i])) {
			if ($foundFirstIndex == false) {
				$foundFirstIndex = true;
				$numberStartingIndex = $i;
			}

			$prefixEndingIndex = $i;
			break;
		}
	}

	foreach ($tFlipped as $key => $value) {
		$keySubst = substr($key, 0, $prefixEndingIndex + 1);
		if (!isset($tests[$keySubst])) {
			$tests[$keySubst] = $R[$value] == "OK";
		} else {
			if ($R[$value] != "OK") {
				$tests[$keySubst] = false;
			}
		}
	}

	$testsFiltered = array_filter($tests, function($a) {
		return $a === true;
	});


	return intval(floor(count($testsFiltered) * 100 / count($tests)));
}

echo solution(["test1a", "test2", "test1b", "test1c", "test3c"], ["Wrong answer", "OK", "Runtime Error", "OK", "Time limt exceeded"]);
