<?php
// Concatenation
$part1 = "Coding in ";
$part2 = "php programming";
$fullText = $part1 . $part2;
echo "1.Combined Text: " . $fullText . "<br>";

//Case Conversion
$upperText = strtoupper($fullText);
echo "2. Uppercase Text: " . $upperText . "<br>";

//String Length
$length = strlen($upperText);
echo "3. Total Characters: " . $length . "<br>";

//Word Position
$position = strpos($upperText, "PHP");
echo "4. Position of 'PHP': " . $position . "<br>";

//Substring Extraction
//Starts at position 10 and takes 11 characters
$extractedWord = substr($upperText, 10, 11);
echo "5. Extracted Word: " . $extractedWord . "<br>";
?>