## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy
## hello world path
* hello_world
  - action_hello_world

## covid zones path
* covid19_zone_status
  - action_covid19_zone_status

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## covid status
* covid19_status
  - action_covid19_status_tracker
  
