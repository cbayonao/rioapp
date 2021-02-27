const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  await page.goto('http://entidadesintegradas.co/Registro/', {
    waitUntil: 'networkidle2',
  });
  await page.pdf({ path: 'example.pdf', format: 'A4' });
  await browser.close();
})();