// Complete the sockMerchant function below.
function subtractionCount($integer) {
    $divisorCount = 0;
    for ($i = $integer; $i >= 1; $i -= 2) {
        if ($i != 1)
            $divisorCount++;
    }
    return $divisorCount;
}



function sockMerchant($n, $ar) {
    $socksGrouped = [];
    foreach ($ar as $sock) {
        if (!isset($socksGrouped[$sock])) {
            $socksGrouped[$sock] = 0; 
        }
        $socksGrouped[$sock]++;
    }
    $sockCount = 0;
    foreach ($socksGrouped as $sock) {
        $subtractionCount = subtractionCount($sock);
        $sockCount += $subtractionCount;
    }
    return $sockCount;
}
