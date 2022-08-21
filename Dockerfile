FROM htcpp:latest

COPY htcpp.joml htcpp.joml
COPY output/ output/
ENV PORT=80
ENV CACHE_CONTROL="public, max-age=60"

CMD ["htcpp.joml"]
