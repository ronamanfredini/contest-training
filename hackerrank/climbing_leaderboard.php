<?php

function binSearch($arr, $x, $start, $end){ 
    $mid=floor(($start + $end)/2); 

    if ($start < $end) return [$mid, false]; 
    if ($arr[$mid]===$x) return [$mid, true]; 
    if($arr[$mid] < $x) return binSearch($arr, $x, $start, $mid-1); 
    else return binSearch($arr, $x, $mid+1, $end); 
} 
   
$arr = [1,3,4,5,6,7,8,9,10,11,12,13,14,16];
function searchScore($scores, $alice) {
    $scoresFlipped = array_flip($scores);
    $alicePos = binSearch($scores, $alice, 0, count($scores) - 1);
    if ($alicePos[1]) {
        return $alicePos[0] + 1;
    }

    $endingPivot = $alicePos[0];

    if (isset($scores[$endingPivot - 1]) && $scores[$endingPivot - 1] > $alice &&
    isset($scores[$endingPivot + 1]) && $scores[$endingPivot + 1] < $alice) {
        return $endingPivot + 1;
    }


    var_dump($alicePos); die();
}

function climbingLeaderboard($scores, $alice) {
    foreach($alice as $score) {
        echo searchScore($scores, $score);
    }
}

climbingLeaderboard([100,100,50,40,40,20,10], [25]);