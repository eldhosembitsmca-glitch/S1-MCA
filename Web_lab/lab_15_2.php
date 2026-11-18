<?php
include 'lab_15_1.php';

$acc_no    = $_POST['accession_no'];
$title     = $_POST['title'];
$authors   = $_POST['authors'];
$edition   = $_POST['edition'];
$publisher = $_POST['publisher'];

$sql = "INSERT INTO books (accession_no, title, authors, edition, publisher) 
        VALUES ('$acc_no', '$title', '$authors', '$edition', '$publisher')";

if (mysqli_query($conn, $sql)) {
    echo "<h3>Book details added successfully!</h3>";
} else {
    echo "Error: " . mysqli_error($conn);
}

echo "<br><a href='lab_15.html'>Go Back</a>";

mysqli_close($conn);
?>