#!/bin/bash
ip -j -br a > interfaces.json

if [ iwlist ]
then
  python3 verify.py
else
  echo 'PACOTE [ wireless-tools ] NÃO INSTALADO'
fi



