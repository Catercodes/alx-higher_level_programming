#!/bin/bash
#Takes in a URL, sends a request to that URL, and dGGisplays the size of the body of the response
#curl -sI $1 |grep -i Content_Length|awk |'{print $1}'
curl -sI "$1" | grep Content-Length
