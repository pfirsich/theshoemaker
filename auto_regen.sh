#!/bin/bash
find raydor.yml src/ projects.yaml templates/ | entr -sr "raydor --output output raydor.yml"
