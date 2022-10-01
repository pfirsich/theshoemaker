#!/bin/bash
set -eou pipefail
set -x

raydor --output output raydor.yml
docker build --tag theshoemaker .
docker save theshoemaker:latest | gzip > theshoemaker.tar.gz
scp theshoemaker.tar.gz theshoemaker:/root
rm theshoemaker.tar.gz

ssh theshoemaker gunzip -f theshoemaker.tar.gz
ssh theshoemaker docker load --input theshoemaker.tar
ssh theshoemaker docker stop theshoemaker
ssh theshoemaker docker rm --force theshoemaker
ssh theshoemaker docker run \
    --detach \
    --rm \
    --init \
    --name theshoemaker \
    --network=host \
    --volume /htcpp_data:/root/.local/share/htcpp \
    theshoemaker
