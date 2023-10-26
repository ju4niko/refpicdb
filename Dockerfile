FROM ubuntu:22.04

EXPOSE 15000
EXPOSE 80

RUN apt-get update
RUN apt-get -y install apache2
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get install -y mysql-client
RUN pip install flask
RUN pip3 install pymysql
# Instala phpMyAdmin
#RUN apt-get -y install phpmyadmin


#RUN apt-get -y install python-pil python-matplotlib python-scipy python-sklearn
RUN pip install reportlab
#load apache cgi module
RUN a2enmod cgi
RUN service apache2 restart

#enable cgi in the website root
#second block to allow .htaccess
RUN echo "                       \n \
<Directory /var/www/html>        \n \
   Options +ExecCGI -Indexes     \n \
   AddHandler cgi-script .py     \n \
   DirectoryIndex index.html     \n \
</Directory>                     \n \
" >> /etc/apache2/apache2.conf

RUN chmod -R u+rwx,g+x,o+x /var/www/html

RUN ln -sf /usr/bin/python3 /usr/local/bin/python

CMD /usr/sbin/apache2ctl -D FOREGROUND


