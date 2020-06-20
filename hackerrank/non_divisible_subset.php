<?php


function nonDivisibleSubset($k, $s) {

	$divisible = [];
	$nonDivisible = [];
	
	foreach($s as $number) {
		if (!isset($divisible[$number])) {
			array_push($nonDivisible, $number);
		}

	}


}

echo nonDivisibleSubset(3, [1,7,2,4]);
