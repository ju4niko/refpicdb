#!/bin/bash
docker run --rm -d -p 80:80 -v "$(pwd)/log;C":/var/log/apache2 -v "$(pwd)/web;C":/var/www/html TIROserver 

