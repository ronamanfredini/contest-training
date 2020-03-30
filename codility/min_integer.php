<?php

// you can write to stdout for debugging purposes, e.g.
// print "this is a debug message\n";
$foundIntegers = [];
$minNotFoundInt = 1;
function findNextMinInt() {
    global $foundIntegers,$minNotFoundInt;
    $minNotFoundInt++;
    if (!isset($foundIntegers[$minNotFoundInt])) {
        return;
    }
    return findNextMinInt();
}

function solution($A) {
    global $foundIntegers,$minNotFoundInt;
    for ($i = 0; $i < count($A); $i++) {
        $foundIntegers[$A[$i]] = true;
        if ($A[$i] == $minNotFoundInt) {
            findNextMinInt();
        }
    }
    return $minNotFoundInt;
}

echo solution([1,3,6,4,1,2]);


?>