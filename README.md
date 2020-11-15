# Surfs Up!
## Analysis
### Overview of the statistical analysis:
Using Python, Pandas functions and methods, and SQLAlchemy, historical weather temperature data in the months of June and December were manipulated and analyzed in order to gain insights on whether or not a Surfs Up ice cream shop would be able to operate year round.

## Results:
### What the findings of this analysis?
 - Overall, when trying to look for differences in the weather data between June and December, the findings seem fairly similar.
 - The most glaring difference seems to be the monthly minimum temperature value, which in December is 56 degrees and in June is 64.
 - The count of rows for December temperature data is significantly less than for the rows accounting for June data. There are 183 more instances of June data.
 - The std dev of temperatures in Deember is about .5 larger than June's.
 
![Imgur](https://imgur.com/QOZiMOE.png) ![Imgur](https://imgur.com/aeiPD0A.png)

## Summary:
In all, it seems as though weather in the area is similar and consistenet enough to sell ice cream year round. With a historical min and max temperature for both June and December never reaching an uncomfortable level, it seems that in the winter months and the in the summer months people will want ice cream.
It would be of interest to run more queries about different aspects of weather around the area as well.
Two query suggestions I might give would be to 
 - Pull rain data calling on 'Measurement.prcp' for Dec and June to analyze whether rain might keep potential customers indoors.
 - Pull all historical rain data and plot it across all 12 months for a more high-level view of rain activity and how Dec and June relate to the rest of the year.

Overall, ice cream prospects are looking good in Hawaii!
