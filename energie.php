<?php
$link = mysqli_connect("127.0.0.1", "root", "password", "emoncms");
$query = "SELECT data FROM feed_16 ORDER BY time DESC limit 1;";
$query .= "SELECT data FROM feed_17 ORDER BY time DESC limit 1;";
$query .= "SELECT data FROM feed_18 ORDER BY time DESC limit 1;";
$query .= "SELECT data FROM feed_38 ORDER BY time DESC limit 1;";
$query .= "SELECT data FROM feed_39 ORDER BY time DESC limit 1;";
$query .= "SELECT data FROM feed_22 ORDER BY time DESC limit 1";
if (mysqli_multi_query($link, $query))
{
  do
  {
    if ($result = mysqli_store_result($link))
    {
      while ($row = mysqli_fetch_array($result))
      {
      	echo $row['data'];
        echo (",");
      }
      mysqli_free_result($result);
    }
  }
  while (mysqli_next_result($link));
}
?>
