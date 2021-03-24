# **Election Audit Findings**

## **Overview of Election Audit**
- The purpose of this project was to assist Seth and Tom with an election audit, to provide a breakdown of the number of votes and percentage of the total votes each candidate received, and to illustrate which candidate won the election, the winner’s vote count, and the winner’s percentage of total votes.  These results were shared with the election commission, and the commission has requested some additional data to complete the audit:
  - The voter turnout for each county
  - The percentage of votes of the total count from each county 
  - The county with the highest turnout

## **Election Audit Analysis and Results**
- The following are the election audit findings that were provided to the election commission.  

  ![Election_Results_Findings](Resources/Election_Results_Findings.PNG)

- Total Votes Cast: 
  - 369,711
- Individual County Names, Voting Percentage, and Number of Votes:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
  - The following image illustrates the for loop that was created to come up with the county results.
   
   ![County_Vote_Findings](Resources/County_Vote_Findings.PNG)
  
           
- County with Largest Number of Votes:
  - Denver
  - The following if statement was created to show the county with the largest number of votes.
    
    `if (county_vote_count > largest_turnout_votes):
            largest_turnout_votes = county_vote_count
            largest_turnout_county = county_name`
- Individual Candidate Names, Voting Percentage, and Number of Votes:
   - Charles Casper Stockham: 23.0% (85,213)
   - Diana DeGette: 73.8% (272,892)
   - Raymon Anthony Doane: 3.1% (11,606) 
- Election Results:
  - Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8% 

## **Election Audit Summary**

- As the project manager of this election audit, I created code that can be geared to work for all types of elections.  With a few modifications, the election commission could reuse this code for future election audits.  Reusing this code could save the election commission a considerable amount of time and resources.  It could prevent the election commission from putting forth extra hours to re-invent the wheel, and it also could prevent the commission from paying for another full audit. I will be available to provide support to the commission staff for a small hourly fee ($x/hour) until the staff are up to speed with the changes that need to be made per election.  

- Some modifications will need to be made to the code per election.  Regardless of what type of election the commission would want to use the code for, the commission would need to ensure they had the new election information included in the csv data and to upload/read a new csv file per each specific election.  If the election commission is going to monitor elections from a local perspective next year, the commission could replace everything that refers to the "county" with "city," double checking that the indexing is correct in the new code.  If they wanted to track city information in addition to the current county/candidate information, there would need to be several additions to the code, but it would be very similar to the current county/candidate script.  Some examples of necessary modifications could include creating a city list and city votes dictionary and tracking the largest voter turnout by city by initiating a string to hold the name of the largest turnout city and a variable for the number of votes for that city.  Then a new for loop would need to be added to pass through each row of the city data to add the city names and votes for the desired output.  This is not an exhaustive list of all modification but more of a general idea for the commission’s reference. 

- This may seem complex, but as stated in my proposal, I would be willing to assist the commission staff with these changes as necessary until they are confident in their abilities, which would save the commission valuable time and money in the future.  Thank you for your consideration, and please let me know if I can be of further assistance.
