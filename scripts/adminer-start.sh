#!/bin/bash
sudo docker run --link matching-postgres:5433 -p 8081:8080 -d adminer