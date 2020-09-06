<?php

// you can write to stdout for debugging purposes, e.g.
// print "this is a debug message\n";

function solution($A) {
	$smallestNotFoundInteger = 1;
	if (max($A) <= 0) return $smallestNotFoundInteger;

	sort($A);
	for($i = 0; $i < count($A); $i++) {
		if ($A[$i] <= 0) continue;
		if ($A[$i] == $smallestNotFoundInteger) {
			$smallestNotFoundInteger = $A[$i] + 1;
		}
	}

	return $smallestNotFoundInteger;
}

echo solution([1,3,6,4,1,2]);