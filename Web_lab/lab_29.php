<html>
<body>
    <form action="" method="POST">
        User name :<input type="text" name="my_text">
        <input type="submit" value="Send">
    </form>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $user_input = $_POST["my_text"];
        echo "user name :".$user_input;
    }
    ?>
</body>
</html>