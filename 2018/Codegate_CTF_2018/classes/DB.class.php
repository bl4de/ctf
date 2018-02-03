<?php
	if(!defined('simple_cms')) exit();
	class DB{
		private static $db = null;
		public static function getInstance()
    	{
        	if (null === static::$db) {
        		static::$db = mysqli_connect($GLOBALS['db_host'], $GLOBALS['db_user'], $GLOBALS['db_password'], $GLOBALS['db_name']);	
        	}
        	return static::$db;
    	}
        function insert($table, $query){
            $table = $GLOBALS['table_prefix'] . $table;

            $result = 'INSERT INTO ' . $table . ' ';

            $column = '';
            $data = '';
            foreach ($query as $key => $value) {
                $column .= '`' . $key . '`, ';
                $data .= "'{$value}', ";
            }

            $column = substr($column, 0, strrpos($column, ','));
            $data = substr($data, 0, strrpos($data, ','));

            $result .= "({$column}) VALUES ({$data})";

            $result = mysqli_query(static::$db, $result);
            return $result;
        }
        function update($table, $replace, $query, $operator=''){
            $table = $GLOBALS['table_prefix'] . $table;
            $result = 'UPDATE '.$table. ' SET ';

            foreach ($replace as $key => $value) {
                $result .= "{$key}='{$value}',";
            }
            
            $result = substr($result, 0, strrpos($result, ',')) . ' WHERE ';

            foreach ($query as $key => $value) {
                $result .= "{$key}='{$value}' {$operator} ";
            }

            if($operator){
                $result = trim(substr($result, 0, strrpos($result, $operator)));
            }
            else{
                $result = trim($result);
            }
            $result = mysqli_query(static::$db, $result);
            return $result;
        }
        function fetch_row($table, $query=array(), $operator=''){
            $table = $GLOBALS['table_prefix'] . $table;
            $result = 'SELECT * FROM '. $table;

            if($query){
                $result .=  ' WHERE ';
            
                foreach ($query as $key => $value) {
                    $result .= "{$key}='{$value}' {$operator} ";
                }
                if($operator){
                    $result = trim(substr($result, 0, strrpos($result, $operator)));
                }
                else{
                    $result = trim($result);
                }
            }
            $result = mysqli_query(static::$db, $result);
            if(!$result){
                exit(mysqli_error(static::$db));
            }
            return mysqli_fetch_array($result, MYSQLI_ASSOC);
        }
        function fetch_multi_row($table, $query=array(), $operator='', $limit='', $orderby='', $condition=''){
            $table = $GLOBALS['table_prefix'] . $table;
            $result = 'SELECT * FROM '. $table;
            if($condition){
                $result .= ' WHERE '. $condition;
            }
            else if($query){
                $result .=  ' WHERE ';
            
                foreach ($query as $key => $value) {
                    $result .= "{$key}='{$value}' {$operator} ";
                }
                if($operator){
                    $result = trim(substr($result, 0, strrpos($result, $operator)));
                }
                else{
                    $result = trim($result);
                }
            }
            else{
                $result .= ' WHERE 1 ';
            }
            if($orderby){
                $result .= ' order by '.$orderby;
            }
            if($limit){
                $result .= ' limit '. $limit;
            }            
            $result = mysqli_query(static::$db, $result);
            if(!$result){
                exit(mysqli_error(static::$db));
            }
            $tmp = array();
            $i = 0;
            while($row = mysqli_fetch_array($result, MYSQLI_ASSOC)){
                $tmp[$i] = $row;
                $i++;
            }
            return $tmp;
        }

	}
?>