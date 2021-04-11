# Debt Timing and Gas Fees Question?
When is the best time to self-issue debt (Borrow alUSD) while minimizing gas fees?

## Minimizing Gas Fees
As a collaborative effort, CryptoLionR and I (celly_harder) used Flipside's queries to understand how much users are spending on gas fees when they are minting alUSD/taking out debt from the Alchemix ecosystem. By creating Flipside charts with both hour and day intervals, and feeding a Python output that offers the best hourly intervals, we offer readers the opportunity to see when alUSD minters might be underpaying/overpaying for gas fees. 

## Debt Timing and Gas Fees By Day

https://app.flipsidecrypto.com/shareable/debt-timing-&-gas-fees-yIwT82

![Screen Shot 2021-04-10 at 10 41 24 PM](https://user-images.githubusercontent.com/82302513/114294264-3c06b380-9a52-11eb-96a6-36fc2e1fb0d8.png)
(Debt Timing and Gas Fees By Day)

We leveraged Flipside's interactive data visualization tool to chart the average gas prices paid for minting alUSD per day. The chart's limit is set to 100 but since Alchemix only came out a few months ago, the dataset starts on March 12. The abundance of visualizable data will grow as time goes on. We found that on a per day basis, the average gas price paid bottomed near $20 per transaction (March 27 & April 10), and this average went as high as $35 on some days. Although this is definitely a cool tool that defined ranges throughout the last few weeks, it didn't necessarily answer the question of: "when is the best time to self-issue debt while minimizing gas fees?"

Therefore, we decided to create a visualization that filtered the averages by hour.

## Debt Timing and Gas Fees By Hour 

https://app.flipsidecrypto.com/shareable/debt-timing-gas-fees-YRV2sD

![Screen Shot 2021-04-10 at 11 13 22 PM](https://user-images.githubusercontent.com/82302513/114294284-648ead80-9a52-11eb-8e81-babb283c929e.png)
(Debt Timing and Gas Fees By Hour) 

By filtering the averages by hour instead of days, it offers the users a better chance of pinpointing the best ranges or times throughout the day to borrow USD. This particular visualization in Flipside gave us a good chance to view some patterns, but we still had to manually scroll through the table to find the best hours, which is both tedious and inefficient. 

## Python Script 

In order to evaluate the best hours, we grouped hour intervals to see when specific hours had lower gas fees than the average. This way, users can be given the information instead of manually scrolling through the interactive chart. 
