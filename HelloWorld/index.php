<html>
<body>

<?php
$size = 10;
if( isset($_POST['info'])){
  $size = $_POST['info'];
}

$my = array();
$my[8] = 10;
$my['y'] = "hi";
echo count($my);
?>

<form method="POST">
  Enter Information:<input type="string" name="info" value="<?php echo $size; ?>">
  <input type="file" name="file">
  <input type="submit">
</form>

<?php




echo '<table border="1">',"\n";
for($y = 0; $y < $size; $y++){
  echo "<tr>\n";
  for($x = 0; $x < $size; $x++){
    echo "   <td>";
    echo $x * $y;
    echo "</td>\n";
  }
  echo "</tr>\n";
}

echo "</table>\n";

?>

<image src="http://www.rd.com/wp-content/uploads/sites/2/2016/04/01-cat-wants-to-tell-you-laptop.jpg">

</body>
</html>
