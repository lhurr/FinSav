#!/bin/sh

MODEL_DIR="/root/.ollama/models/manifests/registry.ollama.ai/library/llama3"

ollama serve &

echo 'Waiting for Ollama service to start...'
sleep 10

if [ ! "$(ls -A $MODEL_DIR)" ]; then
    echo 'LLaMa3 model not found, downloading...'
    ollama pull llama3
    echo 'Model downloaded successfully.'
else
    ollama run llama3
    echo 'LLaMa3 model already present, skipping download.'
fi

# Keep the container running
tail -f /dev/null