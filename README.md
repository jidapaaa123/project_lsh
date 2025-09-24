# project_lsh
"The goal of this project is to use Locality Sensitive Hashing (LSH) to find similarities between the different food categories based on the countries where those categories are eaten."

# How to Use this Repo  
1) Run data.py
2) See results (Jaccard Similarity of the candidate pairs) in final_data.txt  
There is just so many combinations... older rows get cut off in the terminal if I print the data there.  
I'm a bit surprised that a lot of the sets REALLY have identical first 5 rows (band). It'll probably be different with more bands  
3) Pretty-print of normalized consumption data in country_food_normalized.txt  
4) Pretty-print of normalized majority-consumption (>= 0.5) in country_food_normalized_majority.txt

Questions:

* How many food categories are we working with? How many countries?  
    + 11 food categories for 260 countries  
    + (11 rows x 260 columns)
* What countries have the highest Jaccard similarity?  
    + Due to randomization, candidate pairs may slightly differ from run to run. But the full signatures stay the same, so it's generally fine. The common pattern seems to be that, actually, MANY country-pairs have the exact same full-signatures  
    + It takes me about ~1700 rows-ish to see similarities less than 1  
    + Also, United States is under "USA"... despite United Kingdom and United Arab Emirates not being abbreviated  
    + Albania is considered similar to a lot of countries... when I look at the normalized-majority columns, I see a 1 in only "dairy". So it matches all the other countries that have that same dairy-only signature... I really don't get why  
    + So looking at the normalized columns would probably be less strict, since there's no >= 0.5 thresholds. Let's just look at a few, not in any particular order  
    + Albania-Australia (Jaccard=1.0): their most consumed food IS dairy. Albania doesn't eat much else besides wheat. Woah. Australia's other top foods are splt btween wheat and poultry and pork.  
    + USA-Uganda (Jaccard=1.0): ????? Both our most consumed food IS also dairy (hot commodity! Everyone loves cheese, my guess). USA's other top foods are between wheat and poultry (cheese, bread, chicken... burger? Not sure why it's not beef). Ugandas' are between fish and wheat.  
    + And the list goes on. By our metric, many countries have the exact same signature. If I had the time, I would've wanted to see the data normalized in a ranking-based manner (0 for top 1 food, 1 for top 2 food, etc.) to compare it to our current normalization (everything proportional to the country's most and least popular foods--> to the scale of 0 and 1)  
    
* What foods do you see these countries eat?  
    + See above question. It was a bit natural to answer both questions together  

* Is there any connection between these countries?  
    + I don't personally see it in the limited sample size (of 2 country pairs). But it's also because the foods they commonly eat, are ALSO foods *most* countries eat. I don't think the similarities mean too much if they happen to consume a lot of the globally-common foods, like wheat and dairy.  
    + ... which makes me think, the TF.IDF tackled a similar idea with IDF. I wonder if that concept can help me identify "more meaningful similarities."  
* For this dataset, we could have done a similarity test without LSH. When would LSH become a lot more useful?  
    + It would be a lot more useful if there were more food categories. Our band size is 5 rows... but there's 11 rows total! If there were, say, 500 rows, it would be a lot more useful to use the sample-based (band-based) approach of LSH  