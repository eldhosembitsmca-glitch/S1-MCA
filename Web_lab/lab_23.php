<?php
$students = ["Alice", "Bob", "Charlie", "Diana", "Eve"];

echo "Original Array:<br>";
//print r
print_r($students);
echo "<br><br>";

// ascending order using asort
asort($students);
echo "Array Sorted in Ascending Order:<br>";
print_r($students);
echo "<br><br>";

//descending order using arsort
arsort($students);
echo "Array Sorted in Descending Order:<br>";
print_r($students);
?>
