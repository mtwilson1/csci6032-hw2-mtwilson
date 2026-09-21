FROM python:3.12-slim

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        gh \
        git \
        nodejs \
        npm \
    && npm install --global @github/copilot \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --shell /bin/bash agentuser \
    && mkdir --parents /workspace \
    && chown agentuser:agentuser /workspace

USER agentuser
WORKDIR /workspace
