#!/bin/bash
find raydor.yml src/ src/ templates/ | entr -sr "raydor --output output raydor.yml"
