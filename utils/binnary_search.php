<?php

function binarySearch($array, $value) {
    $left = 0;
    $right = count($array) - 1;
 
    while ($left <= $right) {
      $midpoint = (int) floor(($left + $right) / 2);
 
      if ($array[$midpoint] < $value) {
        $left = $midpoint + 1;
      } elseif ($array[$midpoint] > $value) {
        $right = $midpoint - 1;
      } else {
        return $midpoint;
      }
    }
    return false;
}