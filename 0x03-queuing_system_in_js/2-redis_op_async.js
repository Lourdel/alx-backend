import { createClient } from 'redis';
import { promisify } from 'util';

const redis = require('redis');

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client)

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', err => {console.log('Redis client not connected to the server: ERROR_MESSAGE', err);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  client.get(schoolName, redis.print)
  await getAsync(schoolName);}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
client.quit();
