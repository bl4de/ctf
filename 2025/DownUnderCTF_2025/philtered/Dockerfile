FROM php:8.1-cli

# Set working directory
WORKDIR /var/www/html

# Copy challenge files
COPY challenge/ /var/www/html/

CMD ["php", "-S", "0.0.0.0:80"]
