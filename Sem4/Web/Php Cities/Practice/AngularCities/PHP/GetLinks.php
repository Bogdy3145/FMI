<?php

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json'); // Set the response content type to JSON

$con = new mysqli("localhost", "root", "", "practice");
if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

$sql = "SELECT * FROM Link";
$result = $con->query($sql);
$data = array();

if($result = mysqli_query($con, $sql))
{
  $cr = 0;
  while($row = mysqli_fetch_assoc($result))
  { 
    $data[$cr]['Id'] = $row['Id'];
    $data[$cr]['CityId1'] = $row['CityId1'];
    $data[$cr]['CityId2'] = $row['CityId2'];
    $data[$cr]['Distance'] = $row['Distance'];
    $data[$cr]['Duration'] = $row['Duration'];

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
