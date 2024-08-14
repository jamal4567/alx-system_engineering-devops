# replace line that containe phpp with php

$file_path = '/var/www/html/wp-settings.php'


exec { 'fix error':
  command => "sed -i 's/phpp/php/g' ${file_path}",
  path    => ['/bin','/usr/bin']
}
