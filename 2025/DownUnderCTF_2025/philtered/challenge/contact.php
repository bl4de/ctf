<?php
require_once __DIR__ . '/layout.php';

$content = <<<HTML
<nav style="margin-bottom:2em;">
    <a href="index.php">Home</a> |
    <a href="aboutus.php">About Us</a> |
    <a href="contact.php">Contact</a> |
    <a href="gallery.php">Gallery</a>
</nav>
<h2>Contact Us</h2>
<p>Have questions? Reach out to us!</p>
<ul>
    <li>Email: naaah</li>
    <li>Phone: you ain't getting my digits</li>
    <li>Address: I am Mr Worldwide</li>
</ul>
HTML;

render_layout('Contact - Philtered', $content);
