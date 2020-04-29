<?php

function checkMagazine($magazine, $note) {
    $magazineAvailableWords = [];

    foreach($magazine as $word) {
        if (!isset($magazineAvailableWords[$word])) {
            $magazineAvailableWords[$word] = 0;
        }
        $magazineAvailableWords[$word]++;
    }

    $wordCount = count($note);
    foreach ($note as $word) {
        if (!isset($magazineAvailableWords[$word])) {
            break;
        }
        if($magazineAvailableWords[$word] > 0) {
            $magazineAvailableWords[$word]--; $wordCount--;
        }
    }
    if ($wordCount == 0) {
        echo "Yes";
        return;
    }
    echo 'No';
}

checkMagazine("ive got a lovely bunch of coconuts", "ive got some coconuts");
