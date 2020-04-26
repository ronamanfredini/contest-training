<?php

function solution($A) {
    $sums = [];
    $sums[0] = $A[0];
    for ($i = 1; $i < count($A); $i++) {
        $toSum = 1;
        if ($A[$i] == 0) {
            $toSum = -1;
        }
        $sums[$i] = $sums[$i - 1] + $toSum;
    }
    var_dump($sums); die();
}


echo solution([0,1,0,1,1]);
