# Change the OS configuration
# so that it is possible to login with the holberton user
# and open a file without any error message.

file { '/etc/security/limits.d/holberton.conf':
  ensure  => present,
  content => "holberton hard nofile 65536\nholberton soft nofile 65536\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

exec { 'reload_limits':
  command     => 'sysctl -p',
  refreshonly => true,
}
