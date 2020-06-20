<?php

function twoPluses($grid) {
	for ($i = 1; $i < count($grid) - 1; $i++) {
		for ($j = 1;$j < strlen($grid[$i][0]) - 1; $j++) {
			$char = $grid[$i][0][$j];
			if ($char == 'G') {
				
			}
			echo $grid[$i][0][$j];
		}
		echo PHP_EOL;
	}
}

echo twoPluses([['BGBBGB'],
				['GGGGGG'],
				['BGBBGB'],
				['GGGGGG'],
				['BGBBGB'],
				['BGBBGB']]);