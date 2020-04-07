#!/bin/bash
# Send a POST request with param
curl -s -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
