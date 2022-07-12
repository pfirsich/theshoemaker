FROM htcpp:latest

COPY htcpp.joml htcpp.joml
COPY output/ output/

CMD ["htcpp.joml"]
