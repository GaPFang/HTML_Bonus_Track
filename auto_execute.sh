#!/bin/bash

# Define an array of arguments
args=(
    # "cryptocurrency Will cryptocurrency take the place of our current currency?"
    # "democracy Is the best government structure democracy?"
    "income_based_fines Should people be fined for crimes based on their income?"
    "space_exploration Is space exploration still important?"
    "after_life Does the afterlife exist?"
    "free_will Do humans have free will?"
    "phy_edu Should schools eliminate physical education requirements?"
    "coedu Should high schools be co-educational?"
    "virtual_games Is the spending on virtual games meaningless?"
    "motor Should the motorcycle make a two-stage left turn?"
    "aa Should we apply “all averaging” to payments of dating?"
    "santa Does Santa Claus exist?"
    "alcohol Will drinking detriment working efficiency?"
    "doraemon Is Doraemon a harmful or beneficial friend to Nobita?"
    "TWindep Should Taiwan be independent?"
    "human_right Is the elimination of certain humans a necessary evil for the protection of humanity or not?"
    "conservation Could the government ethically control stray dogs and cats to mitigate the threat they pose to endangered wildlife by designating certain sensitive zones where the feeding of strays is banned?"
    "CNforce Will China use military force to reunify Taiwan in the near future?"
    "Mars On a planet where you cannot breathe, is living on Mars the best idea?"
    "gender_neutral Should we require gender-neutral bathrooms for transgender people?"
    "gender_gap Do Dedicated Hiring Quotas Close the Gender Gap in Tech?"
    "AIcrisis Will artificial intelligence (AI) cause human extinction?"
    "spectre Is it correct that 'Detecting is not about finding the truth but making others believe in one's assertions'?"
    "aiprogress Do you agree that AI progress is not a natural phenomenon like the Pandemic; therefore, we have considerably more agency rather than taking some preemptive defensive measures?"
    "youtube_profit Should professors monetize their educational videos on YouTube?"
    "legalizing_marijuana Should marijuana be legalized in Taiwan?"
    "NTU_courseweeks Will the transition to a 16-week semester benefit in NTU?"
    "ractopamine_pork Should Taiwan allow the import of pork with ractopamine?"
    "referendum Should referendums be held on the same day as elections?"
    "chicken_eggs Which came first, the chicken or the egg?"
    "girlfriend_mom If your girlfriend and mother both fell into the water simultaneously, whom should you rescue first?"
    "hawaii_pizza Is the existence of Hawaiian pizza acceptable?"
    "good_evil Is human nature inherently good or evil?"
    "sex_love Can sex and love be separated?"
    "lost_penny You’re walking down the street and see a penny on the ground. Would you pick it up or keep walking?"
    "cats_dogs Which do you prefer to be? a cat person or a dog person?"
    # Add more arguments as needed
)

# Loop through the arguments and execute the program with each argument
for arg in "${args[@]}"
do
    # Split the argument into topic and question
    topic="${arg%% *}" # Extract the first word (topic)
    question="${arg#* }" # Extract the rest as the question
    
    # Print the current topic and question
    echo "Current Topic: $topic"
    echo "Current Question: $question"

    # Execute the program with the argument
    python3 spider.py "$topic" "\"$question\"" --close_directly
done

