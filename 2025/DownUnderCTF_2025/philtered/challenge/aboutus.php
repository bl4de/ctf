<?php
require_once __DIR__ . '/layout.php';

$content = <<<HTML
<nav style="margin-bottom:2em;">
    <a href="index.php">Home</a> |
    <a href="aboutus.php">About Us</a> |
    <a href="contact.php">Contact</a> |
    <a href="gallery.php">Gallery</a>
</nav>
<h2>About Us</h2>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eu turpis molestie, dictum est a, mattis tellus. Sed dignissim, metus nec fringilla accumsan.</p>
HTML;

render_layout('About Us - Philtered', $content);
