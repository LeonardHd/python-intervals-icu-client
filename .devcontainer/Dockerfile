FROM mcr.microsoft.com/devcontainers/python:2-3.9-bookworm

RUN curl -L "https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64" -o /usr/local/bin/yq \
	&& chmod +x /usr/local/bin/yq

# Install specify-cli via uv
USER vscode
RUN pipx install uv && uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
