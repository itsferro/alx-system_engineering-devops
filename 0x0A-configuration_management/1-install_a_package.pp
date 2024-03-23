#install flask from pip3.
#Version 2.1.0

exec { 'flask installation':
  command => 'pip install flask==2.1.0',
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
