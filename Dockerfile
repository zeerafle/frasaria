FROM python:3.10-slim AS model

RUN apt-get update && apt-get install --no-install-recommends -y build-essential gcc git
RUN pip install -U "huggingface_hub[cli,hf_transfer]"
ENV HF_HUB_ENABLE_HF_TRANSFER=1
RUN huggingface-cli download prithivida/parrot_paraphraser_on_T5 && \
    huggingface-cli download prithivida/parrot_adequacy_model && \
    huggingface-cli download prithivida/parrot_fluency_model && \
    huggingface-cli download sentence-transformers/paraphrase-distilroberta-base-v2
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --user -r /requirements.txt

FROM debian:bookworm-slim
RUN apt update && \
    apt install --no-install-recommends -y build-essential python3 gunicorn3 && \
    apt clean && rm -rf /var/lib/apt/lists/*
COPY --from=model /root/.local/lib/python3.10/site-packages /usr/local/lib/python3.10/dist-packages
ARG CACHE_DIR="/root/.cache/huggingface"
RUN mkdir -p ${CACHE_DIR}
COPY --from=model ${CACHE_DIR} ${CACHE_DIR}
WORKDIR /app
COPY . /app
EXPOSE 50505

ENTRYPOINT [ "gunicorn", "app:app" ]