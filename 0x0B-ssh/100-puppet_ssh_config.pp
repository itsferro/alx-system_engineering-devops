#so that you can connect to a server without typing a password.

file { '/root/.ssh/config':
  ensure  => file,
  content => "\
Host *
    IdentityFile ~/.ssh/school
    PasswordAuthentication no\n",
}
