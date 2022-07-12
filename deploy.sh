#!/bin/bash
set -eou pipefail
set -x

raydor --output output raydor.yml
docker build --tag theshoemaker .
docker save theshoemaker:latest --output theshoemaker.tar
scp theshoemaker.tar theshoemaker:/root
rm theshoemaker.tar

ssh theshoemaker docker load --input theshoemaker.tar
ssh theshoemaker docker stop theshoemaker
ssh theshoemaker docker rm --force theshoemaker
ssh theshoemaker docker run --detach --init --name theshoemaker --network=host theshoemaker
