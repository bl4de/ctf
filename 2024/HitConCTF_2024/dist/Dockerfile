FROM oven/bun:1.1.8-slim
RUN apt-get update && apt-get install -y gcc

RUN useradd -ms /bin/bash ctf

WORKDIR /home/ctf/app

# Setup challenge
COPY ./src/index.js .
RUN chown -R ctf:ctf /home/ctf/app

# Setup flag & readflag
COPY ./flag/readflag.c /readflag.c
COPY ./flag/flag /flag
RUN chmod 0400 /flag && chown root:root /flag
RUN chmod 0444 /readflag.c && gcc /readflag.c -o /readflag
RUN chown root:root /readflag && chmod 4555 /readflag

USER ctf
ENV NODE_ENV=production
CMD ["bun", "index.js"]

