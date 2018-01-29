sudo /etc/init.d/mysql start
mysql -uroot -e "create database ask;"
mysql -uroot -e "CREATE USER ask IDENTIFIED BY 'ask@ask';"
mysql -uroot -e "GRANT ALL ON ask.* TO 'ask'@'localhost';"
