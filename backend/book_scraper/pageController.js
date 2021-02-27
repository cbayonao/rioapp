const pageScraper = require('./pageScraper');
async function scrapeAll(browserInstance){
    let browser;
    try {
        browser = await browserInstance;
        let scrapedData = {};
        scrapedData['Data'] = await pageScraper.scraper(browser);
        await browser.close();
        return scrapedData;
    }
    catch(err){
        console.log("Could not resolve the browser instance => ", err);
    }
}

module.exports = (browserInstance) => scrapeAll(browserInstance)