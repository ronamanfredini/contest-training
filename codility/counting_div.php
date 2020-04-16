<?php
function solution($A, $B, $K) {
	$includeA = $A % $K == 0? 1: 0;
	return floor(($B / $K) - ($A / $K) + $includeA);
}

echo solution(6,11,2);
