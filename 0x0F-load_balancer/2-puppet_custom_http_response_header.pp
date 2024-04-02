#install and configure an Nginx server using Puppet

#install nginx if it's not already installed
package { 'nginx':
  ensure => installed,
}

#create a custom 404 page
file { '/var/www/html/custom_404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

#create an index.html
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

#create a config file for the custom 404 page
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;
        root /var/www/html;
        index index.html;

	add_header X-Served-By $hostname;

        location = /redirect_me/ {
                return 301 https://www.youtube.com/watch?v=xvFZjo5PgG0;
        }

        error_page 404 /custom_404.html;
        location = /custom_404.html {
                root /var/www/html;
                internal;
        }
}",
  mode => '0755',
}

#create a sympolic link for the default server
exec { 'enables the default site':
  command => 'ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default',
  unless  => 'test -L /etc/nginx/sites-enabled/default',
  path    => '/usr/bin',
}

service{ 'nginx':
  ensure => running,
  enable => true,
  restart => '/usr/sbin/service nginx reload',
}
