#!/bin/bash
# Takes a URL & sends a request to that URL & displays the size of body
curl -s "$1" | wc -c
