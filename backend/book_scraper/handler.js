'use strict';
const {
  browserObject, scraperController
} = require('./index')

module.exports.hello = async (event, context) => {
  try {
    let browserInstance = await browserObject.startBrowser();
    const bInstance = await scraperController(browserInstance);
    console.log(Object.getOwnPropertyNames(bInstance.Data));
    const { Data } = bInstance;
    return {
      statusCode: 200,
      body: JSON.stringify({
        message: Data
      })
    }
  } catch (e) {
    return {
      statusCode: 400,
      body: JSON.stringify({
        message: `Error in handler: ${e.message}`,
      })
    }
  }
};
