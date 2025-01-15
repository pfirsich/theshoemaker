FROM htcpp:b690475

COPY htcpp.joml htcpp.joml
COPY output/ output/
ENV PORT=80
ENV CACHE_CONTROL="public, max-age=600"
RUN apt update && apt install -y ca-certificates

CMD ["htcpp.joml"]
