## Features found in all tables

    player          -   Player's full name
    nationality     -   Player's nationality
    position        -   Player's position and is one or two of the general positions
                        (GK, DF, MF, FW)
    age             -   Player's age in years at the season's end
    club            -   The club that the player played for during the season
    league          -   The league the club is found in
    minutes_90s     -   Number of minutes played by the player divided by 90


## Defense Table Features

    p_tackled               -   Number of players tackled
    tklw                    -   Number of tackles in which the team won the possession of the ball
    def_3rd                 -   Tackles in defensive 3rd
    mid_3rd                 -   Tackles in middle 3rd
    att_3rd                 -   Tackles in attacking 3rd
    d_tackled               -   Number of dribblers tackled
    challenges              -   Dribbles challenged, unsuccessful challenges + number of dribblers tackled
    challenge_tackles_pct   -   Dribblers tackled divided by number of attempts to challenge an opposing dribbler
                                (0.625 dribblers challenged per squad game to qualify as leader)
    challenges_lost         -   Number of unsuccessful attempts to challenge a dribbling player
    blocks                  -   Number of times blocking the ball by standing in its path
    blocked_shots           -   Number of times blocking a shot by standing in its path
    blocked_passes          -   Number of times blocking a pass by standing in its path
    intr                    -   Total interceptions
    tkl_intr                -   Number of players tackled + interceptions
    clr                     -   Clearances 
    err                     -   Mistakes leading to an opponent's shot


## Goalkeeping Table Features
    
    MP                  -   Matches played
    starts              -   Games started by the player
    mins                -   Minutes played
    GA                  -   Goals against
    GA90                -   Goals against per 90 minutes
    shotsOT_a           -   Shots on target against   
    saves               -   Saves
    save_pct            -   (Shot on target against minus Goals against) divided by Shot on target against
    W                   -   Wins
    D                   -   Draws
    L                   -   Losses
    CS                  -   Clean Sheets
    CS_pct              -   % of matches that result in Clean Sheet
    PKatt               -   Penalty kicks faced
    PK_scored           -   Penalty kicks scored against
    PK_save             -   Penalty kicks saved
    PK_missed           -   Penalty kicks missed
    PK_pct              -   Penalty kicks saving %


## Goalkeeping Advanced Table Features

    GA                      -   Goals against
    PK_scored               -   Penalties scored against
    FK_scored               -   Freekicks scored against
    CK_scored               -   Corners scored against
    OG                      -   Own goals scored against the goalkeeper (either by the goalkeeper himself or by his teammates)
    psxg                    -   Expected goals based on how likely the GK is to save the shot
                                (PK not included)
    psxg_per_sot            -   npxg per shot on target
    psxg_net                -   + means better luck saving a shot
    psxg_net90              -   psxg net per 90 minutes
    launched_c              -   Launched passes completed
    launched                -   Launched passes attempted
    launched_pct            -   Launched passes completed %
    passes                  -   Passes attempted (GK not included)
    throws                  -   Throws attempted
    launch_pct              -   % of passes that were launched (longer than 40 yards)
    avg_len                 -   Average length of passes in yards
    gk                      -   Goal kicks attempted
    gk_launched             -   Goal kicks launched %
    gk_avg_len              -   Average length of GK
    crosses                 -   Crosses faced
    crosses_stopped         -   Crosses stopped by the goalkeeper
    crosses_stopped_pct     -   % of crosses stopped by the goalkeeper   
    OPA                     -   Defensive actions outside penalty area
    OPA_per90               -   Defensive actions outside penalty area per 90 minutes
    avg_dist                -   Average distance of defensive actions from goal


## GSC Table Features
    -Goal and Shot Creation-

    sca                 -   Shot-creating Action
                            (Two offensive actions directly leading to a shot, such as passes, take-ons and drawing fouls)
    sca_per90           -   Shot-creating Action per 90 minutes
                            (Minimum 30 mins played per squad game to qualify as a leader)
    sca_passes_live     -   Completed live-ball passes that lead to a shot attempt
    sca_passes_dead     -   Completed dead-ball passes that lead to a shot attempt
                            (FK, CK, Throw-in, GK, kick off included)
    sca_take_ons        -   Successful take-ons that lead to a shot attempt
    sca_shots           -   Shots that lead to another shot attempt
    sca_fouled          -   Fouls drawn that lead to a shot attempt
    sca_defense         -   Defensive actions that lead to a shot attempt
    gca                 -   Goal-creating action
                            (Desc similar to sca but leading to a goal instead of a shot)
    gca_per90           -   Goal-creating action per 90 minutes
    gca_passes_live     -   Completed live-ball passes that lead to a goal
    gca_passes_dead     -   Completed dead-ball passes that lead to a goal
    gca_take_ons        -   Successful take-ons that lead to a goal
    gca_shots           -   Shots that lead to another goal-scoring shot
    gca_fouled          -   Fouls drawn that lead to a goal
    gca_defense         -   Defensive actions that lead to a goal


## Misc Table Features

    Y                   -   Yellow cards
    R                   -   Red cards
    YR                  -   2nd Yellow red card
    fouls               -   Fouls committed
    fouled              -   Fouls drawn
    offsides
    crosses
    interceptions
    tklw                -   Tackles won
    pens_won            -   Penalties won
    pens_conceded       -   Penalties conceded
    OG                  -   Own goals
    ball_recoveries
    aerials_won
    aerials_lost
    aerials_won_pct   


## Pass Types Table Features

    passes              -   Passes attempted
    passes_live         -   Live-ball passes
    passes_dead         -   Dead-ball passes
                            (includes FK, CK, GK, Kick-offs,Throw ins)
    passes_fk           -   Passes attempted from FK
    through_balls       -   Completed passes sent between back defenders into open space
    passes_switches     -   Passes over 40 yards the width of the pitch
    crosses
    throw_ins
    CK                  -   Corner kicks
    CK_in               -   Inswinging corner kicks
    CK_out              -   Outswinging corner kicks
    CK_s                -   Straight corner kicks
    passes_completed
    passes_offside
    passes_blocked      -   Blocked by the opponent who was standing in the path


## Passing Table Features

    passes_comp         -   Passes completed
    passes              -   Passes attempted
    passes_pct          -   Completed passes %
    passes_total_dist   -   Total distance in yards passes have traveled
    passes_prog_dist    -   Total distance in yards passes have traveled towards the opponent goal
    SPasses_comp        -   Short passes completed (5 to 15 yards)
    SPasses             -   Short passes attempted
    SP_pct              -   Short passes completed %
    MPasses_comp        -   Medium passes completed (15 to 30 yards)
    MPasses             -   Medium passes attempted
    MPasses_pct         -   Medium passes completed %
    LPasses_comp        -   Long passes completed (+30 yards)
    Lpasses             -   Long passes attempted
    LPasses_pct         -   Long passes completed %
    assists
    xAG                 -   xG which follows a pass that assists a shot
    xA                  -   Expected assists
                            (Likeliness of each completed pass to become an assist)
    xg_assist_net       -   (Assists minus xG assisted)
    KP                  -   Key passes (passes directly leading to a shot)
    P_into_fin3rd       -   Completed passes entering the final 3rd
    P_into_PA           -   Passes into penalty area
    C_into_PA           -   Crosses into penalty area
    prog_passes         -   Progressive passes
                            (Completed passes that move the ball towards opp goal at least 10 yards from its furthest point
                            in the last 6 passes+comp passes into penalty area)


## Playing Time Table Features

    games                   -   Games played
    minutes
    mins_per_game           -   Minutes played per game
    mins_pct                -   % of squand minutes played
    game_starts             -   Games started
    mins_per_start          -   Minutes player per game started
    games_completed         -   Games in which player played whole 90 minutes
    game_subs               -   Games entered as a sub
    mins_per_sub            -   Minutes played per games entered as a sub
    unused_sub              -   Games spent on the bench
    PPM                     -   Average points earned when the player appeared
    onG                     -   Goals scored by team while on pitch
    onGA                    -   Goals conceded by team while on pitch
    plus_minus              -   (GA minus onGA)
    plus_minus_per90        -   (GA minus onGA) per 90 minutes played
    plus_minus_wwo          -   Net goals per 90 while player was on - net goals per 90 while player was not on 
    onxG                    -   xG by team while player was on   
    onxGA                   -   xG against while player was on
    xg_plus_minus           -   xG scored minus goals allowed by team was on
    xg_plus_minus_per90     -   xG scored minus goals allowed by team was on per 90 minutes played
    xg_plus_minus_wwo       -   Difference of net expected goals per 90 minutes by team
                                while player was on and off the pitch


## Possession Table Featues

    touches                     -   Number of times a player touched the ball
                                    (dribbling and passing doesn't count as multiple touches)
    touches_dpa                 -   Touches in defensive penalty area
    touches_def_3rd             -   Touches in defensive 1/3
    touches_mid_3rd             -   Touches in middle 1/3
    touches_att_3rd             -   Touches in attacking 1/3
    touches_apa                 -   Touches in the attacking penalty area
    touches_live_ball           -   Live balls touched
    TO                          -   Number of attempts to take on defenders while dribbling
    TO_won                      -   Number of def. taken on successfully by dribbling past them
    TO_won_pct                  -   % of successful take-ons
    TO_tkld                     -   Number of times tackled by a defender during a take-on attempt
    TO_tkld_pct                 -   % of times tackled by a defender during a take-on attempt
    carries                     -   Number of times the player controlled the ball with their feet
    carries_dist                -   Total distance in yards a player moved the ball while controlling it with their feet
    carries_prog_dist           -   Total distance in yards a player moved the ball towards the opponent's goal
                                    while controlling it with his feet
    prog_carries                -   Carries that moved the ball towards the opp goal at least 10 yards
                                    from its furthest point in the last 6 passes + carries into the pen area
    carries_into_final_3rd      -   Carries that enter the final 1/3
    carries_into_pa             -   Carries into the penalty are
    miscontrols                 -   Times a player failed an attempt to gain control of a ball
    dispossessed                -   Times a player loses control of the ball after being tackled by an opp
                                    excluding attempted take-ons
    passes_received             -   Number of times a player successfully received a pass
    prog_passes_received        -   Completed passes that move the ball towards the opp goal
                                    at least 10 yards from its furthest point in the last 6 passes+carries into the pen area


## Shooting Table Features

    goals
    shots               -   Shots excluding pens
    SOTs                -   Shots on target excluding pens
    SOTs_pct            -   % of shots on target (.395 per squad to qualify as a leader)
    shots_per90         -   Shots total per 90 mins (minimum 30 mins played per squad to qualify as leader)
    SOT_per90           -   Shots on target per 90 mins
    goals_per_shot      -   Minimum .395 shots per squad to qualify as leader
    goals_per_SOT       -   Goals per shot on target, minimum .111 shots on target per squad to qualify as leader
    avg_shot_dist       -   Average distance in yards from goal all shots taken
    shots_fk            -   Shots from free kicks
    pens_scored         -   Penalty kicks scored
    pens_att            -   Penalty kicks attempted
    xg                  -   Expected goals, includes pens but not penalty shootouts
    npxg                -   Expected goals without penalties
    npxg_per_shot       -   Expected goals per shot excluding penalties
    xg_net              -   Goals minus xG, pens excluded
    npxg_net            -   Non penalty goals minus non penalty xG
