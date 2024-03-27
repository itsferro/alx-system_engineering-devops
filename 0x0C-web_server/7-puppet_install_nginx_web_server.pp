#install and configure an Nginx server using Puppet

#install nginx if it's not already installed
package { 'nginx':
  ensure => installed,
}

#create a custom 404 page
file { '/var/www/html/custom_404.html':
  content => "Ceci n'est pas une page",
}

#create a config file for the custom 404 page
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;

        location = /redirect_me {
                return 301 https://www.youtube.com/watch?v=xvFZjo5PgG0;
        }

        location = /mystery {
                return 301 https://www.youtube.com/watch?v=xvFZjo5PgG0;
        }

        error_page 404 /custom_404.html;
        location /custom_404.html {
                root /var/www/html;
                internal;
        }
}",
}

#create a sympolic link for the default server
exec { 'enables the default site':
  command => 'ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default',
  unless => 'test -L /etc/nginx/sites-enabled/default',
  path => '/usr/bin',
}

#restart nginx to apply changes
service{ 'nginx':
  ensure => running,
  enable => true,
}
