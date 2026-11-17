<?php

// 1. Database Connection
$conn = mysqli_connect("localhost", "root", "", "employee_db");

// 2. Add Employee
if (isset($_POST['add'])) {

    $name = $_POST['name'];
    $dept = $_POST['department'];
    $salary = $_POST['salary'];

    $sql = "INSERT INTO employee (name, department, salary)
            VALUES ('$name', '$dept', '$salary')";

    mysqli_query($conn, $sql);

    header("Location: lab_14.php");
    exit();
}

// 3. Update Employee
if (isset($_POST['update'])) {

    $id = $_POST['id'];
    $name = $_POST['name'];
    $dept = $_POST['department'];
    $salary = $_POST['salary'];

    $sql = "UPDATE employee SET
            name='$name',
            department='$dept',
            salary='$salary'
            WHERE id=$id";

    mysqli_query($conn, $sql);

    header("Location: lab_14.php");
    exit();
}

// 4. Delete Employee
if (isset($_GET['delete'])) {

    $id = $_GET['delete'];

    $sql = "DELETE FROM employee WHERE id=$id";

    mysqli_query($conn, $sql);

    header("Location: lab_14.php");
    exit();
}

// 5. Edit Employee
$edit = false;

if (isset($_GET['edit'])) {

    $id = $_GET['edit'];

    $sql = "SELECT * FROM employee WHERE id=$id";

    $result = mysqli_query($conn, $sql);

    $row = mysqli_fetch_assoc($result);

    $edit = true;
}

// 6. Display Employee Records
$result = mysqli_query($conn, "SELECT * FROM employee");

?>


<html>
<head>
    <title>Employee Management System</title>
</head>

<body>

<h2>Employee Management System</h2>

<h3>Add / Update Employee</h3>


<form method="POST">

    <input type="hidden" name="id"
    value="<?php echo $edit ? $row['id'] : ''; ?>">

    Employee Name:

    <input type="text" name="name"
    value="<?php echo $edit ? $row['name'] : ''; ?>"
    required>

    <br><br>

    Department:

    <input type="text" name="department"
    value="<?php echo $edit ? $row['department'] : ''; ?>"
    required>

    <br><br>

    Salary:

    <input type="number" name="salary"
    value="<?php echo $edit ? $row['salary'] : ''; ?>"
    required>

    <br><br>

    <?php
    if ($edit) {
    ?>

        <input type="submit" name="update"
        value="Update Employee">

    <?php
    }
    else {
    ?>

        <input type="submit" name="add"
        value="Add Employee">

    <?php
    }
    ?>

</form>

<hr>

<!-- 8. Display Employee Records -->

<h3>Employee Records</h3>

<table border="1" cellpadding="10">

    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Department</th>
        <th>Salary</th>
        <th>Action</th>
    </tr>

    <?php

    while ($row = mysqli_fetch_assoc($result)) {

    ?>

    <tr>

        <td><?php echo $row['id']; ?></td>

        <td><?php echo $row['name']; ?></td>

        <td><?php echo $row['department']; ?></td>

        <td><?php echo $row['salary']; ?></td>

        <td>

            <a href="lab_14.php?edit=<?php echo $row['id']; ?>">
                Edit
            </a>

            |

            <a href="lab_14.php?delete=<?php echo $row['id']; ?>"
            onclick="return confirm('Are you sure?')">
                Delete
            </a>

        </td>

    </tr>

    <?php
    }
    ?>

</table>

</body>
</html>

<?php

// 9. Close Database Connection
mysqli_close($conn);

?>

