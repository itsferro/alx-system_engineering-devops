#so that you can connect to a server without typing a password.
include stdlib

file_line { 'Declare identity file':
  path  => '~/.ssh/config',
  line  => ' IdentityFile ~/.ssh/school',
  match => '^Host *',
}

file_line { 'Turn off passwd auth':
  path  => '~/.ssh/config',
  line  => ' PasswordAuthentication no',
  match => '^Host *',
}
