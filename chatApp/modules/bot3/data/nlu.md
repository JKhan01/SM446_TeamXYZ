## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there
- Jarvis
- jarvis
- greetings
- hey jarvis

## intent:goodbye
- bye
- goodbye
- see you around
- see you later
- thank you
- that's it

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct
- great
- yeah

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- C

## intent:create
- create a page on project
- generate a new project
- add
- new
- schedule a deadline

## intent:search
- find the solution
- help me out 
- open the platform
- read for me
- what is the 

- check for the solution
- search
- bring me the progress
- update
- get
- hey Jarvis, find me the latest commit
- hey jarvis, get [me](search_keys) the update




## intent:commitMsg
- hey Jarvis, [get](search_key) the [commit](bitbucket_action) for [story text extraction]{"entity": "message", "value": "text extraction"}
- [fetch the](search_key) [commit](bitbucket_action) details with [message payment operation]{"entity": "message", "value": "payment operation"}
- who did the [commit](bitbucket_action) for [text summarization](message)
- [get me]{"entity": "search_keys", "value": " search_keys"} the [commit]{"entity": "bitbucket_action", "value": "code"} for [story text summarization]{"entity": "message", "value": "text summarization"}

## intent:message_entry
- [text summarization](message)
- the story for which the [commit](bitbucket_action) is [payment operation]{"entity": "message", "value": "text summarization"}
- the comment for the [commit](bitbucket_action) should be [order operation]{"entity": "message", "value": "text summarization"}.

## intent:commitBitbucket
- hey Jarvis, [find me](search_keys) the latest [commit](bitbucket_action)
- [find me](search_keys) the last update from user [jamaluddin](user_name) on [repo](bitbucket_key)
- [get me](search_keys) the [code](bitbucket_action).
- bitbucket
- hey, [get me](search_keys) the [code](bitbucket_action) on [test](repo_name)
- hey, [get me](search_keys) the [code](bitbucket_action) on [test](repo_name) under [atlassian](owner_name).
- hey, [get me](search_keys) the [code](bitbucket_action) on [repository test]{"entity": "repo_name", "value": "test"} [atlassian project]{"entity": "owner_name", "value": "atlassian"}.
- Jarvis, [get me](search_keys) the [code](bitbucket_action) on [repository test]{"entity": "repo_name", "value": "test"} under [project atlassian](owner_name).
- Jarvis, [get me](search_keys) the latest [commit](bitbucket_action) on branch [master](branch_name).
- [get me](search_keys) the [code](bitbucket_action) from [master](branch_name) branch of [repository](bitbucket_key) [atlassian](repo_name)
- [get me](search_keys) the [code](bitbucket_action) from [master](branch_name) branch of [atlassian repository]{"entity": "repo_name", "value": "atlassian"}
- [get me]{"entity": "search_keys", "value": " search_keys"} the last [commit code](bitbucket_action) on [repo atlassian]{"entity": "repo_name", "value": "atlassian"}
- who did the last [commit](bitbucket_action) on [sih repo]{"entity": "repo_name", "value": "sih"} under [project atlassianwork](owner_name)?
- Jarvis, when was the last [commit](bitbucket_action) made on [repo art-2020]{"entity": "repo_name", "value": "art-2020"}
- Jarvis, on [repo art-2020]{"entity": "repo_name", "value": "art-2020"}, when was the last [commit]{"entity": "bitbucket_action", "value": " commit"} made
- hey jarvis, on [repository robocon]{"entity": "repo_name", "value": "robocon"} who made the last [commit](bitbucket_action)
- [find]{"entity": "search_keys", "value": " search_keys"} the latest update on [repo arcWork]{"entity": "repo_name", "value": "arcWork"}
- jarvis, [get me]{"entity": "search_keys", "value": " search_keys"} the last [commit]{"entity": "bitbucket_action", "value": "code"} on [repo sihWork](repo_name)
- hey jarvis, [who](search_keys) did the [last](duration_keys) [commit](bitbucket_action) on [repo trialApp](repo_name)
- [who](search_keys) made the last [commit](bitbucket_action)
- [who]{"entity": "search_keys", "value": " search_keys"} did the last [commit]{"entity": "bitbucket_action", "value": "code"} on [repo workingonatlassianapis]{"entity": "repo_name", "value": "wokringonatlassianapis"} under [workspace jkhan01]{"entity": "owner_name", "value": "jkhan01"}

## intent:watcherList
- hey Jarvis, [get me](search_keys) the list of [watchers](bitbucket_action) on [repo workingonatlassianapis]{"entity": "repo_name", "value": "wokringonatlassianapis"}
- [who all](search_keys) are the watchers on [repo test]{"entity": "repo_name", "value": "test"}
- [get me](search_keys) the [watchers](bitbucket_action).
- list all the [watchers](bitbucket_action).
- jarvis, [get me]{"entity": "search_keys", "value": " search_keys"} the list of [developers]{"entity": "bitbucket_action", "value": "watchers"} on [repository]{"entity": "bitbucket_key", "value": "bitbucket_key"}
- [I want](search_keys) to know [who all](search_keys) are [watchers](bitbucket_action) on the [repository atlassianWork]{"entity": "repo_name", "value": "atlassianWork"} under [art-2020](owner_name)
- Good morning Jarvis, please [get me]{"entity": "search_keys", "value": " search_keys"} the list of [watchers](bitbucket_action) on [test3 repository]{"entity": "repo_name", "value": "test3"}
- [I want](search_keys) to know [who all](search_keys) are [watchers](bitbucket_action) on the [repository atlassianWork]{"entity": "repo_name", "value": "atlassianWork"} under [project art-2020](owner_name)

## intent:repoList
- hey Jarvis, [get me](search_keys) the list of [repository](repo_key).
- [what are](search_keys) the [repositories](repo_key) under [workspace jkhan01]{"entity": "owner_name", "value": "jkhan01"}?
- find all the [repos](repo_key) with [owner art-2020]{"entity": "owner_name", "value": "art-2020"}
- list all [repo](repo_key) owned by [tanmaygujar](owner_name)

## intent:branchList
- [get me](search_keys) the branches on [repo workingonatlassianapis]{"entity": "repo_name", "value": "wokringonatlassianapis"}
- hey Jarvis, [find the](search_keys) branches under [repository test]{"entity": "repo_name", "value": "test"}
- list all the branches.
- [find the](search_keys) name of branches of type [release](branch_type).
- hey Jarvis, [get me](search_keys) branches under [art-2020 repo]{"entity": "repo_name", "value": "art-2020"} owned by [jkhan01](owner_name)
- [get](search_keys) the list of branches under [test repo]{"entity": "test", "value": "test"}

## intent:searchErrors
- hey Jarvis, [find me](search_keys) the [solution to the error](error_keys)
- [Help me](search_keys) out with the [error](error_keys)
- [what is](search_keys) the best answer to the [problem of value error](error_keys)?
- Stackoverflow
- hey, [solve](error_keys) the error for me.
- stackoverflow
- [find me]{"entity": "search_keys", "value": " search_keys"} the optimal [solution to](error_keys) the [error]{"entity": "error_keys", "value": " error"}
- [find]{"entity": "search_keys", "value": " search_keys"} the [solution to](error_keys) [the class not found error](error_action)
- Fetch [me](search_keys) the best [solution to](error_keys) the [invalid input for json error](error_action)
- yes, [i want](search_keys) [solution](error_keys)
- hey, [get me]{"entity": "search_keys", "value": " search_keys"} the [best answer](error_keys) to the [error](error_keys)
- hey jarvis, help [me](search_keys) with the solution
- fetch [me](search_keys) the solution
## intent:error_action_entry
- [the class not found error](error_action)
- the error is [value not found]{"entity": "error_action", "value": "value not found error"}
- It reads [invalid token error](error_action)
- [floating point error](error_action)
- [no module name flask found](error_action)

## intent:repo_name_entry
- [test](repo_name)
- the repository on target is [webApp](repo_name)
- repo name is [mobileApp](repo_name)
- [webApp](repo_name)
- i am talking about [secTest](repo_name)

## intent:owner_name_entry
- the slug name of owner is [jkhan01](owner_name)
- [art2020](owner_name) is the owner
- I am the owner
- me, my slug is [tanmaygujar](owner_name)
- the [owner](owner_key) of the [workspace](owner_key) is [jkhan01](owner_name)
- [jkhan01](owner_name)

## intent:user_name_entry
- user name is [jamal](user_name)
- [rohit](user_name) is the user name i am looking for
- [Jamal](user_name)
- user is [tanmay](user_name)
- No, [not any user-specific]{"entity": "user_name", "value": "any"}
- [Not specific to any user]{"entity": "user_name", "value": "any"}

## intent:branch_name_entry
- [master](branch_name) is the branch name
- the branch is [version](branch_name)
- [stable](branch_name) is the branch of type [bugfixes](branch_type)
- [master](branch_name)
- [version-2.x](branch_name) branch
- in [general]{"entity": "branch_name", "value": "any"}
- [Not specific to any branch]{"entity": "branch_name", "value": "any"}
- [Just get me the changes]{"entity": "branch_name", "value": "any"}
- It should be on branch [testing](branch_name)

## intent:branch_type_entry
- [release](branch_type)
- [bugfixes](branch_type)
- [other](branch_type)
- [feature](branch_type)
- [hotfix](branch_type)

## intent:bitbucket_action_entry
- [commit]{"entity": "bitbucket_action", "value": "code"}
- i want the [code](bitbucket_action)
- [watchers](bitbucket_action)
- list of [watchers]{"entity": "bitbucket_action", "value": "list of watchers"}

## intent:update
- add the filter to
- set the deadline to
- change the requirements
- reschedule the meeting
- set a new dependancy
- update
- remove the release note
- postpone
- reschedule the deadline

## synonym: bitbucket_action
- commit
- developers
- list of watchers
- watchers
- code
- source code
- list of users
- list of developers
- users

## synonym: bitbucket_key
- repository
- repo
- bitbucket
- branch
- project

## synonym: duration_keys
- since last weekend
- since
- since yesterday
- over the past month
- overnight
- in fortnight
- the latest

## synonym: error_keys
- error
- solution to the error
- problem
- issue
- answer
- solution

## synonym: search_keys
- get me
- find
- who
- find me
- search
- fetch
- bring
- can you get me
- please update me
- get
- check
- Help me
- what is
- when is
- i want
- who all
- i need

## synonym:"duration_keys","value":"last"
- last

## synonym:any
- not any user-specific
- Not specific to any user
- general
- Not specific to any branch
- Just get me the changes

## synonym:arcWork
- repo arcWork

## synonym:art-2020
- repo art-2020
- owner art-2020
- art-2020 repo

## synonym:atlassian
- atlassian project
- atlassian repository
- repo atlassian

## synonym:atlassianWork
- repository atlassianWork

## synonym:jkhan01
- workspace jkhan01

## synonym:payment operation
- message payment operation

## synonym:repo_key
- repos
- repositories

## synonym:robocon
- repository robocon

## synonym:sih
- sih repo

## synonym:test
- repository test
- repo test
- test repo
- project test

## synonym:test3
- test3 repository

## synonym:text extraction
- story text extraction

## synonym:text summarization
- payment operation
- order operation

## synonym:value not found error
- value not found

## synonym:wokringonatlassianapis
- repo workingonatlassianapis
