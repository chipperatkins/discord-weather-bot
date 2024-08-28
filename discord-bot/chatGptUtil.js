module.exports = {
    spawnPythonGPTProcess: function(prompt, onReply) {
        const arg1 = prompt
        const spawn = require("child_process").spawn;
        const pythonProcess = spawn('python', ['../chatGPTIntegration.py', arg1]);
        pythonProcess.stdout.on('data', (data) => {
            onReply(data.toString());
        });    
    }
}
