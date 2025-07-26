<?php
require_once __DIR__ . '/layout.php';

$content = <<<HTML
<nav style="margin-bottom:2em;">
    <a href="index.php">Home</a> |
    <a href="aboutus.php">About Us</a> |
    <a href="contact.php">Contact</a> |
    <a href="gallery.php">Gallery</a>
</nav>
<h2>Gallery</h2>
<div style="display:flex;gap:1em;flex-wrap:wrap;">
    <img src="https://picsum.photos/seed/1/200/150" alt="Random 1" style="border-radius:8px;box-shadow:0 2px 8px #0001;">
    <img src="https://picsum.photos/seed/2/200/150" alt="Random 2" style="border-radius:8px;box-shadow:0 2px 8px #0001;">
    <img src="https://picsum.photos/seed/3/200/150" alt="Random 3" style="border-radius:8px;box-shadow:0 2px 8px #0001;">
    <img src="https://picsum.photos/seed/4/200/150" alt="Random 4" style="border-radius:8px;box-shadow:0 2px 8px #0001;">
</div>
HTML;

render_layout('Gallery - Philtered', $content);
