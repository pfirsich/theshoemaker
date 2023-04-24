#!/bin/bash
find raydor.yml posts/ src/ projects.yaml templates/ | entr -sr "raydor --output output raydor.yml"
