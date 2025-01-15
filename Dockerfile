FROM htcpp:b690475c0f1fc8da148150004e73945457eefbce

COPY htcpp.joml htcpp.joml
COPY output/ output/
ENV PORT=80
ENV CACHE_CONTROL="public, max-age=600"
RUN apt update && apt install -y ca-certificates

CMD ["htcpp.joml"]
