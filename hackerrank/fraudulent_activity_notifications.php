<?php

// Complete the activityNotifications function below.
function activityNotifications($expenditure, $d) {
	$notifCount = 0;
	
	for ($i = $d; $i < count($expenditure); $i++) {
		$median;
		$arr_slice = array_slice($expenditure, $i - $d, $d);

		if ($d % 2 == 0) {
			$middleIndex = count($arr_slice) / 2;
			$median = ($arr_slice[$middleIndex] + $arr_slice[$middleIndex - 1]) / 2;
		} else {
			$median = $arr_slice[intval(count($arr_slice) / 2)];
		}
		
		$valToTriggerNotification = $median * 2;
		if ($expenditure[$d] >= $valToTriggerNotification) $notifCount++;
	}
	return $notifCount;
}



echo activityNotifications([2 ,3 ,4 ,2 ,3 ,6 ,8 ,4 ,5], 5);