<?php

$geometricProgressionSavings = [];

function searchForGeometricProgressionSuccessor($vector, $startingNumberIndex, $progressionLevel, $progressionRate) {
    global $geometricProgressionSavings;
    $numberBeingAnalyzed = $vector[$startingNumberIndex];
    $targetNumber  = $numberBeingAnalyzed * $progressionRate;
    if ($progressionLevel >= 3) return true;

    if (isset($geometricProgressionSavings[$numberBeingAnalyzed])) {
        return searchForGeometricProgressionSuccessor($vector, $geometricProgressionSavings[$numberBeingAnalyzed][1], ++$progressionLevel, $progressionRate);
    }

    for ($i = $startingNumberIndex + 1; $i < count($vector); $i++) {
        if ($vector[$i] == $targetNumber) {
            $geometricProgressionSavings[$numberBeingAnalyzed] = [$targetNumber, $i];
            return searchForGeometricProgressionSuccessor($vector, $i, ++$progressionLevel, $progressionRate);
        }
    }
    return false;
}
function countTriplets($arr, $r) {
    $tripletCount = 0;
    for ($i = 0; $i < count($arr); $i++) {
        $tripletCount += searchForGeometricProgressionSuccessor($arr, $i, 1, $r)? 1: 0;
    }
    return $tripletCount;
}


echo countTriplets([1,2,2,4], 2);

