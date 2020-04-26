<?php

function countTriplets($arr, $r) {
    $possibleTripletDict = [];
    for ($i = 0; $i < count($arr); ++$i) {
        if (!isset($possibleTripletDict[$arr[$i]])) {
            $possibleTriplet1 = [$arr[$i] => true, $arr[$i] * $r => false, $arr[$i] * $r * $r => false];
            $possibleTriplet2 = [$arr[$i] / $r => false, $arr[$i] => true, $arr[$i] * $r => false];
            $possibleTriplet3 = [($arr[$i] / $r) / $r => false, $arr[$i] / $r => false, $arr[$i] => true];
            $possibleTripletDict[$arr[$i]] = [$possibleTriplet1, $possibleTriplet2, $possibleTriplet3];
        } else {

        }
    }
}


