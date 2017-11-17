<?php if(!defined('APP')) { die('직접 접근 금지'); }

$ip = $_SERVER['HTTP_CLIENT_IP'] ?: ($_SERVER['HTTP_X_FORWARDED_FOR'] ?: $_SERVER['REMOTE_ADDR']);

function ip_in_range($ip, $min, $max) {
    return (ip2long($min) <= ip2long($ip) && ip2long($ip) <= ip2long($max));
}

if(ip_in_range($ip, '175.45.176.0', '175.45.179.255') ||
   ip_in_range($ip, '210.52.109.0', '210.52.109.255') ||
   ip_in_range($ip, '77.94.35.0', '77.94.35.255')) {

    if (!isset($_SERVER['PHP_AUTH_USER'])) {
        header('HTTP/1.0 401 Unauthorized');
        header('WWW-Authenticate: Basic realm="LOGIN"');
    } else {
        $login = $_SERVER['PHP_AUTH_USER'];
        $password = $_SERVER['PHP_AUTH_PW'];

        $db = new PDO('sqlite:database.sqlite3');

        $result = $db->query("select login, password from users where login = '$login'");
        if (!$result) { die($db->errorInfo()[2]); }
        $data = $result->fetchAll();

        if(count($data) == 0) {
            header('HTTP/1.0 401 Unauthorized');
            header('WWW-Authenticate: Basic realm="NO USER"');
        } elseif (md5($password) !== $data[0]['password']) {
            header('HTTP/1.0 401 Unauthorized');
            header('WWW-Authenticate: Basic realm="WRONG PASSWORD"');
        } else {
            print '<h2>안녕하십니까</h2>';

            $result = $db->query("select message from instructions where login = '{$data[0]['login']}'");
            if (!$result) { die($db->errorInfo()[2]); }
            $data = $result->fetchAll();

            if(count($data) == 0) {
                print('<h3>메시지 없음</h3>');
            } else {
                print '<h3>여기에 당신을위한 메시지가 있습니다.:</h3>';

                foreach($data as $row) {
                    print "<p>- {$row['message']}</p>";
                }
            }
        }
    }
} else {
    ?>
        <p>귀하의 지적 재산권은 영광 된 북한에 속해 있지 않습니다. VPN을 사용하면 사용자 이름과 비밀번호로 로그인 할 수 있습니다.</p>
    <?php
}

?>