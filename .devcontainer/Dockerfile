FROM mcr.microsoft.com/devcontainers/python:2-3.9-bookworm

# Install specify-cli via uv
USER vscode
RUN pipx install uv && uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
