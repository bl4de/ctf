FROM php:7-apache

RUN /usr/sbin/useradd -u 1000 user

COPY index.php /var/www/html/
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 444 /var/www/html && \
    chmod 555 /var/www/html

COPY flag.txt /flag.txt
COPY files /var/www/html/files/
RUN mv /flag.txt /flag-`tr -dc A-Za-z0-9 < /dev/urandom | head -c 20`.txt

VOLUME /var/log/apache2
VOLUME /var/run/apache2

CMD bash -c 'source /etc/apache2/envvars && APACHE_RUN_USER=user APACHE_RUN_GROUP=user /usr/sbin/apache2 -D FOREGROUND'
