FROM node:20-alpine
RUN apk add --no-cache python3 py3-pip
RUN apk add py3-requests py3-matplotlib py3-numpy py3-pandas py3-beautifulsoup4
RUN pip install --no-cache-dir -U --break-system-packages openai
COPY *.py /src/
COPY /discord-bot/ /src/discord-bot/
WORKDIR /src/discord-bot/
RUN npm install discord.js
CMD [ "node", "index.js" ]