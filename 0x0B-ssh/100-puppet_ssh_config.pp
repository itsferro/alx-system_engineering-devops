#so that you can connect to a server without typing a password.
include stdlib

file { '/root/.ssh/config':
  ensure => present,
}

file_line { 'The host configuration':
  ensure             => present,
  path               => '/root/.ssh/config',
  line               => 'Host *',
  match              => 'Host *',
  replace            => true,
  append_on_no_match => true,
}

file_line { 'Declare identity file':
  ensure             => present,
  path               => '/root/.ssh/config',
  line               => '    IdentityFile ~/.ssh/school',
  match              => '    IdentityFile ',
  replace            => true,
  append_on_no_match => true,
}

file_line { 'Turn off passwd auth':
  ensure             => present,
  path               => '/root/.ssh/config',
  line               => '    PasswordAuthentication no',
  match              => '    PasswordAuthentication ',
  replace            => true,
  append_on_no_match => true,
}
