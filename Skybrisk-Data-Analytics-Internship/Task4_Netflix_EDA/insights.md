# Netflix EDA Insights

## Key Interpretations

1. Movies dominate the Netflix catalog. The dataset contains 6,131 movies versus 2,676 TV shows, showing that films make up the majority of available titles.

2. Netflix expanded its content additions rapidly between 2016 and 2019, peaking in 2019 with 1,999 titles added. This indicates a strong platform growth phase before a moderation in later additions.

3. International content is a major part of the catalog. Genres such as `International Movies` and `International TV Shows` rank among the most frequent categories, reflecting Netflix's global content strategy.

4. The United States is the largest single content source, followed by India and the United Kingdom. This shows both strong North American depth and meaningful international diversification.

5. Missing metadata is concentrated in fields like director, cast, and country, which means downstream analysis should treat descriptive metadata carefully and avoid assuming full completeness.

## Bonus Trend Prediction

A simple linear trend fit on yearly title additions suggests that Netflix's content growth remained strong after the initial ramp-up period, but the recent slowdown indicates the library expansion rate may be stabilizing rather than continuing at the same pace indefinitely.
