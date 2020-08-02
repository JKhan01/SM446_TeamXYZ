## happy path
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## info of all spaces
* greet
  - utter_greet
* info_of_all_spaces
  - utter_info_of_all_spaces  
* goodbye
  - utter_goodbye

## commitMsg path
* commit_msg
  - commit_msg_form
  - form{"name": "commit_msg_form"}
  - form{"name": null}
  - utter_commitMsg


## searchError path
* error_search
  - error_search_form
  - form{"name": "error_search_form"}
  - form{"name": null}
  - utter_searchErrors


## searchError path 2
* greet
  - utter_greet
* error_search
  - error_search_form
  - form{"name": "error_search_form"}
  - form{"name": null}
  - utter_searchErrors
## create space path
* greet
  - utter_greet
* create_space
  <!-- - create_space_form
  - form{"name" : "create_space_form"}
  - form{"name" : null}
  - utter_create_space_slot_values
  - utter_submit -->
  - utter_create_space
* goodbye
  - utter_goodbye

## watcherList path 1
* watcher_list
  - watcher_list_form
  - form{"name": "watcher_list_form"}
  - form{"name": null}
  - utter_watcherList

## watcherList path 2
* greet
  - utter_greet
* watcher_list
  - watcher_list_form
  - form{"name": "watcher_list_form"}
  - form{"name": null}
  - utter_watcherList


## space name entry path
* space_name_entry
  - utter_space_name_entry


## space key entry path 1
* space_key_entry
  - utter_space_key_entry

## space key entry path 2
* greet
  - utter_greet
* space_key_entry
  - utter_space_key_entry


## info of a space path 1
* info_of_a_space
  - utter_info_of_a_space

## info of a space path 2
* greet
  - utter_greet
* info_of_a_space
  - utter_info_of_a_space


## get pages in a space path 1
* greet
  -utter_greet
* get_pages_in_a_space
  <!-- - action_get_pages_in_a_space
  - utter_pages_in_a_space_slot_value
  - utter_submit   -->
  - utter_get_pages_in_a_space
* goodbye
  - utter_goodbye


## get pages in a space path 2
* get_pages_in_a_space
  <!-- - action_get_pages_in_a_space
  - utter_pages_in_a_space_slot_value
  - utter_submit   -->
  - utter_get_pages_in_a_space
<!-- ## interactive_story_1
* watcherList{"search_key": " search_key", "repo_key": "repo"}
    - utter_watcherList
* watcherList{"search_key": " search_key", "repo_key": "repo", "repo_name": "art-2020"}
    - slot{"repo_name": "art-2020"}
    - utter_watcherList
* watcherList{"repo_key": "repo", "repo_name": "secTest"}
    - slot{"repo_name": "secTest"}
    - utter_watcherList
* create_space{"space": "plagiarisms"}
    - slot{"space": "plagiarisms"}
    - utter_create_space
* repo_name_entry{"repo_key": "repo", "repo_name": "sih2020"}
    - slot{"repo_name": "sih2020"}
    - utter_repo_name_entry
* commitMsg{"search_key": "fetch me", "message": "operation"}
    - slot{"message": "operation"}
    - utter_commitMsg
* info_of_all_spaces{"search_key": " search_key"}
    - utter_info_of_all_spaces
* message_entry{"message": "transaction operation"}
    - slot{"message": "transaction operation"}
    - utter_message_entry -->



## repoList path 1
* repo_list
  - repo_list_form
  - form{"name": "repo_list_form"}
  - form{"name": null}
  - utter_repoList

## branchList path 1
* branch_list
  - branch_list_form
  - form{"name":"branch_list_form"}
  - utter_branchList

<!-- ## branch type entry path 1
* branch_type_entry
  - utter_branch_type_entry -->

<!-- ## branch name entry path 1
* branch_name_entry
  - utter_branch_name_entry -->

## commit by user path
* commit_by_user
  - commit_by_user_form
  - form{"name": "commit_by_user_form"}
  - form{"name": null}
  - utter_commit_by_user

## commit by branch path
* commit_by_branch
  - commit_by_branch_form
  - form{"name": "commit_by_branch_form"}
  - form{"name": null}
  - utter_commit_by_branch
<!-- ## interactive_story_1
* commit_by_branch{"search_key": "who", "bitbucket_action": " commit", "branch_name": "master"}
    - slot{"branch_name": "master"}
    - utter_commit_by_branch
* commit_by_user{"search_key": " search_key", "user_name": "tanmay"}
    - slot{"user_name": "tanmay"}
    - utter_commit_by_user
* info_of_all_spaces{"search_key": "get all"}
    - utter_info_of_all_spaces
* create_space{"create_key": " create_key", "space": "Demo3"}
    - slot{"space": "Demo3"}
    - utter_create_space
* info_of_a_space{"search_key": " search_key", "key": "timepass"}
    - slot{"key": "timepass"}
    - utter_info_of_a_space
* get_pages_in_a_space{"search_key": "bring me", "space": "setup"}
    - slot{"space": "setup"}
    - utter_get_pages_in_a_space -->

## interactive_story_1
* watcher_list{"search_key": " search_key"}
    - watcher_list_form
    - form{"name": "watcher_list_form"}
    - slot{"requested_slot": "repo_name"}
* form: repo_name_entry{"repo_name": "workingonatlassianapis"}
    - slot{"repo_name": "workingonatlassianapis"}
    - form: watcher_list_form
    - slot{"repo_name": "workingonatlassianapis"}
    - slot{"requested_slot": "owner_name"}
* form: owner_name_entry{"owner_name": "jkhan01"}
    - slot{"owner_name": "jkhan01"}
    - form: watcher_list_form
    - slot{"owner_name": "jkhan01"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_watcherList

## interactive_story_2
* repo_list{"search_key": " search_key", "repo_key": "repositories"}
    - repo_list_form
    - form{"name": "repo_list_form"}
    - slot{"requested_slot": "owner_name"}
* form: owner_name_entry{"owner_name": "jkhan01"}
    - slot{"owner_name": "jkhan01"}
    - form: repo_list_form
    - slot{"owner_name": "jkhan01"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_repoList
* watcher_list{"search_key": "get", "repo_key": "repo", "repo_name": "test"}
    - slot{"repo_name": "test"}
    - watcher_list_form
    - form{"name": "watcher_list_form"}
    - slot{"repo_name": "test"}
    - slot{"owner_name": "jkhan01"}
    - slot{"repo_name": "test"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_watcherList

## interactive_story_3
* watcher_list{"search_key": " search_key", "repo_key": "repo", "repo_name": "test", "owner_name": "jkhan01"}
    - slot{"owner_name": "jkhan01"}
    - slot{"repo_name": "test"}
    - watcher_list_form
    - form{"name": "watcher_list_form"}
    - slot{"repo_name": "test"}
    - slot{"owner_name": "jkhan01"}
    - slot{"repo_name": "test"}
    - slot{"owner_name": "jkhan01"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_watcherList
* watcher_list{"search_key": " search_key", "repo_key": "repo", "repo_name": "art-2020", "owner_name": "art2020"}
    - slot{"owner_name": "art2020"}
    - slot{"repo_name": "art-2020"}
    - watcher_list_form
    - form{"name": "watcher_list_form"}
    - slot{"repo_name": "art-2020"}
    - slot{"owner_name": "art2020"}
    - slot{"repo_name": "art-2020"}
    - slot{"owner_name": "art2020"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_watcherList
* commit_by_branch{"bitbucket_action": " commit", "repo_key": "repo", "owner_name": "art-2020", "repo_name": "art2020"}
    - slot{"owner_name": "art2020"}
    - slot{"repo_name": "art-2020"}

## interactive_story_4
* commit_by_branch{"bitbucket_action": " commit", "repo_key": "repo", "repo_name": "art-2020", "owner_name": "art2020"}
    - slot{"owner_name": "art2020"}
    - slot{"repo_name": "art-2020"}
    - commit_by_branch_form
    - form{"name": "commit_by_branch_form"}
    - slot{"repo_name": "art-2020"}
    - slot{"owner_name": "art2020"}
    - slot{"repo_name": "art-2020"}
    - slot{"owner_name": "art2020"}
    - slot{"requested_slot": "branch_name"}
* form: branch_name_entry{"branch_name": "master"}
    - slot{"branch_name": "master"}
    - form: commit_by_branch_form
    - slot{"branch_name": "master"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_commit_by_branch
* commit_by_branch{"search_key": "fetch me", "bitbucket_action": " commit", "repo_key": "repo", "owner_name": "art2020", "repo_name": "art-2020"}
    - slot{"owner_name": "art2020"}
    - slot{"repo_name": "art-2020"}

## interactive_story_1
* commit_by_user{"search_key": " search_key", "user_name": "prathamesh"}
    - slot{"user_name": "prathamesh"}
    - commit_by_user_form
    - form{"name": "commit_by_user_form"}
    - slot{"user_name": "prathamesh"}
    - slot{"user_name": "prathamesh"}
    - slot{"requested_slot": "repo_name"}
* form: repo_name_entry{"repo_key": "repo", "repo_name": "art-2020"}
    - slot{"repo_name": "art-2020"}
    - form: commit_by_user_form
    - slot{"repo_name": "art-2020"}
    - slot{"requested_slot": "owner_name"}
* form: owner_name_entry{"owner_name": "art2020"}
    - slot{"owner_name": "art2020"}
    - form: commit_by_user_form
    - slot{"owner_name": "art2020"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_commit_by_user
* commit_msg{"search_key": " search_key"}
    - commit_msg_form
    - form{"name": "commit_msg_form"}
    - slot{"repo_name": "art-2020"}
    - slot{"owner_name": "art2020"}
    - slot{"requested_slot": "message"}
* form: message_entry{"message": "transaction operation", "bitbucket_action": " commit"}
    - slot{"message": "transaction operation"}
    - form: commit_msg_form
    - slot{"message": "transaction operation"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_commitMsg
