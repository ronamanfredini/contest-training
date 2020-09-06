<?php

function solution($A) {
	$startFound = 0;
	$endFound = 1;
	$found = [];

	$leastEndFound = $leastStartFound = 0;
	for ($i = 0; $i < count($A); $i++) {
		if ($i > 0 && $A[$startFound] == $A[$i]) {  
			$endFound = ++$startFound;
		} 
		else if (!isset($found[$A[$i]])) { 
			$endFound = $i;
		}
		$found[$A[$i]] = true;
	}
	return $endFound - $startFound + 1;
}

echo solution([7,3,7,3,1,3,4,1]);
