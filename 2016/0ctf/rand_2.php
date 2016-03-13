<?php
error_reporting(0);
session_start();

$flag = "p0wnd!!!";

// jesli jest $_SESSION['time'] i aktualna wartosc time() - $_SESSION["time"] > 60
// - 
if($_SESSION['time'] && time() - $_SESSION['time'] > 60) {
	
	// usun sesje
    session_destroy();
	
	// koniec - timeout
    die('timeout');
	
	
} else {
    // jesli nie, $_SESSION["time"] = time()
	$_SESSION['time'] = time();
}

//// tutaj powinna byc juz ustawiona wartosc dla $_SESSION['time']
// echo 'Wartosc $_SESSION po ustawieniu $_SESSION["time"]: ';
// var_dump($_SESSION);


//// time sluzy tylko ustaleniu max. dlugosci trwania sesji - nie bierze udzialu w algorytmie

// --------------------

// wyswietl aktualna wartosc pobrana z generatora losowego rand()
echo "Pierwsza wartosc rand() :" . rand() . "<br />";

// jesli jest 'go':
if (isset($_GET['go'])) {
	
	// zadeklaruj $_SESISON['rand'] jako tablice
    $_SESSION['rand'] = array();
	
	// zadeklaruj $i = 5
    $i = 5;
	
	// zadeklaruj pusty string $d
    $d = '';
	
	// dopoki $x jest true - wiekszy od 0 w tym wypadku, czyli 5 iteracji
    while($i--){
		
		// zadeklaruj $r jako wartosc rand() rzutowana na typ string
        $r = (string)rand();
		
		// dodaj do tablicy $_SESSION['rand'] ciag zadeklarowany powyzej
        $_SESSION['rand'][] = $r;
		
		// wykonaj konkatenacje $d i $r
        $d .= $r;
    }
	
	//// tutaj $_SESSION['rand'] powinna zawierac piec elementow wygenerowanych przez rand()
	
	echo 'Wartosc $_SESSION po $_GET["go"] i pieciu iteracjach rand(): ';
	var_dump($_SESSION);
	
	// wyswietl MD5 ciagu $d
	//// $d to MD5 wszystkich polaczonych uprzednio ciagow $r ^^^
    echo "MD5 wszystkich ciagow \$r: " . md5($d);
	
	
// albo jesli jest 'check':
} else if (isset($_GET['check'])) {
	
	echo 'Wartosc $_SESSION po $_GET["check"] - tu jest porownanie $_GET["check"] z $_SESSION["rand"]: ';
	
	var_dump($_SESSION);
	var_dump($_GET['check']);
	var_dump('$_GET["check"] === $_SESSION["rand"]: ' . $_GET['check'] === $_SESSION['rand']);
	
	//jesli wartosc przeslana w 'check' jest identyczna z zapisana w $_SESSION['rand']:
    if ($_GET['check'] === $_SESSION['rand']) {
		
		// wyswietl FLAGE
        echo $flag;
    } else {
		
		// jesli nie, wyjdz i usun sesje
        echo 'Nie ma flagi :/';
        session_destroy();
    }
	
	// albo (nie ma nic w GET)
} else {
	
	// pokaz zrodlo tego pliku - komentuje to, bo mam juz zrodlo
    // show_source(__FILE__);
}

// usun sesje
session_destroy();