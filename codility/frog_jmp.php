<?php

function solution($X, $Y, $D) {
	 $distance = $Y - $X;
	 return intval(ceil($distance / $D));
}
