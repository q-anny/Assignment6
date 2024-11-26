<?php
  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $integers = escapeshellarg($_POST['integers']);
    $threshold = escapeshellarg($_POST['threshold']);

    $command = "python3 bitwise_operations.py $integers $threshold";
    $result = shell_exec($command);

    echo $result;
  }
?>