<!-- ## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

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
  - utter_iamabot -->


## create_epic_path_1
* greet
  - utter_greet
* create_issue_epic
  - create_epic_form
  - form{"name":"create_epic_form"}
  - form{"name":null}
  - utter_epic_cred
  <!-- - utter_create_issue_epic -->

## create_epic_path_2
* create_issue
  - utter_create_issue
* create_issue_epic
  - create_epic_form
  - form{"name":"create_epic_form"}
  - form{"name":null}
  - utter_epic_cred
  <!-- - utter_create_issue_epic -->

## create_story_path_1
* greet
  - utter_greet
* create_issue_story
  - create_story_form
  - form{"name":"create_story_form"}
  - form{"name":null}
  - utter_story_cred

## create_story_path_2
* create_issue
  - utter_create_issue
* create_issue_story
  - create_story_form
  - form{"name":"create_story_form"}
  - form{"name":null}
  - utter_story_cred


## create_bug_path_1
* greet
  - utter_greet
* create_issue_bug
  - create_story_form
  - form{"name":"create_bug_form"}
  - form{"name":null}
  - utter_bug_cred

## create_bug_path_2
* create_issue
  - utter_create_issue
* create_issue_bug
  - create_story_form
  - form{"name":"create_bug_form"}
  - form{"name":null}
  - utter_bug_cred

## create_task_path_1
* greet
  - utter_greet
* create_issue_task
  - create_task_form
  - form{"name":"create_task_form"}
  - form{"name":null}
  - utter_task_cred
## create_task_path_2
* create_issue
  - utter_create_issue
* create_issue_task
  - create_task_form
  - form{"name":"create_task_form"}
  - form{"name":null}
  - utter_task_cred


## create_subtask_path_1
* greet
  - utter_greet
* create_issue_subtask
  - create_subtask_form
  - form{"name":"create_subtask_form"}
  - form{"name":null}
  - utter_subtask_cred

## create_subtask_path_2
* create_issue
  - utter_create_issue
* create_issue_subtask
  - create_subtask_form
  - form{"name":"create_subtask_form"}
  - form{"name":null}
  - utter_subtask_cred


## get_all_project_path_1
* greet
 - utter_greet
* get_all_project_name
 - utter_get_all_project_name

## get_all_project_path_2
* get_all_project_name
 - utter_get_all_project_name

## create_version_path_1
* greet
  - utter_greet
* create_version
  - create_version_form
  - form{"name":"create_version_form"}
  - form{"name":null}
  - utter_version_cred

## create_version_path_2
* create_version
  - create_version_form
  - form{"name":"create_version_form"}
  - form{"name":null}
  - utter_version_cred


## create_project_path_1
* greet
 - utter_greet
* create_project
 - create_project_form
 - form{"name":"create_project_form"}
 - form{"name":null}
 - utter_project_cred

## create_project_path_2
* create_project
 - create_project_form
 - form{"name":"create_project_form"}
 - form{"name":null}
 - utter_project_cred


## create_group_path_1
* greet
 - utter_greet
* create_group
 - create_group_form
 - form{"name":"create_group_form"}
 - form{"name":null}
 - utter_group_cred


## create_group_path_2
* create_group
 - create_group_form
 - form{"name":"create_group_form"}
 - form{"name":null}
 - utter_group_cred



## add_user_to_group_path_1
* greet
 - utter_greet
* add_user_to_group
 - add_user_to_group_form
 - form{"name":"add_user_to_group_form"}
 - form{"name":null}
 - utter_add_user_to_group_cred

## add_user_to_project_path_2
* add_user_to_group
 - add_user_to_group_form
 - form{"name":"add_user_to_group_form"}
 - form{"name":null}
 - utter_add_user_to_group_cred



## get_user_in_group_path_1
* greet
 - utter_greet
* get_user_in_group
 - get_user_in_group_form
 - form{"name":"get_user_in_group_form"}
 - form{"name":null}
 - utter_get_user_in_group_cred

## get_user_in_group_path_2
* get_user_in_group
 - get_user_in_group_form
 - form{"name":"get_user_in_group_form"}
 - form{"name":null}
 - utter_get_user_in_group_cred

## get_issue_in_project_path_1
* greet
 - utter_greet
* get_issue_in_project
 - get_issue_in_project_form
 - form{"name":"get_issue_in_project_form"}
 - form{"name":null}
 - utter_get_issue_in_project_cred

## get_issue_in_project_path_2
* get_issue_in_project
 - get_issue_in_project_form
 - form{"name":"get_issue_in_project_form"}
 - form{"name":null}
 - utter_get_issue_in_project_cred
 
## get_issue_path_1
* greet
 - utter_greet
* get_issue
 - get_issue_form
 - form{"name":"get_issue_form"}
 - form{"name":null}
 - utter_get_issue_cred

## get_issue_path_2
* get_issue
 - get_issue_form
 - form{"name":"get_issue_form"}
 - form{"name":null}
 - utter_get_issue_cred

## get_status_of_issue_path_1
* greet
 - utter_greet
* get_status_of_issue
 - get_status_of_issue_form
 - form{"name":"get_status_of_issue_form"}
 - form{"name":null}
 - utter_get_status_of_issue_cred

## get_status_of_issue_path_2
* get_status_of_issue
 - get_status_of_issue_form
 - form{"name":"get_status_of_issue_form"}
 - form{"name":null}
 - utter_get_status_of_issue_cred


## get_issue_version_path_1
* greet
 - utter_greet
* get_issue_version
 - get_issue_version_form
 - form{"name":"get_issue_version_form"}
 - form{"name":null}
 - utter_get_issue_version_cred

## get_issue_version_path_2
* get_issue_version
 - get_issue_version_form
 - form{"name":"get_issue_version_form"}
 - form{"name":null}
 - utter_get_issue_version_cred


## add_comment_path_1
* greet
 - utter_greet
* add_comment
 - add_comment_form
 - form{"name":"add_comment_form"}
 - form{"name":null}
 - utter_add_comment_cred

## add_comment_path_2
* add_comment
 - add_comment_form
 - form{"name":"add_comment_form"}
 - form{"name":null}
 - utter_add_comment_cred


## delete_comment_path_1
* greet
 - utter_greet
* delete_comment
 - delete_comment_form
 - form{"name":"delete_comment_form"}
 - form{"name":null}
 - utter_delete_comment_cred

## delete_comment_path_2
* delete_comment
 - delete_comment_form
 - form{"name":"delete_comment_form"}
 - form{"name":null}
 - utter_delete_comment_cred



## get_comment_in_issue_path_1
* greet
 - utter_greet
* get_comment_in_issue
 - get_comment_form
 - form{"name":"get_comment_form"}
 - form{"name":null}
 - utter_get_comment_cred

## get_comment_in_issue_path_2
* get_comment_in_issue
 - get_comment_form
 - form{"name":"get_comment_form"}
 - form{"name":null}
 - utter_get_comment_cred


## add_worklog_path_1
* greet
 - utter_greet
* add_worklog
 - add_worklog_form
 - form{"name":"add_worklog_form"}
 - form{"name":null}
 - utter_add_worklog_cred 

## add_worklog_path_2
* add_worklog
 - add_worklog_form
 - form{"name":"add_worklog_form"}
 - form{"name":null}
 - utter_add_worklog_cred 


## delete_worklog_path_1
* greet
 - utter_greet
* delete_worklog
 - delete_worklog_form
 - form{"name":"delete_worklog_form"}
 - form{"name":null}
 - utter_delete_worklog_cred


## delete_worklog_path_2
* delete_worklog
 - delete_worklog_form
 - form{"name":"delete_worklog_form"}
 - form{"name":null}
 - utter_delete_worklog_cred


## get_worklog_in_issue_path_1
* greet
 - utter_greet
* get_worklog_in_issue
 - get_worklog_form
 - form{"name":"get_worklog_form"}
 - form{"name":null}
 - utter_get_worklog_cred

 
## get_worklog_in_issue_path_2
* get_worklog_in_issue
 - get_worklog_form
 - form{"name":"get_worklog_form"}
 - form{"name":null}
 - utter_get_worklog_cred


## interactive_story_1
* greet{"greet": "hello"}
    - utter_greet
* create_issue_epic{"create": "create", "issue_type": "epic", "epic_name": "text summarization"}
    - slot{"epic_name": "text summarization"}
    - slot{"issue_type": "epic"}
    - create_epic_form
    - utter_epic_cred
* issue_summary_entry{"issue_summary": "text summarization using nlp"}
    - slot{"issue_summary": "text summarization using nlp"}
    - utter_ask_description_entity
* description_entry{"description_entity": "text summarization of resume should be performed to fetch skills"}
    - slot{"description_entity": "text summarization of resume should be performed to fetch skills"}
    - utter_ask_version_entity
* project_version_entry{"version_entity": "version 3"}
    - slot{"version_entity": "version 3"}
    - utter_ask_project_name
* project_entry{"project_name": "Resume screening"}
    - slot{"project_name": "Resume screening"}
    - utter_ask_assignee_name_entry
* assignee_name_entry{"assignee_name": "myself"}
    - slot{"assignee_name": "myself"}
    - create_epic_form
    - utter_epic_cred
* goodbye