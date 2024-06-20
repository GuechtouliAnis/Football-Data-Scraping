# Data Cleaning Process
The data cleaning process for this football dataset was carried out in two steps. Initially, data was scraped from 11 leagues, and later, an additional 7 leagues were added. Despite the two-step approach, the cleaning methodology remained consistent throughout.

## Step-by-Step Cleaning Approach
### 1. Checking for Null Values:

* The process began by identifying null values in the dataset using the ```isna``` method. This helped to pinpoint which columns and rows required attention.

### 2. Filling NaN Values in Percentage Columns:
* Columns such as "challenge_tackles_pct" had ```NaN``` values because there were no tackles to be counted, resulting in a 0/0 scenario. These were filled with ```0```.

* Most of the ```NaN``` values in percentage columns were treated similarly, ensuring no gaps in the dataset.

### 3. Removing Players with Excessive NaNs:

* Players who had a significant number of empty ```NaN``` columns were identified and removed from the dataset. This cleanup step resulted in the removal of ```8``` such players in the second phase of data cleaning.

### 4. Handling Missing Age and Nationality Values:

* Initially, missing values for age and nationality were filled manually.
* Over time, it was observed that the same players consistently had missing age and nationality values. To streamline this, a function (```fill_age_nat```) was created to automatically fill these missing values. Age values were then converted to integers for consistency.
* Additionally, during the cleaning process, days were removed from age using the ```transform_age``` function.

### 5. Specific Table Adjustments:

* Playing Time Table: This table included all players, regardless of whether they played or not, resulting in ```745``` additional rows for players who did not participate. These non-participating players were removed to maintain dataset accuracy.
* Shooting Table: A goalkeeper who scored ```9``` penalties but had ```0``` shots (as penalties aren't counted in shots and shots on target) was identified. The missing values for this player's shots and shots on target were filled with ```0```.

### 6. Removing Players from Imaginary Countries:
Players identified as "Israeli" were removed from the dataset as part of a policy to exclude players from imaginary countries.

## Second Phase: Additional Leagues
The second phase of data cleaning integrated data from the following additional leagues:

* EFL
* Segunda Division
* Serie B
* Ligue 2
* Bundesliga
* MLS
* Liga MX

The same cleaning approach was applied to this new data to ensure consistency and accuracy across the entire dataset.