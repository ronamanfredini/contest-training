<?php

function minPurchases($trip_durations, $total_hours) {
    $min_purchases = 0;
    rsort($trip_durations);

    if ($trip_durations[count($trip_durations) - 1] > $total_hours) return -1;

    for ($i = 0; $i < count($trip_durations) && $total_hours > 0; $i++) {
        if ($total_hours >= $trip_durations[$i]) {
            $min_purchases += intval(floor($total_hours / $trip_durations[$i]));
            $total_hours -= intval(floor($total_hours / $trip_durations[$i])) * $trip_durations[$i];
        }
    }
    // Put your code here to calculate min_purchases
    
    // Return the result, don't change the structure
    return $min_purchases;
}