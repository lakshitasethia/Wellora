const mongoose = require('mongoose');
const User = require('./models/User');
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://127.0.0.1:27017/wellora';

mongoose.connect(MONGODB_URI).then(async () => {
  const users = await User.find({}, '-password'); // Exclude password from output
  console.log('--- USERS IN MONGODB ---');
  console.log(JSON.stringify(users, null, 2));
  mongoose.disconnect();
});
