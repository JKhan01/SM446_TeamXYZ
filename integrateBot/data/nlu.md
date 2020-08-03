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
- thank you jarvis
- thank you for your service jarvis
- thank you for your service

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

## intent:commit_msg
- hey Jarvis, [get](search_key) the commit for story [text extraction](message)
- [fetch the](search_key) commit details with [message payment operation]{"entity": "message", "value": "payment operation"}
- who did the commit for [text summarization](message)
- [get me]{"entity": "search_key", "value": " search_key"} the commit for story ["text summarization"]{"entity": "message", "value": "text summarization"}
- jarvis, [fetch me](search_key) the commit details with comment login [operation](message)
- [get me]{"entity": "search_key", "value": " search_key"} the commit by message

## intent:message_entry
- [text summarization](message)
- the story for which the commit is [payment operation](message)
- the comment for the commit should be [order operation](message).
- the [transaction operation](message)
- [transaction operation](message) was the message of the [commit]{"entity": "bitbucket_action", "value": " commit"}

## intent:commit_by_branch
- hey Jarvis, [find me](search_key) the latest [commit](bitbucket_action)
- [get me](search_key) the [code](bitbucket_action).
- hey, [get me](search_key) the [code](bitbucket_action) on [test](repo_name)
- hey, [get me](search_key) the [code](bitbucket_action) on [test](repo_name) under [atlassian](owner_name).
- hey, [get me](search_key) the [code](bitbucket_action) on [repository](repo_key) [test](repo_name) [atlassian project]{"entity": "owner_name", "value": "atlassian"}.
- Jarvis, [get me](search_key) the [code](bitbucket_action) on [repository](repo_key) [test](repo_name) under [project atlassian](owner_name).
- Jarvis, [get me](search_key) the latest [commit](bitbucket_action) on branch [master](branch_name).
- [get me](search_key) the [code](bitbucket_action) from [master](branch_name) branch of [repository](bitbucket_key) [atlassian](repo_name)
- [get me](search_key) the code from [master](branch_name) branch of [atlassian](repo_name) [repository](repo_key)
- [get me]{"entity": "search_key", "value": " search_key"} the last [commit code](bitbucket_action) on [repo](repo_key) [atlassian](repo_name)
- who did the last [commit](bitbucket_action) on [sih](repo_name) [repo](repo_key) under project [atlassianwork](owner_name)?
- Jarvis, when was the last [commit](bitbucket_action) made on [repo art-2020]{"entity": "repo_name", "value": "art-2020"}
- Jarvis, on [repo](repo_key) [art-2020](repo_name), when was the last [commit]{"entity": "bitbucket_action", "value": " commit"} made
- hey jarvis, on [repository](repo_key) [robocon](repo_name) who made the last [commit](bitbucket_action)
- [find]{"entity": "search_key", "value": " search_key"} the latest update on [repo](repo_key) [arcWork](repo_name)
- [who](search_key) did the last [commit]{"entity": "bitbucket_action", "value": " commit"} on branch [master](branch_name)
- who did the last [commit]{"entity": "bitbucket_action", "value": " commit"} on [repo](repo_key) [art-2020](owner_name) owned by [art2020](repo_name)
- who did the last [commit]{"entity": "bitbucket_action", "value": " commit"} on [repo](repo_key) [art-2020](repo_name) owned by [art2020](owner_name)
- [fetch me](search_key) the last [commit]{"entity": "bitbucket_action", "value": " commit"} from user paresh on [repo](repo_key) [art-2020](owner_name) owned by [art2020](repo_name)

## intent:commit_by_user
- [find me](search_key) the last update from user [jamaluddin](user_name) on [repo](repo_key) [sectTest](repo_name)
- hey jarvis, get the latest [commit](bitbucket_action) done by user [tanmay](user_name)
- [find me](search_key) the last [update](bitbucket_action) from user [shritej](user_name) on [repo](repo_key)
- [find me]{"entity": "search_key", "value": " search_key"} the commit from user [tanmay](user_name)
- [get me]{"entity": "search_key", "value": " search_key"} the commit done by user [prathamesh](user_name)

## intent:branch_name_entry
- [master](branch_name) is the branch name
- the branch is [version](branch_name)
- [stable](branch_name) is the branch of type [bugfixes](branch_type)
- [master](branch_name)
- [version-2.x](branch_name) branch
- the branch name is [master](branch_name)

## intent:user_name_entry
- user name is [jamal](user_name)
- [rohit](user_name) is the user name i am looking for
- [Jamal](user_name)
- user is [tanmay](user_name)
- the user is [shritej](user_name)

## intent:branch_type_entry
- [release](branch_type) is the type of branch
- [bugfixes](branch_type)
- The branch is just a [other](branch_type) branch.
- It is just a [normal]{"entity": "branch_type", "value": "other"} branch
- the branch is of [feature](branch_type)
- [hotfix](branch_type)

## intent:info_of_all_spaces
- [fetch me](search_key) the information about all the spaces
- [retrieve](search_key) the details of all the spaces
- [get](search_key) the information of all the spaces
- Jarvis [fetch](search_key) all the spaces' details
- [get](search_key) info of all the spaces
- hey jarvis, [get me]{"entity": "search_key", "value": " search_key"} info about all the spaces
- [get all](search_key) the spaces from confluence

## intent:watcher_list
- hey Jarvis, [get me](search_key) the list of watchers on repo [workingonatlassianapis](repo_name)
- [who all](search_key) are the watchers on repo [test](repo_name)
- [get me](search_key) the watchers.
- list all the watchers.
- jarvis, [get me]{"entity": "search_key", "value": " search_key"} the list of developers on [repository](repo_key)
- [I want](search_key) to know [who all](search_key) are watchers on the [repository](repo_key) [atlassianWork](repo_name) under [art2020](owner_name)
- Good morning Jarvis, please [get me](search_key) the list of watchers on [test3](repo_name) repository
- [I want](search_key) to know [who all](search_key) are watchers on the [repository](repo_key) [atlassianWork](repo_name) under project [art2020](owner_name)
- [get me]{"entity": "search_key", "value": " search_key"} the list of watchers on [repo](repo_key) dev
- [get me]{"entity": "search_key", "value": " search_key"} the list of watchers on [repo](repo_key) [art-2020](repo_name)
- jarvis, list all the watchers on [repo](repo_key) [secTest](repo_name)
- [get me]{"entity": "search_key", "value": " search_key"} the list of watchers
- [get](search_key) the list of watchers on [repo](repo_key) [test](repo_name)
- [get me]{"entity": "search_key", "value": " search_key"} the list of watchers on [repo](repo_key) [test](repo_name) owned by [jkhan01](owner_name)
- [get me]{"entity": "search_key", "value": " search_key"} the list of watchers on [repo](repo_key) [art-2020](repo_name) owned by [art2020](owner_name)

## intent:repo_list
- hey Jarvis, [get me](search_key) the list of [repository](repo_key).
- [what are](search_key) the [repositories](repo_key) under [workspace jkhan01]{"entity": "owner_name", "value": "jkhan01"}?
- find all the [repos](repo_key) with [owner art2020]{"entity": "owner_name", "value": "art2020"}
- list all [repo](repo_key) owned by [tanmaygujar](owner_name)
- [get me]{"entity": "search_key", "value": " search_key"} the list of [repositories](repo_key)

## intent:branch_list
- [get me](search_key) the branches on [repo workingonatlassianapis]{"entity": "repo_name", "value": "workingonatlassianapis"}
- hey Jarvis, [find the](search_key) branches under [repository test]{"entity": "repo_name", "value": "test"}
- list all the branches.
- [find the](search_key) name of branches of type [release](branch_type).
- hey Jarvis, [get me](search_key) branches under [art-2020 repo]{"entity": "repo_name", "value": "art-2020"} owned by [jkhan01](owner_name)
- [get](search_key) the list of branches under [test repo]{"entity": "test", "value": "test"}

## intent:repo_name_entry
- the [repo](repo_key) is [test](repo_name)
- the [repository](repo_key) on target is [webApp](repo_name)
- [repo](repo_key) name is [mobileApp](repo_name)
- [webApp](repo_name) is the repo name
- i am talking about [secTest](repo_name)
- the name of the [repo](repo_key) is [sih2020](repo_name)
- the name of [repo](repo_key) is [sih2020](repo_name)
- [workingonatlassianapis](repo_name)
- the [repo](repo_key) is [art-2020](repo_name)

## intent:owner_name_entry
- the owner is [jkhan01](owner_name)
- [deftNinja](owner_name) is the owner
- the owner of the repo is [jhatya](owner_name)
- [jkhan01](owner_name)
- [art-202]{"entity": "owner_name", "value": "art2020"}0 is the owner

## intent:create_space
- [create](create_key) space named [Demo](space)
- new space for the name [sample](space)
- make a new space with the name [random](space)
- [create](create_key) a new space named [new space](space)
- [develop](create_key) a space whose name is [work](space)
- Jarvis could you [create](create_key) a space named [stuff](space) for me
- [create](create_key) a new space for me with the name [space](space)
- [create](create_key) a new space for us named [trial](space) and with key [something](key)
- [create](create_key) a new space for me with the name [space](space) and with key [random](key)
- [create](create_key) a new space named [Demo](space) having key [demo](key)
- [create](create_key) a new space
- [create](create_key) a new space named [Physics](space)
- [create](create_key) a new space named
- [create](create_key) a space named [Biology](space) with the key [biology](key)
- [create](create_key) a new space named [Title](space) with the key [title](key)
- [create](create_key) a new space named [Time](space)
- [create](create_key) a new space with the name [Barca](space) and with the key [barca](key)
- [develop](create_key) a new space with the name [Shritej](space) and with key as [shritej](key)
- jarvis could you make a novel space with the name [Boat](space) and having a key set as [boat](key)
- construct a novel space with the name [Music](space) which has the key as [bro](key)
- make a pristine space having a name [Shit](space) and whose key is [broshit](key)
- jarvis u have to [create](create_key) a space which has a name [Clubs](space) and a key which is [clubs](key)
- make a new space having a name and a key as [Stocks](space) and [stock](key) respectively
- [develop](create_key) or [create](create_key) a new space which is named as [Market](space) and having a key [market-value](key)
- [create](create_key) a new space titled [Nevermind](space) and the key of this space is [whatever](key)
- [create](create_key) a brand new space having a name [Whatever](space) and the key is [dont-care](key)
- [create](create_key) a new space having a name [FuckOff](space) and having a key which is [you](key)
- [create](create_key) a space with name [plagiarisms](space)
- [create]{"entity": "create_key", "value": " create_key"} space with name [Demo3](space)

## intent:space_name_entry
- space name is [Demo](space)
- named [Demo](space)
- titled [Random](space)
- the name of the space is [Sample](space)
- with the name [Demo](space)
- [Demo](space)
- [Sample](space)
- the name of the space is [Chemistry](space)
- the name of the space is [Dynamic](space)
- [Time](space)

## intent:space_key_entry
- space key is [Timepass](key)
- key is [random](key)
- the key of the space is [Random](key)
- the space has key [Sample](key)
- with the key [stuff](key)
- give [Demo](key) as the key of the space
- [sample](key)
- [demo](key)
- [phy](key)
- [chemistry](key)
- the key is [dynamic](key)

## intent:info_of_a_space
- [fetch me](search_key) the information about the space with the key [physics](key)
- [retrieve](search_key) the details of the space having the key [bio](key)
- [get the](search_key) information of the space whose key is [sample](key)
- Jarvis [fetch](search_key) the space's details whose key is [math](key)
- [get](search_key) info of the space which has the key [mechanics](key)
- I want all the info about the space whose key is [brocode](key)
- [get](search_key) me all the information you have about the space with the key [trial](key)
- [fetch the](search_key) entire details about the space having the key [shit](key)
- Jarvis I want all the details about the space whose key is [timepass](key)
- [get me]{"entity": "search_key", "value": " search_key"} the info about space with key [timepass](key)

## intent:get_pages_in_a_space
- [get all](search_key) the pages in the space [name](space)
- [fetch all](search_key) the names of all the pages present in the space named [Biology](space)
- Jarvis [get all](search_key) the pages existing in the space having the name [Physics](space)
- [retrieve](search_key) all the pages present in the space [Math](space)
- I want all the pages that are currently existing in the space which has the name [BroCode](space)
- Jarvis I want all the names of the pages that you can fetch that are present in the space [KyaBaat](space)
- [display](search_key) all the pages that are present in the space whose name is [Bro](space)
- Hey, jarvis [bring me](search_key) all the pages which have space name as [setup](space)

## intent:error_search
- hey Jarvis, [find me](search_key) the [solution to the error](error_keys)
- [Help me](search_key) out with the [error](error_keys)
- [what is](search_key) the best answer to the [problem of value error](error_keys)?
- Stackoverflow
- hey, [solve](error_keys) the error for me.
- stackoverflow
- [find me]{"entity": "search_key", "value": " search_key"} the optimal [solution to](error_keys) the [error]{"entity": "error_keys", "value": " error"}
- [find]{"entity": "search_key", "value": " search_key"} the [solution to](error_keys) [the class not found error](error_query)
- Fetch [me](search_key) the best [solution to](error_keys) the [invalid input for json error](error_query)
- yes, [i want](search_key) [solution](error_keys)
- hey, [get me]{"entity": "search_key", "value": " search_key"} the [best answer](error_keys) to the [error](error_keys)
- hey jarvis, help [me](search_key) with the solution
- fetch [me](search_key) the solution

## intent:error_query_entry
- [the class not found error](error_query)
- the error is [value not found]{"entity": "error_query", "value": "value not found error"}
- It reads [invalid token error](error_query)
- [floating point error](error_query)
- [no module name flask found](error_query)

## intent:create_page
- [create](create_key) a new page with title [Sample](title) in the space [Chemistry](space) with the body ["Bro!! this is nothing new"](body)
- [create](create_key) page named [Demo](title)
- new page for the title [Kya](title)
- [make](create_key) a new page with the name [random](title)
- [create](create_key) a new page titled [new page](title)
- [develop](create_key) a page whose name is [work](title)
- Jarvis could you [create](create_key) a page named [Stuff](title) for me
- [create](create_key) a new page for me with the title [Page](title)
- Jarvis I want you to [create](create_key) a new page with the title [Bruh](title) in the space [Math](space)
- [generate](create_key) a page titled [Title](title) with body as ["This is messed up"](body) in the space [BroCode](space)
- build a novel page in the space [Biology](space) with title as [Reproductive System](title) and having a body ["This is how we reproduce, and multiply as well."](body)
- [fabricate](create_key) a page named [Boi](title) in the space [BroCode](space) with a body ["This is swag"](body)
- Jarvis make a new page in the space [Physics](space) under the title [Light](title) and a body ["Light travels in a straight line."](body)
- Jarvis make a new page in the space [Physics](space) under the title [Magnetism](title)
- [make](create_key) a pristine page having a title [Shit](title) having body as ["Bro this is pretty messed up. Sort it out."](body) in the space [Bruh](space)
- make a new page [New](title) comprising a body which is ["This is pretty novel, let's improve it."](body)
- I just want you to give me a new page named [Bruhhh](title) and create it in the space named [Swag](space)
- [create](create_key) new page [Page](title) with body ["this is a new page  bruh."](body) and do this in the space with the name [KyaBaat](space)

## intent:title_entry
- the title of the page is [Title](title)
- [Kya Baat Hai](title)
- the page is titled [Bruh this is enough](title)
- [This is the Title](title)
- The title shall be [Enough](title)
- [Bro Swag](title) shall be the title
- The page should have title[Deployment and Testing of chatbot](title)
- the page has the title [Socket communications on chatbot](title)
- the page to be created should have the title [Integration of the Domains](title)

## intent:body_entry
- the body for the page to be created is ["This is the beeping body."](body)
- ["Kya baat hai bantai, aise hi chalte raho"](body)
- ["This page entails all the details about the stock prices of various companies."](body)
- ["What a strike by Lionel Messi!! Just Brilliant"](body)
- The body is ["A water molecule has two atoms of hydrogen and one atom of oxygen."](body)
- ["And here is Messi, away from two, three, four, wonderful, wonderful, wonderful. How good is he? A near supernatural goal from Lionel Messi"](body)
- ["This is really really very boring mah boi"](body) is the body of the page to be created
- ["enough brother, that's enough!!"](body) is the body of the page that is going to be created

## intent:delete_page
- delete the page
- remove the page
- eliminate the page
- destroy the page
- delte the page with id [2345167](page_id)
- remove the page having page id [2315867](page_id)
- jarvis find and remove the page whose id is [2348798](page_id)
- Jarvis could you delete the page having the id [4254867](page_id)

## intent:page_id_entry
- the id of the page is [3525426](page_id)
- id is [3252359](page_id)
- [7985722](page_id)
- [0375025](page_id)
- [9877321](page_id)
- [3642302](page_id)
- the page id is [3759290](page_id)
- [0240522](page_id)

## intent:get_page_info_by_id
- get the details of the page which has id [3984322](page_id)
- fetch the complete information about the page with id [9923569](page_id)
- I want the details of the page whose id is [5767184](page_id)
- retrieve the details about the page with page id [5982355](page_id)
- the page with page id [9923569](page_id) fetch all that pages details
- get the entire info of the page whose page id is [5767184](page_id)
- Jarvis get the info about the page having id [9836421](page_id)
- Jarvis I want you to fetch the complete details you have about the page having id [3587232](page_id)
- get the page info having id [5767184](page_id)
- get the info of the page having id [5767184](page_id)

## intent:export_page_as_pdf
- export the page having id [3984322](page_id) as a pdf file named [no_idea](file_name)
- the page whose id is [5767184](page_id) is to be exported as a pdf file with the name [bruh](file_name)
- Jarvis export a page with id [9836421](page_id) as a pdf file whose name is [sample](file_name)
- I want a page to be exported as pdf
- export a page as pdf
- Jarvis could you export a page as pdf
- Jarvis I want you to export the page with page id [9923569](page_id) as a pdf file named [physics](file_name)
- the page with id [3984322](page_id) is to be exported as a pdf file
- the page with id [3984322](page_id) is to be exported as a pdf file titled [bro](file_name)

## intent:file_name_entry
- the name of the pdf file is [tester](file_name)
- [physics](file_name)
- pdf file must be named [mechanics](file_name)
- [biology](file_name) is the name of the pdf file to be created
- [Physics](file_name)
- [Math](file_name) is the title of the pdf file
- the pdf file's name is [physics](file_name)
- [Chemistry](file_name)


## intent:issue_type_entry
- [epic]{"entity": "issue_type", "value": "Epic"}
- create [story]{"entity": "issue_type", "value": "Story"}
- I want [task]{"entity": "issue_type", "value": "Task"}
- [subtask]{"entity": "issue_type", "value": "Subtask"}
- [bug]{"entity": "issue_type", "value": "Bug"}


## intent:epic_summary_entry
- [epic]{"entity": "issue_type", "value": "Epic"} summary is [text summarization](epic_summary)
- the [epic]{"entity": "issue_type", "value": "Epic"} summary is [browse](epic_summary)
- [corporate voice assistant](issue_summary) is summary for [epic]{"entity": "issue_type", "value": "Epic"}
- [epic]{"entity": "issue_type", "value": "Epic"} summary is [skill extraction from resume](epic_summary)
- summary is [text extraction](epic_summary)

## intent:task_summary_entry
- [task]{"entity": "issue_type", "value": "Task"} summary is [create registration page](task_summary)
- [task]{"entity": "issue_type", "value": "Task"} summary is [develop add and remove from cart feature](task_summary)
- [task]{"entity": "issue_type", "value": "Task"} is [support tool](task_summary)
- [corporate voice assistant](task_summary) is summary for [task]{"entity": "issue_type", "value": "Task"}

## intent:issue_summary_entry
- [story]{"entity": "issue_type", "value": "Story"} summary is [text summarization](issue_summary)
- the [bug]{"entity": "issue_type", "value": "Bug"} summary is [browse](issue_summary)
- the [story]{"entity": "issue_type", "value": "Story"} name is [order operation](issue_summary)
- [subtask]{"entity": "issue_type", "value": "Subtask"} summary is [payment operation](issue_summary)
- summary of [subtask]{"entity": "issue_type", "value": "Subtask"} [track](issue_summary)
- the [story]{"entity": "issue_type", "value": "Story"} summary is [text extraction](issue_summary)
- [story]{"entity": "issue_type", "value": "Story"} summary is [make login page](issue_summary)
- [bug]{"entity": "issue_type", "value": "Bug"} summary is [cash payment function](issue_summary)
- summary of [bug]{"entity": "issue_type", "value": "Bug"} is [debit/credit card payment feature](issue_summary)
- summary of [story]{"entity": "issue_type", "value": "Story"} is [ETA support](issue_summary)
- [subtask]{"entity": "issue_type", "value": "Subtask"} is [duplicate previous order](issue_summary)
- [subtask]{"entity": "issue_type", "value": "Subtask"} is [database formation](issue_summary)
- [wrong credentials](issue_summary) bug
- for [bug]{"entity": "issue_type", "value": "Bug"} set summary as [text summarization using nlp](issue_summary)
- [payment functionality for flipkart](issue_summary) is summary of [bug]{"entity": "issue_type", "value": "Bug"}
- [create](create) [story]{"entity": "issue_type", "value": "Story"} with summary [feature extraction](issue_summary)
- [login error](issue_summary)


## intent:project_entry
- [project Resume Screening](project_name)
- project is [project automated surveying](project_name)
- The name of the project is [corporate jarvis](project_name)
- project is [Resume screening](project_name)
- [Online shopping system](project_name) project
- [voice assistant](project_name) is project name
- project name is [Resume screening](project_name)
- project name is [resume screening](project_name)
- [resume screening](project_name)
- [resume screening](project_name) is project name


## intent:get_all_project_name
- [hey jarvis](greet) [fetch](search_keys) all projects
- [hi](greet) [fetch](search_keys) all projects
- [hello](greet) can you [get](search_keys) project names
- [hey](greet) [what](search_keys) are the projects
- [list](search_keys) project names
- [fetch](search_keys) all projects


## intent:group_name_entry
- group name is [designers](group_name)
- group is [administrators](group_name)
- name is [creative](group_name)
- [manager](group_name) group



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
- [get](search_keys) [story]{"entity": "issue_type", "value": "Story"} [text summarization](issue_summary) details
- [fetch](search_keys) [browse](issue_summary) [story]{"entity": "issue_type", "value": "Story"}
- [find](search_keys) [story]{"entity": "issue_type", "value": "Story"} [system error](issue_summary) details
- [get](search_keys) [bug]{"entity": "issue_type", "value": "Bug"} [text summarization](issue_summary) details
- [fetch](search_keys) [browse](issue_summary) [bug]{"entity": "issue_type", "value": "Bug"}
- [find](search_keys) [bug]{"entity": "issue_type", "value": "Bug"} [system error](issue_summary) details
- [get](search_keys) [subtask]{"entity": "issue_type", "value": "Subtask"} [text summarization](issue_summary) details
- [fetch](search_keys) [browse](issue_summary) [subtask]{"entity": "issue_type", "value": "Subtask"}
- [find](search_keys) [subtask]{"entity": "issue_type", "value": "Subtask"} [system error](issue_summary) details
- [fetch](search_keys) [text extraction](issue_summary) [story]{"entity": "issue_type", "value": "Story"}

## intent:get_epic
- [get](search_keys) [epic]{"entity": "issue_type", "value": "Epic"} [text summarization](epic_summary) details
- [fetch](search_keys) [browse](epic_summary) [epic]{"entity": "issue_type", "value": "Epic"}
- [find](search_keys) [epic]{"entity": "issue_type", "value": "Epic"} [system error](epic_summary) details

## intent:get_task
- [get](search_keys) [task]{"entity": "issue_type", "value": "Task"} [text summarization](task_summary) details
- [fetch](search_keys) [browse](task_summary) [task]{"entity": "issue_type", "value": "Task"}
- [find](search_keys) [task]{"entity": "issue_type", "value": "Task"} [system error](task_summary) details
- [get](search_keys) [task]{"entity": "issue_type", "value": "Task"} [browse](task_summary)
- [fetch](search_keys) [task]{"entity": "issue_type", "value": "Task"} [browse](task_summary)

## intent:get_status_of_issue
- [get](search_keys) status of [story]{"entity": "issue_type", "value": "Story"} [text summarization](issue_summary)
- [what](search_keys) is status of [browse](issue_summary) [story]{"entity": "issue_type", "value": "Story"}
- [find](search_keys) status for [story]{"entity": "issue_type", "value": "Story"} [system error](issue_summary)
- [fetch](search_keys) status of [system error](issue_summary) [story]{"entity": "issue_type", "value": "Story"}
- [get](search_keys) status of [bug]{"entity": "issue_type", "value": "Bug"} [text summarization](issue_summary)
- [what](search_keys) is status of [browse](issue_summary) [bug]{"entity": "issue_type", "value": "Bug"}
- [find](search_keys) status for [bug]{"entity": "issue_type", "value": "Bug"} [system error](issue_summary)
- [fetch](search_keys) status of [system error](issue_summary) [bug]{"entity": "issue_type", "value": "Bug"}
- [get](search_keys) status of [subtask]{"entity": "issue_type", "value": "Subtask"} [text summarization](issue_summary)
- [what](search_keys) is status of [browse](issue_summary) [subtask]{"entity": "issue_type", "value": "Subtask"}
- [find](search_keys) status for [subtask]{"entity": "issue_type", "value": "Subtask"} [system error](issue_summary)
- [fetch](search_keys) status of [system error](issue_summary) [subtask]{"entity": "issue_type", "value": "Subtask"}
- [get](search_keys) status of [story]{"entity": "issue_type", "value": "Story"} [text extraction](issue_summary)

## intent:get_status_of_task
- [get](search_keys) status [task]{"entity": "issue_type", "value": "Task"} [text summarization](task_summary)
- [what](search_keys) is status of [browse](task_summary) [task]{"entity": "issue_type", "value": "Task"}
- [find](search_keys) status for [task]{"entity": "issue_type", "value": "Task"} [system error](task_summary)
- [fetch](search_keys) status of [system error](task_summary) [task]{"entity": "issue_type", "value": "Task"}
- [fetch](search_keys) status of [task]{"entity": "issue_type", "value": "Task"} [browse](task_summary)

## intent:get_status_of_epic
- [get](search_keys) status of [epic]{"entity": "issue_type", "value": "Epic"} [text summarization](epic_summary)
- [what](search_keys) is status of [browse](epic_summary) [epic]{"entity": "issue_type", "value": "Epic"}
- [find](search_keys) status for [epic]{"entity": "issue_type", "value": "Epic"} [system error](epic_summary)
- [fetch](search_keys) status of [system error](epic_summary) [epic]{"entity": "issue_type", "value": "Epic"}
- [fetch](search_keys) status of [epic]{"entity": "issue_type", "value": "Epic"} [browse](epic_summary)

## intent:get_issue_version
- [get](search_keys) version of [story]{"entity": "issue_type", "value": "Story"} [text summarization](issue_summary)
- [what](search_keys) is release of [browse](issue_summary) [story]{"entity": "issue_type", "value": "Story"}
- [find](search_keys) release date of [system error](issue_summary) [story]{"entity": "issue_type", "value": "Story"}
- [fetch](search_keys) version details of [system error](issue_summary) [story]{"entity": "issue_type", "value": "Story"}
- [get](search_keys) version of [bug]{"entity": "issue_type", "value": "Bug"} [text summarization](issue_summary)
- [what](search_keys) is release of [browse](issue_summary) [bug]{"entity": "issue_type", "value": "Bug"}
- [find](search_keys) release date of [system error](issue_summary) [bug]{"entity": "issue_type", "value": "Bug"}
- [fetch](search_keys) version details of [system error](issue_summary) [bug]{"entity": "issue_type", "value": "Bug"}
- [get](search_keys) version of [subtask]{"entity": "issue_type", "value": "Subtask"} [text summarization](issue_summary)
- [what](search_keys) is release of [browse](issue_summary) [subtask]{"entity": "issue_type", "value": "Subtask"}
- [find](search_keys) release date of [subtask]{"entity": "issue_type", "value": "Subtask"} [system error](issue_summary)
- [fetch](search_keys) version details of [system error](issue_summary) [subtask]{"entity": "issue_type", "value": "Subtask"}

## intent:get_task_version
- [get](search_keys) version of [task]{"entity": "issue_type", "value": "Task"} [text summarization](task_summary)
- [what](search_keys) is release of [browse](task_summary) [task]{"entity": "issue_type", "value": "Task"}
- [find](search_keys) release date of [system error](task_summary) [task]{"entity": "issue_type", "value": "Task"}
- [fetch](search_keys) version details of [system error](task_summary) [task]{"entity": "issue_type", "value": "Task"}

## intent:get_epic_version
- [get](search_keys) version of [epic]{"entity": "issue_type", "value": "Epic"} [text summarization](epic_summary)
- [what](search_keys) is release of [browse](epic_summary) [epic]{"entity": "issue_type", "value": "Epic"}
- [find](search_keys) release date of [system error](epic_summary) [epic]{"entity": "issue_type", "value": "Epic"}
- [fetch](search_keys) version details of [system error](epic_summary) [epic]{"entity": "issue_type", "value": "Epic"}



## intent:get_comments_in_issue​
- [hi](greet) [get](search_keys) all comments on [story]{"entity": "issue_type", "value": "Story"} [system error](issue_summary)
- [fetch](search_keys) me all comment on [browse](issue_summary) [story]{"entity": "issue_type", "value": "Story"}
- [find](search_keys) all comment for [story]{"entity": "issue_type", "value": "Story"} [text summarization](issue_summary)
- [hi](greet) [get](search_keys) all comments on [bug]{"entity": "issue_type", "value": "Bug"} [system error](issue_summary)
- [fetch](search_keys) me all comment on [browse](issue_summary) [bug]{"entity": "issue_type", "value": "Bug"}
- [find](search_keys) all comment from [bug]{"entity": "issue_type", "value": "Bug"} [text summarization](issue_summary)
- [hi](greet) [get](search_keys) all comments on [subtask]{"entity": "issue_type", "value": "Subtask"} [system error](issue_summary)
- [fetch](search_keys) me all comment on [browse](issue_summary) [subtask]{"entity": "issue_type", "value": "Subtask"}
- [find](search_keys) all comment for [subtask]{"entity": "issue_type", "value": "Subtask"} [text summarization](issue_summary)

## intent:get_comments_in_task
- [hi](greet) [get](search_keys) all comments on [task]{"entity": "issue_type", "value": "Task"} [system error](task_summary)
- [fetch](search_keys) me all comment on [browse](task_summary) [task]{"entity": "issue_type", "value": "Task"}
- [find](search_keys) all comment for [task]{"entity": "issue_type", "value": "Task"} [text summarization](task_summary)

## intent:get_comments_in_epic
- [hi](greet) [get](search_keys) all comments on [epic]{"entity": "issue_type", "value": "Epic"} [system error](epic_summary)
- [fetch](search_keys) me all comment on [browse](epic_summary) [epic]{"entity": "issue_type", "value": "Epic"}
- [find](search_keys) all comment for [epic]{"entity": "issue_type", "value": "Epic"} [text summarization](epic_summary)



## intent:get_worklog_in_issue
- [hi](greet) [get](search_keys) all worklogs from [story]{"entity": "issue_type", "value": "Story"} [system error](issue_summary)
- [fetch](search_keys) worklogs in [browse](issue_summary) [story]{"entity": "issue_type", "value": "Story"}
- [find](search_keys) all worklogs from [text summarization](issue_summary) [story]{"entity": "issue_type", "value": "Story"}
- from [story]{"entity": "issue_type", "value": "Story"} [text summarization](issue_summary) [get](search_keys) all worklog
- [hi](greet) [get](search_keys) all worklogs from [bug]{"entity": "issue_type", "value": "Bug"} [system error](issue_summary)
- [fetch](search_keys) worklogs in [bug]{"entity": "issue_type", "value": "Bug"} [browse](issue_summary)
- [find](search_keys) all worklogs from [text summarization](issue_summary
- from [bug]{"entity": "issue_type", "value": "Bug"} [text summarization](issue_summary) [get](search_keys) all worklog
- [hi](greet) [get](search_keys) all worklogs from [subtask]{"entity": "issue_type", "value": "Subtask"} [system error](issue_summary)
- [fetch](search_keys) worklogs in [subtask]{"entity": "issue_type", "value": "Subtask"} [browse](issue_summary)
- [find](search_keys) all worklogs from [text summarization](issue_summary) [subtask]{"entity": "issue_type", "value": "Subtask"}
- from [subtask]{"entity": "issue_type", "value": "Subtask"} [text summarization](issue_summary) [get](search_keys) all worklog

## intent:get_worklog_in_task
- [hi](greet) [get](search_keys) all worklogs from [system error](task_summary) [task]{"entity": "issue_type", "value": "Task"}
- [fetch](search_keys) worklogs in [task]{"entity": "issue_type", "value": "Task"} [browse](task_summary)
- [find](search_keys) all worklogs from [task]{"entity": "issue_type", "value": "Task"} [text summarization](task_summary)
- from [task]{"entity": "issue_type", "value": "Task"} [text summarization](task_summary) [get](search_keys) all worklog

## intent:get_worklog_in_epic
- [hi](greet) [get](search_keys) all worklogs from [system error](epic_summary) [epic]{"entity": "issue_type", "value": "Epic"}
- [fetch](search_keys) worklogs in [epic]{"entity": "issue_type", "value": "Epic"} [browse](epic_summary)
- [find](search_keys) all worklogs from [epic]{"entity": "issue_type", "value": "Epic"} [text summarization](epic_summary)
- from [text summarization](epic_summary) [epic]{"entity": "issue_type", "value": "Epic"} [get](search_keys) all worklog

## intent:visible_to_role_entry
- visible to [administrators](visible_to_role)
- [developers](visible_to_role) can see
- visible to all [managers](visible_to_role)

## intent:get_latest_email_in_inbox
- get the latest mail present in the inbox
- retrieve the last mail i have received
- fetch the latest mail that was sent to me
- fetch the most recent email that i have received
- i want you to get the latest email present from the inbox
- jarvis i would appreciate if you could fetch the latest email present in the inbox
- jarvis fetch me the last email i have received

## intent:get_latest_email_from_user
- get the latest mail from a specific user
- get the latest email sent by a specific user
- retrieve the last mail i have received from the user which i will mention
- fetch the latest mail that was sent to me by a specific person
- fetch the most recent email that i have received from the person that i am going to specify
- i want you to get the latest email present from the inbox that was sent to me by the specific user
- jarvis i would appreciate if you could fetch the latest email present in the inbox which was sent to me by a specific user
- jarvis fetch me the last email i have received from the user that i am gonna specify
- get the latest email from a specific user
- get the latest mail from the specific user

## intent:option_entry
- 1
- 3
- 6
- 5
- 2
- 4

## intent:get_latest_email_from_label
- get the latest mail from a specific label
- get the latest email sent by a specific label
- retrieve the last mail i have received from the label which i will mention
- fetch the latest mail that was sent to me with a specific label
- fetch the most recent email that i have received with the label that i am going to specify
- i want you to get the latest email present from the inbox that was sent to me with the specific label
- jarvis i would appreciate if you could fetch the latest email present in the inbox which was sent to me with a specific label
- jarvis fetch me the last email i have received with the label that i am gonna specify
- get the latest email with a specific label
- get the latest email with the specified label

## intent:query_entry
- the query is [from: sample@gmail.com](query)
- [from: abc@gmail.com](query)
- query is [from: efg@gmail.com](query)
- [from: ab234@gmail.com](query)
- [from: random123@gmail.com](query)
- [Testing](query)
- [Random](query)
- [Anything else](query)
- the query is [Something else](query)
- [It can be anything else](query)
- [from: patilshritej112@gmail.com](query)
- [Sports : Football](query)
- [from: patilshritej112@gmail.com](query)

## intent:send_email
- send a mail
- send an email
- send an email for me
- send an email on my behalf
- jarvis could you send an email for me
- i would like to send an email
- create a new mail and send it for me
- jarvis send an email for me

## intent:email_body_entry
- [this is the body of the mail](email_body)
- [This is random stuff.](email_body)
- [Anything can be present here.](email_body)
- [This is a rasa tutorial.](email_body)
- [This project name is Corporate JARVIS.](email_body)

## intent:receiver_entry
- [abc@gmail.com](receiver)
- [random@gmail.com](receiver)
- [efg@gmail.com](receiver)
- [abc123@gmail.com](receiver)
- [receiver@gmail.com](receiver)

## intent:subject_entry
- [Subject](subject)
- the subject is [Random stuff](subject)
- [Anything can be here](subject)
- [Something else](subject)
- [This is the subject](subject)
- [Unique](subject)
- [Google forms](subject)

## intent:send_email_with_attachments
- send a mail with attachments
- send an email with attachments
- send an email for me with attachments
- send an email with attachments on my behalf
- jarvis could you send an email with an attachment for me
- i would like to send an email with attachments
- create a new mail with an attachment and send it for me
- jarvis send an email with attachments for me


## intent:file_dir_entry
- the directory of the file is [./Attachments](file_dir)
- dir is [./Dir](file_dir)
- [./Dir1/Dir2/dir3](file_dir)
- [./Rand](file_dir)
- [./Back/front](file_dir)
- [./front/Back](file_dir)
- [./Attachments](file_dir)

## intent:filename_entry
- the file name is [abc.pdf](filename)
- file named [random.jpg](filename)
- [abc.docx](filename)
- [anything.pdf](filename)
- [something.png](filename)
- [this.pdf](filename)
- [ghi.docx](filename)




## synonym:Bug
- bug

## synonym:Epic
- epic

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





## synonym: commit
- commit
- code

## synonym: create_key
- create
- construct
- assemble
- develop
- make
- generate

## synonym: error
- error

## synonym: repo
- repository

## synonym: search_key
- get me
- find
- find me
- search
- fetch
- bring
- can you get me

## synonym:art-2020
- repo art-2020
- art-2020 repo
- owner art-2020

## synonym:art2020
- owner art2020

## synonym:atlassian
- atlassian project

## synonym:jkhan01
- workspace jkhan01

## synonym:other
- normal

## synonym:payment operation
- message payment operation

## synonym:test
- repository test
- test repo

## synonym:text summarization
- "text summarization"

## synonym:value not found error
- value not found

## synonym:workingonatlassianapis
- repo workingonatlassianapis
- workingonatlassianapis
