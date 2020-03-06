#!/bin/bash
# na defaultnom porte mam election
docker run --name matching-postgres -e POSTGRES_PASSWORD=docker -e POSTGRES_USER=root -e POSTGRES_DB=matching -p 5433:5432 -d postgres;
