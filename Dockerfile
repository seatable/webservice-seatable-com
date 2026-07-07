# Use the latest debian base image
FROM debian:trixie-slim

# Update and install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    curl \
    wget \
    ca-certificates

# Download and execute the NodeSource setup script
RUN curl -fsSL https://deb.nodesource.com/setup_22.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh

ARG NPM_VERSION=11.6.3

# Install Node22 and update NPM
RUN apt-get update && \
    apt-get install -y nodejs && \
    npm install -g npm@${NPM_VERSION}

# Verify installation
RUN node -v && npm -v && npx -v

ENV HUGO_BIND="0.0.0.0" \
    HUGO_ENV="development" \
    HUGO_EDITION="extended"

ARG HUGO_VERSION=0.152.2

# Download Hugo
RUN wget https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.tar.gz -O hugo.tar.gz && \
    tar -C /usr/local/bin -xzf hugo.tar.gz && \
    rm hugo.tar.gz

# Set the working directory for Hugo projects
WORKDIR /hugo/src

# Copy code
COPY . /hugo

RUN git config --global --add safe.directory /hugo

# Clean up
RUN apt-get remove -y wget && apt-get autoremove -y && apt-get clean
RUN rm -rf /var/lib/apt/lists/*

EXPOSE 1313

COPY entrypoint.sh /usr/local/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]

# This starts hugo and tailwind in watch mode
#CMD ["npm", "--prefix", "/hugo/src/themes/seatable", "run", "docker:watch"]
CMD ["sh", "-c", "ENABLE_PAGEFIND=${ENABLE_PAGEFIND:-0} npm --prefix /hugo/src/themes/seatable run docker:watch"]
