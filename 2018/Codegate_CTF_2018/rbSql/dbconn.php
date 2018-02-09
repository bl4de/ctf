<?php
/*
Table[
  tablename, filepath
  [column],
  [row],
  [row],
  ...
rbSqlSchema[
  rbSqlSchema,/rbSqlSchema,
  ["tableName","filePath"],
  ["something","/rbSql_".substr(md5(rand(10000000,100000000)),0,16)]
]
*/

define("STR", chr(1), true);
define("ARR", chr(2), true);
define("SCHEMA", "../../rbSql/rbSqlSchema", true);

function rbSql($cmd,$table,$query){
	switch($cmd){
	case "create":
		$result = rbReadFile(SCHEMA);
		for($i=3;$i<count($result);$i++){
			if(strtolower($result[$i][0]) === strtolower($table)){
				return "Error6";
			}
		}
		$fileName = "../../rbSql/rbSql_".substr(md5(rand(10000000,100000000)),0,16);
		$result[$i] = array($table,$fileName);
		rbWriteFile(SCHEMA,$result);
		exec("touch {$fileName};chmod 666 {$fileName}");
		$content = array($table,$fileName,$query);
		rbWriteFile($fileName,$content);
		break;

	case "select":
		/*
		  Error1 : Command not found
		  Error2 : Column not found
		  Error3 : Value not found
		  Error4 : Table name not found
		  Error5 : Column count is different
		  Error6 : table name duplicate
		*/
		$filePath = rbGetPath($table);
		if(!$filePath) return "Error4";
		$result = rbReadFile($filePath);
		$whereColumn = $query[0];
		$whereValue = $query[1];
		$countRow = count($result) - 3;
		$chk = 0;
		for($i=0;$i<count($result[2]);$i++){
			if(strtolower($result[2][$i]) === strtolower($whereColumn)){
				$chk = 1;
				break;
			}
		}
		if($chk == 0) return "Error2";
		$chk = 0;
		for($j=0;$j<$countRow;$j++){
			if(strtolower($result[$j+3][$i]) === strtolower($whereValue)){
				$chk = 1;
				return $result[$j+3];
			}
		}
		if($chk == 0) return "Error3";
		break;

	case "insert":
		$filePath = rbGetPath($table);
		if(!$filePath) return "Error4";
		$result = rbReadFile($filePath);
		if(count($result[2]) != count($query)) return "Error5";
		$result[count($result)] = $query;
		rbWriteFile($filePath,$result);
		break;

	case "delete":
		$filePath = rbGetPath($table);
		if(!$filePath) return "Error4";
		$result = rbReadFile($filePath);
		$whereColumn = $query[0];
		$whereValue = $query[1];
		$countRow = count($result) - 3;
		$chk = 0;
		for($i=0;$i<count($result[2]);$i++){
			if(strtolower($result[2][$i]) === strtolower($whereColumn)){
				$chk = 1;
				break;
			}
		}
		if($chk == 0) return "Error2";
		$chk = 0;
		for($j=0;$j<$countRow;$j++){
			if(strtolower($result[$j+3][$i]) === strtolower($whereValue)){
				$chk = 1;
				unset($result[$j+3]);
			}
		}
		if($chk == 0) return "Error3";
		rbWriteFile($result[1],$result);
		break;

	default:
		return "Error1";
		break;
	}
}

function rbParse($rawData){
	$parsed = array();
	$idx = 0;
	$pointer = 0;

	while(strlen($rawData)>$pointer){
		if($rawData[$pointer] == STR){
			$pointer++;
			$length = ord($rawData[$pointer]);
			$pointer++;
			$parsed[$idx] = substr($rawData,$pointer,$length);
			$pointer += $length;
		}
		elseif($rawData[$pointer] == ARR){
			$pointer++;
			$arrayCount = ord($rawData[$pointer]);
			$pointer++;
			for($i=0;$i<$arrayCount;$i++){
				if(substr($rawData,$pointer,1) == ARR){
					$pointer++;
					$arrayCount2 = ord($rawData[$pointer]);
					$pointer++;
					for($j=0;$j<$arrayCount2;$j++){
						$pointer++;
						$length = ord($rawData[$pointer]);
						$pointer++;
						$parsed[$idx][$i][$j] = substr($rawData,$pointer,$length);
						$pointer += $length;
					}
				}
				else{
					$pointer++;
					$length = ord(substr($rawData,$pointer,1));
					$pointer++;
					$parsed[$idx][$i] = substr($rawData,$pointer,$length);
					$pointer += $length;
				}
			}
		}
		$idx++;
		if($idx > 2048) break;
	}
	return $parsed[0];
}

function rbPack($data){
	$rawData = "";
	if(is_string($data)){
		$rawData .= STR . chr(strlen($data)) . $data;
	}
	elseif(is_array($data)){
		$rawData .= ARR . chr(count($data));
		for($idx=0;$idx<count($data);$idx++) $rawData .= rbPack($data[$idx]);
	}
	return $rawData;
}

function rbGetPath($table){
	$schema = rbReadFile(SCHEMA);
	for($i=3;$i<count($schema);$i++){
		if(strtolower($schema[$i][0]) == strtolower($table)) return $schema[$i][1];
	}
}

function rbReadFile($filePath){
	$opened = fopen($filePath, "r") or die("Unable to open file!");
	$content = fread($opened,filesize($filePath));
	fclose($opened);
	return rbParse($content);
}

function rbWriteFile($filePath,$fileContent){
	$opened = fopen($filePath, "w") or die("Unable to open file!");
	fwrite($opened,rbPack($fileContent));
	fclose($opened);
	clearstatcache();
}

