<!-- ## happy path
* greet
  - utter_greet -->
<!-- * mood_great
  - utter_happy -->

<!-- ## sad path 1
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
  - utter_goodbye -->

## say goodbye
* goodbye
  - utter_goodbye

<!-- ## bot challenge
* bot_challenge
  - utter_iamabot -->

## greet path
* greet
  - utter_greet

<!-- ## search path 2
* search 
  - utter_search
  - action_confirm_domain -->

## create path 2
* create 
  - utter_create
  <!-- - action_confirm_domain -->

## update path 2
* update
  - utter_update
  <!-- - action_confirm_domain -->
<!-- 
## search path 1
* greet
  - utter_greet
* search 
  - utter_search
  - action_confirm_domain -->

## update path 1
* greet
  - utter_greet
* update 
  - utter_update
  <!-- - action_confirm_domain -->

## create path 1
* greet
  - utter_greet
* create 
  - utter_create
  <!-- - action_confirm_domain -->
<!-- ## interactive_story_1
* greet
    - utter_greet
* search
    - utter_search -->

## commit_msg
* commitMsg
  - commit_msg_form
  - form{"name": "commit_msg_form"}
  - form{"name": null}
  - utter_slots_values

## commit_bitbucket path 1
* greet
  - utter_greet
* search
  - utter_search
* affirm
  - utter_get_exact_domain
* commitBitbucket
  - commit_form  
  - form{"name": "commit_form"}
  - form{"name": null}
  - utter_slots_values

## commit_bitbucket path 2
* greet
  - utter_greet
* commitBitbucket
  - commit_form
  - form{"name": "commit_form"}
  - form{"name": null}
  - utter_slots_values

## commit_bitbucket path 3
* commitBitbucket
  - commit_form
  - form{"name": "commit_form"}
  - form{"name": null}
  - utter_slots_values
## commit_bitbucket path 4
* greet
  - utter_greet
* search
  - utter_search
* deny
  - utter_rephrase_please

<!-- ## commit_bitbucket path 5
* bitbucket_action_entry
  - commit_form
  - form{"name": "commit_form"}
  - form{"name": null}
  - utter_slots_values -->

## search_errors path 1
* greet
  - utter_greet
* search
  - utter_search
* affirm
  - utter_get_exact_domain
* searchErrors
  - error_form
  - form{"name": "error_form"}
  - form{"name": null}
  - utter_error_query

## search_errors path 2
* greet
  - utter_greet
* searchErrors
  - error_form
  - form{"name": "error_form"}
  - form{"name": null}
  - utter_error_query

## search_errors path 3
* searchErrors
  - error_form
  - form{"name": "error_form"}
  - form{"name": null}
  - utter_error_query




## search_errors path 4
* greet
  - utter_greet
* search
  - utter_search
* deny
  - utter_rephrase_please

## search_errors path 5
* error_action_entry
  - error_form
  - form{"name": "error_form"}
  - form{"name": null}
  - utter_error_query

## watchers_list
* watchersList
  - watchers_form
  - form{"name": "watchers_form"}
  - form{"name": null}
  - utter_slots_values

## repo_list
* repoList
  - repo_form
  - form{"name": "repo_form"}
  - form{"name": null}
  - utter_slots_values

## branch_list
* branchList
  - branch_form
  - form{"name": "branch_form"}
  - form{"name": null}
  - utter_slots_values




<!-- ## interactive_story_1
* commitMsg{"search_keys": " search_keys", "bitbucket_action": "code", "message": "text summarization"}
    - slot{"bitbucket_action": "code"}
    - slot{"message": "text summarization"}
    - slot{"search_keys": " search_keys"}
    - commit_msg_form
    - form{"name": "commit_msg_form"}
    - slot{"bitbucket_action": "code"}
    - slot{"message": "text summarization"}
    - slot{"bitbucket_action": "code"}
    - slot{"message": "text summarization"}
    - slot{"requested_slot": "repo_name"}
* form: repo_name_entry{"repo_name": "secTest"}
    - slot{"repo_name": "secTest"}
    - form: commit_msg_form
    - slot{"repo_name": "secTest"}
    - slot{"requested_slot": "owner_name"}
* form: owner_name_entry{"owner_name": "jkhan01"}
    - slot{"owner_name": "jkhan01"}
    - form: commit_msg_form
    - slot{"owner_name": "jkhan01"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values -->
