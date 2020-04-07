#!/bin/bash
# Dsplay all http methods
curl -s --head "$1" | head -n4 | tail -n1 | cut -d' ' -f2-
