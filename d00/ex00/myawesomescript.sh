#!/bin/sh
if [ $# -eq 1 ]
   then
	   curl $1 -s > site.ly ; cut -d'"' -f2 site.ly | grep -v  html\> | grep -v head\> ; rm -f site.ly
fi
