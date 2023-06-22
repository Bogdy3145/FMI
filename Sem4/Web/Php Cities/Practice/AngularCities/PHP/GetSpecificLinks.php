<?php

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
header('Content-Type: application/json'); // Set the response content type to JSON

$con = new mysqli("localhost", "root", "", "practice");
if (!$con) {
    die('Could not connect: ' . mysqli_error());
}

$filterId = isset($_GET['id']) ? $_GET['id'] : '';

#$sql = "SELECT * FROM Link WHERE CityId1 LIKE '%$filterId%' OR CityId2 LIKE '%$filterId%'";
$sql = "SELECT City.Name, City.Id, 
         CASE
            WHEN Link.CityId1 != '$filterId' THEN City.Id
            ELSE OtherCity.Id
         END AS CityId,
         CASE
            WHEN Link.CityId1 != '$filterId' THEN City.Name
            ELSE OtherCity.Name
         END AS CityName
         FROM Link
         INNER JOIN City ON City.Id = Link.CityId1
         INNER JOIN City AS OtherCity ON OtherCity.Id = Link.CityId2
         WHERE Link.CityId1 LIKE '%$filterId%' OR Link.CityId2 LIKE '%$filterId%'";


$result = $con->query($sql);
$data = array();

if($result = mysqli_query($con, $sql))
{
  $cr = 0;
  while($row = mysqli_fetch_assoc($result))
  { 
    $data[$cr]['Name'] = $row['CityName'];
    $data[$cr]['Id'] = $row['CityId'];
    // $data[$cr]['CityId1'] = $row['CityId1'];
    // $data[$cr]['CityId2'] = $row['CityId2'];
    // $data[$cr]['Distance'] = $row['Distance'];
    // $data[$cr]['Duration'] = $row['Duration'];

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
