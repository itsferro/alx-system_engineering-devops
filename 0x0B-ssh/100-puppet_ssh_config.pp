#so that you can connect to a server without typing a password.

file_line { 'Declare identity file':
  path  => '/root/.ssh/config',
  line  => ' IdentityFile ~/.ssh/school',
  match => '^Host *',
}

file_line { 'Turn off passwd auth':
  path  => '/root/.ssh/config',
  line  => ' PasswordAuthentication no',
  match => '^Host *',
}
