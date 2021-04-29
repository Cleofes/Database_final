<!DOCTYPE html>
<html>
<head>
<title>Final Project</title>
</head>
<body>
<h1>Cleofes Sarmiento Final Project</h1>
<!Collect input from web user!> 
<form method="post" action="<?php echo $_SERVER['PHP_SELF'];?>">
	Enter the name of the annotated JE-2 gene you are looking for: <input type="text" name="name">
	<input type="submit">
</form>
<?php
$name = "empty";
/*process input from web user */
// Checks to see the condition of the text boxes.
if ($_SERVER["REQUEST_METHOD"] == "POST"){
	// collect value of input field
	$name = $_POST['name'];
	echo "<br>";
	if (empty($name)) {
		}   	
			 	
	elseif (!empty($name)){	
		echo "Name provided was $name.<br/>";
	}
}
/*Connection variables at top
* Makes it easy to change if needed*/
$server="localhost";
$username="Enter username here";
$password="";
$database="Name of Database";
/*Connect to my database
* and throw errors if its unable to connect.
* Greets the web user if it is able to connect.*/
$connect = mysqli_connect($server,$username,"",$database);
if($connect->connect_error){
	echo "Something has gone terribly wrong";
	echo "Connection error:" .$connect->connect_error;
}else{
	echo "<br/>";
}
/* Run a basic SQL query and throw
 * an error if its unable to perform the query
 */
$query = "SELECT qualifier FROM S_aureus_JE2 WHERE name =\"". $name ."\"";
$result = mysqli_query($connect, $query) 
	  or trigger_error("Query Failed! SQL: $query - Error: "
	  . mysqli_error($connect), E_USER_ERROR);
//echo "Query is: $query <br>";

/*If there are results from the query, print the 0th
 * token in the current tuple from the result relation
 * If there are no results, print an error message.
 */ 
// Displays the results of the query.
if ($result = mysqli_query($connect, $query)) {
    while ($row = mysqli_fetch_row($result)) {
        echo ("The results for " . $name." are:". $row[0]);
    }
    mysqli_free_result($result);
}else{
	echo "No results";
}

/*Always close your connection. 
 * Its a courtesy to your fellow users.
 */
mysqli_close($connect);
?>
</body>
</html>
