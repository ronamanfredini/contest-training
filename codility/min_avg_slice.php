<?php

function solution($A) {
    $minSumIndex = -1;
    $minSumAvg = 99999999;
    for ($i = 0; $i < count($A) - 1; $i++) {
        $twoIndexSumAvg = ($A[$i] + $A[$i + 1]) / 2;
        if ($twoIndexSumAvg < $minSumAvg) {
            $minSumIndex = $i;
            $minSumAvg = $twoIndexSumAvg;
        }

        if ($i < count($A) - 2) {
            $threeIndexSumAvg = ($A[$i] + $A[$i + 1] + $A[$i + 2]) / 3;
            if ($threeIndexSumAvg < $minSumAvg) {
                $minSumIndex = $i;
                $minSumAvg = $threeIndexSumAvg;
            }
        }
    }
    return $minSumIndex;
}

echo solution([4,2,2,5,1,5,8]);
