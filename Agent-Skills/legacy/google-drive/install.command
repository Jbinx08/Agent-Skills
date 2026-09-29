#!/bin/bash
cd "$(dirname "$0")" || exit 1
python3 install.py
result=$?
echo
read -r -p "Press Enter to close this window..." _
exit "$result"
