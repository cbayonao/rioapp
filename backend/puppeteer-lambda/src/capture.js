// src/capture.js

// this module will be provided by the layer
const chromeLambda = require("chrome-aws-lambda");

// aws-sdk is always preinstalled in AWS Lambda in all Node.js runtimes
const S3Client = require("aws-sdk/clients/s3");

// create an S3 client
const s3 = new S3Client({ region: process.env.S3_REGION });


// The function to run
exports.handler = async (event) => {

  // launch a headless browser
  const browser = await chromeLambda.puppeteer.launch({
    args: chromeLambda.args,
    defaultViewport: chromium.defaultViewport,
    executablePath: await chromeLambda.executablePath
  });

  // Open a page and navigate to the url
  const page = await browser.newPage();
  await page.goto(event.url);

  // take a screenshot
  const buffer = await page.screenshot()

  // upload the image using the current timestamp as filename
  const result = await s3
    .upload({
      Bucket: process.env.S3_BUCKET,
      Key: `${Date.now()}.png`,
      Body: buffer,
      ContentType: "image/png",
      ACL: "public-read"
    })
    .promise();

  // return the uploaded image url
  return { url: result.Location };
};