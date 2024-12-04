import redis from 'redis';

const client = redis.createClient();


client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});


function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (error, reply) => {
        console.log(schoolName);
        console.log(`Reply: ${reply}`);
    });
};

function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, reply) => {
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
