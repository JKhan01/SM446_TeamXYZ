## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- [hello](greet)

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- thankyou

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:create_issue_epic
- [hey Jarvis](greet), [create](create) an [epic](issue_type) for me.
- [Make](create) an [epic](issue_type) with name [login](epic_summary).
- [create](create) an [epic](issue_type) with name [text summarization](epic_name)

## intent:issue_type_entry
- [epic](issue_type)
- create [story]{"entity": "issue_type", "value": "Story"}
- I want [task]{"entity": "issue_type", "value": "Task"}
- [subtask]{"entity": "issue_type", "value": "Subtask"}
- [bug]{"entity": "issue_type", "value": "Bug"}

## intent:create_issue
- [make](create) an issue for me
- [jarvis](greet), [create](create) issue
- [hey jarvis](greet), [generate](create) a new issue.
- [hi](greet), add issue [text extraction](issue_summary)

## intent:epic_name_entry
- The name of the epic is [login](epic_name)
- [test](epic_name)
- [frontentd development](epic_name)
- [database integration](epic_name)

## intent:issue_summary_entry
- [text summarization](issue_summary)
- the issue is [browse](issue_summary)
- the issue name is [order operation](issue_summary)
- name is [payment operation](issue_summary)
- summary is [track](issue_summary)
- the issue summary is [text extraction](issue_summary)
- task summary is [create registration page](issue_summary)
- story summary is [make login page](issue_summary)
- epic summary is [develop add and remove from cart feature](issue_summary)
- bug summary is [cash payment function](issue_summary)
- bug is [debit/credit card payment feature](issue_summary)
- story is [ETA support](issue_summary)
- task is [support tool](issue_summary)
- sub task is [duplicate previous order](issue_summary)
- epic is [database formation](issue_summary)
- [wrong credentials](issue_summary) bug
- set summary as [text summarization using nlp](issue_summary)

## intent:assignee_name_entry
- assign to [rohit](assignee_name)
- [raj](assignee_name) is leader
- make [jamal](assignee_name) the leader
- [hi](greet) make [myself](assignee_name)
- assign it to [myself](assignee_name)

## intent:description_entry
- description is [hello world](description_entity)
- story description is [Developing a browse operation](description_entity)
- epic description [generate all order operations](description_entity)
- task description [work on different payment options](description_entity)
- sub task description [design and develop registration page for user](description_entity)
- bug description [develop login page with php](description_entity)
- [user cam add and remove elemnts ino the cart](description_entity)
- [credentials are not matching](description_entity)
- [data not getting stored in data base](description_entity)
- description is [text summarization of resume should be performed to fetch skills](description_entity)

## intent:project_version_entry
- [version 1.2](version_entity)
- version is [release 2.0](version_entity)
- [alpha version](version_entity)
- [version beta](version_entity)
- release [version 3](version_entity)

## intent:project_entry
- [project Resume Screening](project_name)
- project is [project automated surveying](project_name)
- The name of the project is [corporate jarvis](project_name)
- project is [Resume screening](project_name)

## intent:create_issue_story
- [hey Jarvis](greet), [create](create) an [story]{"entity": "issue_type", "value": "Story"} for me.
- [Make](create) an [story]{"entity": "issue_type", "value": "Story"} with name [login](issue_summary).
- [hello](greet) [add](create) [story]{"entity": "issue_type", "value": "Story"}

## intent:create_issue_bug
- [hey Jarvis](greet), [create](create) an [bug]{"entity": "issue_type", "value": "Bug"} for me.
- [Make](create) an [bug]{"entity": "issue_type", "value": "Bug"} with name [login credential match error](issue_summary).
- [hello](greet) [add](create) [bug]{"entity": "issue_type", "value": "Bug"}

## intent:create_issue_task
- [hey Jarvis](greet), [create](create) an [task]{"entity": "issue_type", "value": "Task"} for me.
- [Make](create) an [task]{"entity": "issue_type", "value": "Task"} with name [login credential match error](issue_summary).
- [hello](greet) [add](create) [task]{"entity": "issue_type", "value": "Task"}

## intent:create_issue_subtask
- [hey Jarvis](greet), [create](create) an [sub task]{"entity": "issue_type", "value": "subtask"} for me.
- [Make](create) an [sub task]{"entity": "issue_type", "value": "subtask"} with name [login credential match error](issue_summary).
- [hello](greet) [add](create) [sub task]{"entity": "issue_type", "value": "subtask"}

## intent:get_all_project_name
- [hey jarvis](greet) [fetch](search_keys) all projects
- [hi](greet) [fetch](search_keys) all projects
- [hello](greet) can you [get](search_keys) project names
- [hey](greet) [what](search_keys) are the projects
- [list](search_keys) project names

## intent:create_version
- [hi jarvis](greet) [create](create) version [version 2.0](version_entity)
- [create](create) release [alpha version](version_entity)
- [add](create) release [release 1](version_entity)

## intent:release_date_entry
- release date is [2020/07/24](release_date)
- release on [2021/08/30](release_date)
- expected on [2023/01/01](release_date)
- [2023/05/21](release_date)

## intent:start_date_entry
- started on [2020/07/24](start_date)
- from [2020/07/24](start_date)
- [2020/07/24](start_date)

## intent:is_released
- [yes]{"entity": "released_status", "value": "True"} released
- [true]{"entity": "released_status", "value": "True"}
- [yes]{"entity": "released_status", "value": "True"}
- [no]{"entity": "released_status", "value": "False"}
- [false]{"entity": "released_status", "value": "False"}
- [not yet]{"entity": "released_status", "value": "False"}

## intent:create_project
- [hi jarvis](greet) [create](create) project [resume screening](project_name)
- [add](create) project [corporate jarvis](project_name)
- [jarvis](greet) [generate](create) project [bank management system](project_name)
- [make](create) a project [hotel booking app](project_name)

## intent:template_entry
- template is [content management](project_template)
- [document approval](project_template)
- [lead tracking](project_template) template
- model is [scrum](project_template)
- [kanban](project_template) model
- [process control](project_template)
- [procurement](project_template)
- [project management](project_template)
- [recruitment](project_template)
- [task tracking](project_template)
- [it](project_template)
- [internal](project_template)
- [external](project_template)

## intent:template_type_entry
- type is [business](temp_type)
- [software](temp_type) type
- [service desk](temp_type)

## intent:project_key_entry
- add key [RS](project_key)
- [AM](project_key)
- [DM](project_key)
- [ST](project_key)
- [OK](project_key)

## intent:project_lead_name_entry
- [myself](project_lead)
- [ram](project_lead) is the leader
- leader is [raju](project_lead)
- assign it to [soham](project_lead)
- assign it to [abhinav](project_lead)

## intent:create_group
- [make](create) a group [developers](group_name)
- [create](create) a group [administrators](group_name)
- [generate](create) group [managers](group_name)
- [hi](greet) [create](group) group naming [assistant manager](group_name)

## intent:add_user_to_group
- [hi](greet) add [rohit](user_name) to [developers](group_name)
- in [developers](group_name) add [raju](user_name)
- add [sushant](user_name) to [managers](group_name)
- add user [rakesh](user_name) to group [administrators](group_name)
- add user [abhinav](user_name) to [assistant manager](group_name)
- add [sharon](user_name) to group [creative](group_name)

## intent:group_name_entry
- group name is [designers](group_name)
- group is [administrators](group_name)
- name is [creative](group_name)
- [manager](group_name) group

## intent:user_name_entry
- user [sharon](user_name)
- user is [gloria](user_name)
- name is [rohit](user_name)
- [akash](user_name) is user name
- user name is [aditya](user_name)
- name of user is [jaideep](user_name)

## intent:get_user_in_group
- [find](search_keys) users in group [designers](group_name)
- [find](search_keys) users in [administrators](group_name)
- [list](search_keys) users in [developers](group_name)
- [list](search_keys) users in [creative](group_name) group
- [who](search_keys) are in [managers](group_name) group
- [who](search_keys) are in [creative](group_name)
- [get](search_keys) users in [manager](group_name)
- [get](search_keys) user in group [administrator](group_name)

## intent:get_issue_in_project
- [find](search_keys) all issues in project [resume screening](project_name)
- [get](search_keys) issues in [corporate jarvis](project_name) project
- [list](search_keys) all issues in [bank management system](project_name)
- [what](search_keys) are issues in [hotel booking system](project_name)

## intent:get_issue
- [get](search_keys) issue [text summarization](issue_summary) details
- [fetch](search_keys) [browse](issue_summary) issue
- [find](search_keys) issue [system error](issue_summary) details

## intent:get_status_of_issue
- [get](search_keys) status of issue [text summarization](issue_summary)
- [what](search_keys) is status of [browse](issue_summary) issue
- [find](search_keys) status of [system error](issue_summary)
- [fetch](search_keys) status of [system error](issue_summary) issue

## intent:get_issue_version
- [get](search_keys) version of issue [text summarization](issue_summary)
- [what](search_keys) is release of [browse](issue_summary) issue
- [find](search_keys) release date of [system error](issue_summary)
- [fetch](search_keys) version details of [system error](issue_summary) issue

## intent:add_comment
- [hi](greet) [add](create) comment [completed research on NLP](comment) for [text summarization](issue_summary) issue
- can you [add](create) [keep doing work](comment) comment on issue [browse](issue_summary)
- please [add](create) comment [get project report done by 12 th june](comment) on  issue [system error](issue_summary)
- [post](create) comment [text cleaning is ready](comment) on [system error](issue_summary)

## intent:delete_comment
- [hi](greet) [delete](delete) comment [completed research on NLP](comment) on [text summarization](issue_summary)
- [delete](delete) [keep doing work](comment) comment on [browse](issue_summary) issue
- [remove](delete) [get project report done by 12 th june](comment) comment from issue [system error](issue_summary)

## intent:get_comments_in_issue​
- [hi](greet) [get](search_keys) all comments on [system error](issue_summary)
- [fetch](search_keys) me all comment on [browse](issue_summary)
- [find](search_keys) all comment on issue [text summarization](issue_summary)

## intent:add_worklog
- [hi](greet) [add](create) [done with database](worklog) worklog in issue [system error](issue_summary) started [3](week) week [2](day) day [12](hour) hour and [30](minute) minute ago
- [add](create) worklog [done with design layout](worklog) on [browse](issue_summary) issue began before [12](week) weeks [7](day) days [23](hour) hours and [59](minute) minutes before
- [hi](greet) [create](create) worklog [done with front end design](worklog) for issue [text summarization](issue_summary)
- started [0](week) week [2](day) day [5](hour) hours and [15](minute) minutes ago on issue [text summarization](issue_summary) [add](create) worklog [half data entered](worklog)

## intent:delete_worklog
- [hi](greet) [delete](delete) [done with database](worklog) from issue [system error](issue_summary)
- from issue [browse](issue_summary) [delete](delete) [done with design layout](worklog) worklog
- [remove](delete) [half data entered](worklog) worklog from [text summarization](issue_summary)

## intent:get_worklog_in_issue
- [hi](greet) [get](search_keys) all worklogs from [system error](issue_summary)
- [fetch](search_keys) worklogs in [browse](issue_summary)
- [find](search_keys) all worklogs from [text summarization](issue_summary)
- from [text summarization](issue_summary) [get](search_keys) all worklog

## intent:visible_to_role_entry
- visible to [administrators](visible_to_role)
- [developers](visible_to_role) can see
- visible to all [managers](visible_to_role)

## synonym:Bug
- bug

## synonym:False
- no
- false
- not yet

## synonym:Story
- story

## synonym:Subtask
- subtask

## synonym:Task
- task

## synonym:True
- yes
- true

## synonym:create
- create
- generate
- add
- new
- schedule
- make

## synonym:delete
- delete
- remove

## synonym:subtask
- sub task
