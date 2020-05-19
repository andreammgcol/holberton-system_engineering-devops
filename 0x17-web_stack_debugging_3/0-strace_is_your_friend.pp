# fixing the local error in wordpress
exec { 'fixing_wperror':
  command => '/usr/bin/sudo /bin/sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" \
  /var/www/html/wp-settings.php',
    }