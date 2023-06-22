<?php

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json'); // Set the response content type to JSON

$con = new mysqli("localhost", "root", "", "practice");
if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

$sql = "SELECT * FROM City";
$result = $con->query($sql);
$data = array();

if($result = mysqli_query($con, $sql))
{
  $cr = 0;
  while($row = mysqli_fetch_assoc($result))
  { 
    $data[$cr]['Id'] = $row['Id'];
    $data[$cr]['Name'] = $row['Name'];
    $data[$cr]['County'] = $row['County'];

    $cr++;
  }
}

if (!empty($data)) {
    header('Contet-Type: application/json');
    echo json_encode($data);
} else {
    echo json_encode(array('message' => 'No records found.'));
}

$con->close();
?>
