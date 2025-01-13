#!/bin/bash
find raydor.yml posts/ src/ projects.yaml microblog.yaml templates/ | entr -sr "raydor --output output raydor.yml"
