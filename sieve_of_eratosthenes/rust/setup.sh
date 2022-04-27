#!/bin/bash
touch .env
echo "USER_ID=$(id -u)" >> .env
echo "GROUP_ID=$(id -g)" >> .env
sudo docker-compose up -d