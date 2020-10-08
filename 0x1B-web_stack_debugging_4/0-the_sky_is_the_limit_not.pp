# Setting ULIMIT
exec { 'fix-for-nginx':
  command => 'sed -i s/15/800/ /etc/default/nginx && service nginx restart',
  path    => '/bin/:/usr/bin/',
}
