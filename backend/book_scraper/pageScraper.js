const scraperObject = {
  url: 'http://entidadesintegradas.co/Registro/Index?60N5MP1O=1',
  async scraper(browser){
      let page = await browser.newPage();
      console.log(`Navigating to ${this.url}...`);
      // Navigate to the selected page
      await page.goto(this.url);
      const pageRionegro = await page.evaluate(() => document.body.innerHTML);
      let data = {};
      // await page.waitForSelector("#login:_t32");
      const servicesNoAuth = await page.$$(".SMREIEnlace1");
      for (let i = 0; i < servicesNoAuth.length; i++) {
        const serviceNoAuth = await (await servicesNoAuth[i].getProperty('innerText')).jsonValue();
        data[i] = serviceNoAuth;
      }
      // Wait for the required DOM to be rendered
      // await page.waitForSelector('.page_inner');
      // // Get the link to all the required books
      // let urls = await page.$$eval('section ol > li', links => {
      //     // Make sure the book to be scraped is in stock
      //     links = links.filter(link => link.querySelector('.instock.availability > i').textContent !== "In stock")
      //     // Extract the links from the data
      //     links = links.map(el => el.querySelector('h3 > a').href)
      //     return links;
      // });
      // // console.log(`estos son: ${urls}`);
      // return urls;
      return data;
  }
}

module.exports = scraperObject;