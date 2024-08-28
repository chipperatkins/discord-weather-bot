const { SlashCommandBuilder } = require('discord.js');
const chatGptUtil = require('../../chatGptUtil.js');

module.exports = {
    cooldown: 60,
	data: new SlashCommandBuilder()
		.setName('weather-update')
		.setDescription('Replies with a weather update!')
        .addStringOption(option => 
            option.setName('ride-time')
            .setDescription('What time do you want weatherman willie to give you weather for?')
            .setRequired(true)
            .setMaxLength(2_000)
        ),
	async execute(interaction) {
		await interaction.deferReply();
        const rideTime = interaction.options.getString('ride-time');
        const prompt = "I need you to produce a weather update for a group ride. " + 
                    "Use the following forecast and JSON hourly forecast data. The group ride is at " + rideTime; 
        chatGptUtil.spawnPythonGPTProcess(prompt, async (data) => await interaction.editReply(data).then(console.log).catch(console.error));         
	},
};