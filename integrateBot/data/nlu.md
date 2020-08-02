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
