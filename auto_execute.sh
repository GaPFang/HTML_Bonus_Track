#!/bin/bash

# Define an array of arguments
args=(
    # pub
    # "technology_and_connections Does technology strengthen connections between people?"
    # "Pokemon_Go	Does Pokemon Go do more good than harm to our society?"
    # "individual_destiny	Does the individual determine individual destiny, not society?"
    # "AI_and_Schooling	Should schools prohibit students from utilizing ChatGPT and similar AI tools for completing their assignments?"
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

    # private
    "animal_research Should animals be used for scientific research?"
    "capital_punishment Should capital punishment be used as a form of punishment?"
    "mandatory_vaccinations Should employers be able to mandate vaccinations?"
    "keep_going_on_or_give_up Is it harder to keep going on or to give up?"
    "fortune_or_adversity Which circumstance, living in fortune or facing adversities, fosters greater personal growth?"
    "outcome_vs_process Is the outcome more important than the process?"
    "standardized_testing Should standardized testing be the primary measure of a student’s academic ability?"
    "tourism Does tourism do more good than harm?"
    "skills_and_connections Which plays a more significant role in achieving success: one’s skills and abilities or their connections with others?"
    "school_uniform_policies Should school uniform policies be gender neutral?"
    "same-sex_marriage Should same-sex marriage be allowed?"
    "online_vs_traditional_learning Is it possible for online learning to eventually supplant traditional classroom-based education?"
    "euthanasia Should euthanasia be decriminalized?"
    "citizen_judge Should we establish the citizen judge system?"
    "plea Should the system of plea bargaining remain?"
    "slave Are people free to sell themselves as slaves?"
    "ww2 Should the United States drop atomic bombs during World War II?"
    "taught-base Should the government set up taught-based master’s degrees?"
    "covid19 Should all people receive at least one dose of the COVID-19 vaccine?"
    "top_unv Should government education funds be allocated first to lower-tier universities or top"
    "academic Should academic research be regulated by sensitive political issues?"
    "pizza Do Pineapples belong on pizza?"
    "rain_conclusion When it rains, do you get less wet when running or walking?"
    "generativeAI Is the benefit of generative AI in creation greater than its drawbacks, or vice versa?"
    "TWedu Are the benefits of establishing more high schools and universities in Taiwan greater than the drawbacks, or vice versa, for education?"
    "house_tax Can the House Tax Act amendments that increase taxes on vacant residential properties to curb speculation in the local property market better achieve housing justice in Taiwan than building public housing?"
    "energy Can the Renewable Energy Development Act that includes regulations on the obligations of electricity-intensive users enhance Taiwan's overall renewable energy share effectively?"
    "bilingual Should the government continue the policy that makes Taiwan bilingual by 2030?"
    "plastic Should the government continue the policy that Taiwan prohibits petroleum-based plastic straws in public spaces?"
    "factcheck Can ChatGPT fact-check what it generates on its own?"
    "master_thesis Must Master's students complete a thesis for their major?"
    "remote_learn Can the pandemic-induced at-home remote learning negatively impact students' capability?"
    "ETalive Do aliens exist? Is there life beyond Earth?"
    "threeking If Sima Yi staged a coup at the Gaoping Tombs incident and failed, which states would win and end the Three Kingdoms era?"
    "youtuber_apology Should YouTubers monetize their apology videos?"
    "global_warm Is global warming a real issue?"
    "nuclear Should the 4-th nuclear power plant in Taiwan be restarted?"
    "algal_reef Do you agree with relocating the CPC Corporation’s natural gas receiving station away from the algal reef coast?"
    "time_machine If you had a time machine, would you choose to go back to the past or forward to the future?"
    "breathe_underwater If you could breathe underwater, would you choose to live on land or underwater?"
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

