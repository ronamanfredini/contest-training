<?php

function twoStrings($s1, $s2) {
    $hash = [];
    for ($i = 0; $i < strlen($s1); $i++) {
        $hash[$s1[$i]] = true;
    }
    for ($i = 0; $i < strlen($s2); $i++) {
        if(isset($hash[$s2[$i]]) && $hash[$s2[$i]])
            return "YES";
    }
    return "NO";
}

echo twoStrings('hello', 'world');