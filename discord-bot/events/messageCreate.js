const { Events, Collection } = require('discord.js');
const chatGptUtil = require('../chatGptUtil.js')
const { clientId, guildId } = require('../config.json');

const defaultCooldownDuration = 60;
const cooldownAmount = defaultCooldownDuration * 1_00;
const timestamps = new Collection();

module.exports = {
	name: Events.MessageCreate,
	async execute(message) {
		if (message.author.bot) return;
        if (message.guildId != guildId) return;

        if (message.mentions.has(clientId)) {
            const now = Date.now();
            if (timestamps.has(message.author.id)) {
                const expirationTime = timestamps.get(message.author.id) + cooldownAmount;

                if (now < expirationTime) {
                    const expiredTimestamp = Math.round(expirationTime / 1_000);
                    return message.reply({ content: `Please wait, you are on a cooldown. You can use me again <t:${expiredTimestamp}:R>.`, ephemeral: true })
                    .then(console.log)
                    .catch(console.error);
                }
            }

            timestamps.set(message.author.id, now);
            setTimeout(() => timestamps.delete(message.author.id));

            await message.reply("Hey there! Give me a moment while I think...")
            chatGptUtil.spawnPythonGPTProcess(message.content, async (data) => await message.reply(data).then(console.log).catch(console.error));
        }
	}
};