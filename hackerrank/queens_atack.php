<?php

// Complete the queensAttack function below.
function queensAttack($n, $k, $r_q, $c_q, $obstacles) {
    $board = array_fill(0, $n, [-1]);
    $realQueenPosition_X = $r_q - 1;
    $realQueenPosition_Y = $c_q - 1;
    $board[$realQueenPosition_X][$realQueenPosition_Y] = 1;
    
    $attackCount = 0;

    //Y
    $attackCount += abs($realQueenPosition_X - $n - 1) + $realQueenPosition_X;

    //Y
    $attackCount += abs($realQueenPosition_X - $n - 1) + $realQueenPosition_X;
}

echo queensAttack(4, 0, 4, 4, []);

