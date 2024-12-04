import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Promisify the get method of the Redis client
const getAsync = promisify(client.get).bind(client);

// Set new school value (returns a promise)
function setNewSchool(schoolName, value) {
  return new Promise((resolve, reject) => {
    client.set(schoolName, value, (error, reply) => {
      if (error) {
        reject(error);
      } else {
        console.log(schoolName);
        console.log(`Reply: ${reply}`);
        resolve(reply);
      }
    });
  });
}

// Async function to display school value
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    if (reply) {
      console.log(reply);  // This will print the value of the school
    } else {
      console.log(`No value found for ${schoolName}`);
    }
  } catch (error) {
    console.error(`Error retrieving value for ${schoolName}: ${error.message}`);
  }
}

// Run operations sequentially
async function run() {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

run();
