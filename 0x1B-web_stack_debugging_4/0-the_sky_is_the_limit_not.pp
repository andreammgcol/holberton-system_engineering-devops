# Fixing the stack

exec { 'fixing_core':
  path    => '/usr/bin',
  command => "sudo sed -i 's/worker_processes 4;/worker_processes 8;/g' /etc/nginx/nginx.conf; sudo service nginx restart",
}
