<?php
include 'lab_15_1.php';

$search_title = $_GET['search_title'];

// Using LIKE with % allows partial title matches
$sql = "SELECT * FROM books WHERE title LIKE '%$search_title%'";
$result = mysqli_query($conn, $sql);

echo "<h2>Search Results</h2>";

if (mysqli_num_rows($result) > 0) {
    echo "<table border='1' cellpadding='10'>
            <tr>
                <th>Accession Number</th>
                <th>Title</th>
                <th>Authors</th>
                <th>Edition</th>
                <th>Publisher</th>
            </tr>";

    while ($row = mysqli_fetch_assoc($result)) {
        echo "<tr>
                <td>" . $row['accession_no'] . "</td>
                <td>" . $row['title'] . "</td>
                <td>" . $row['authors'] . "</td>
                <td>" . $row['edition'] . "</td>
                <td>" . $row['publisher'] . "</td>
              </tr>";
    }
    echo "</table>";
} else {
    echo "<p>No books found matching that title.</p>";
}

echo "<br><a href='lab_15.html'>Go Back</a>";

mysqli_close($conn);
?>