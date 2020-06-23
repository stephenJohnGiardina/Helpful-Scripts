/**
 * This is a function that takes in the package.json object
 * in an package.json file and returns an array of both
 * a space separated string of all the dependencies and
 * a space seperated string of all the devDependencies.
 * This is so you can easily download (npm i) all the
 * npm packages of a repo that you are copying.
 */

let makeDependencyString = (packageObj) => {
  let result = {};
  if (packageObj.dependencies !== undefined) {
    let str = '';
    let dependencies = packageObj.dependencies;
    for (let key in dependencies) {
      str+= ' ' + key;
    }
    result.dependencies = str.substring(1)
  }
  if (packageObj.devDependencies !== undefined) {
    let str = '';
    let devDependencies = packageObj.devDependencies;
    for (let key in devDependencies) {
      str+= ' ' + key;
    }
    result.devDependencies = str.substring(1)
  }
  return result;
}

console.log(makeDependencyString({
  "name": "hrr45-mvp",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "build": "webpack -d --watch",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/stephenJohnGiardina/hrr45-mvp.git"
  },
  "author": "",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/stephenJohnGiardina/hrr45-mvp/issues"
  },
  "homepage": "https://github.com/stephenJohnGiardina/hrr45-mvp#readme",
  "dependencies": {
    "@babel/core": "^7.10.2",
    "@babel/preset-env": "^7.10.2",
    "@babel/preset-react": "^7.10.1",
    "babel-core": "^6.26.3",
    "babel-loader": "^8.1.0",
    "babel-preset-airbnb": "^5.0.0",
    "body-parser": "^1.19.0",
    "express": "^4.17.1",
    "jquery": "^3.5.1",
    "mongodb": "^3.5.8",
    "mongoose": "^5.9.18",
    "path": "^0.12.7",
    "react": "^16.13.1",
    "react-dom": "^16.13.1"
  },
  "devDependencies": {
    "css-loader": "^3.5.3",
    "style-loader": "^1.2.1",
    "webpack": "^4.43.0",
    "webpack-cli": "^3.3.11"
  }
}
));