<?php

function countingValleys($n, $s) {
	$levelCounter = $valleyCounter = 0;

	$enteredValley = false;
	for ($i = 0; $i < $n; $i++) {
		if ($s[$i] == 'U') {
			$levelCounter++;
			if ($levelCounter >= 0 && $enteredValley) {
				$enteredValley = false;
			}
		} else {
			$levelCounter--;
			if ($levelCounter < 0 && !$enteredValley) {
				$enteredValley = true;
				$valleyCounter++;
			}
		}
	}

	return $valleyCounter;
}

echo countingValleys(8, 'UDDDUDUU');