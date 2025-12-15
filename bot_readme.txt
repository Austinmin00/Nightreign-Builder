Prompt:
    1.) Help me work this logic out. No code just help me learn and understand professional coding and infrastructure.

    2.) I need each effect button to work for standard and deep versions to load the relic_effects database for individual selection. Im concerned that loading each button with a copy of the database would be inefficient and prone to crashing and wonder about better solutions. 

    3.) I also need those effect buttons to function similiarly but different for rememberance and sovereign versions. These versions have preset relic effects and I need  those effects to populate the effect buttons. Since the database is pretty condensed I feel it shouldnt have any major issues.

    4.) I want this to be dynamic as in, if a user selects a deep version of any relic type they should be able to select the respective limit of effects and individually assign relic effect. Lets say all goes well and this context occurs. If the user decides to change it to a rememberance or sovereign then the effect buttons will lock out and and when a specific named guaranteed relic is chosen then the database will populate the respective effects properly. Some relics of theses version will come with less than three and in the database will have an empty value for that column. Otherwise if saved then the choice will be remembere and possibly edited if desired afterwards.
