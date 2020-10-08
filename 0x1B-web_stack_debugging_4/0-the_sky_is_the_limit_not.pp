# Setting ULIMIT
exec { 'fix-for-nginx':
  command => 'sed -i s/-n 15/-n 800/ /etc/default/nginx && sudo service nginx restart',
  path    => '/bin/:/usr/bin/',
}
