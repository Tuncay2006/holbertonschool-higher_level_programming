#!/bin/bash

# MySQL root kullanıcısıyla bağlanıp ayrıcalıkları listeleyen script
# root şifresi sorulmadan çalışması için ~/.my.cnf dosyasına root şifresi yazılmalı
mysql -u root -e "SHOW GRANTS FOR 'user_0d_1'@'localhost';"
mysql -u root -e "SHOW GRANTS FOR 'user_0d_2'@'localhost';"
