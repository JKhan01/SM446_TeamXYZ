<!-- Space related stories -->

## info of all spaces
* greet
  - utter_greet
* info_of_all_spaces
  - action_info_of_all_spaces  
* goodbye
  - utter_goodbye


## info of a space
* greet
  - utter_greet
* info_of_a_space
  - action_space_info
  - utter_space_info_slot_value
  - utter_submit 
* goodbye
  - utter_goodbye


## create space
* greet
  - utter_greet
* create_space
  - create_space_form
  - form{"name" : "create_space_form"}
  - form{"name" : null}
  - utter_create_space_slot_values
  - utter_submit
* goodbye
  - utter_goodbye


## get pages in a space
* greet
  -utter_greet
* get_pages_in_a_space
  - action_get_pages_in_a_space
  - utter_pages_in_a_space_slot_value
  - utter_submit  
* goodbye
  - utter_goodbye



<!-- Page related stories -->

## create page
* greet
  - utter_greet
* create_page
  - create_page_form
  - form{"name": "create_page_form"}
  - form{"name": null}
  - utter_create_page_slot_values
  - utter_submit
* goodbye
  - utter_goodbye  

## delete page
* greet
  - utter_greet
* delete_page
  - action_delete_page
  - utter_submit
* goodbye
  - utter_goodbye

## delete page 2
* greet
  - utter_greet
* delete_page
  - utter_ask_page_id
  - action_delete_page
* goodbye
  - utter_goodbye


## check page exists
* greet
  - utter_greet
* check_page_exists
  - check_page_exists_form
  - form{"name": "check_page_exists_form"}
  - form{"name": null}
  - utter_check_page_exists_slot_values
  - utter_submit
* goodbye
  - utter_goodbye      


## get page id
* greet
  - utter_greet
* get_page_id
  - get_page_id_form
  - form{"name": "get_page_id_form"}
  - form{"name": null} 
  - utter_get_page_id_slot_values
  - utter_submit
* goodbye
  - utter_goodbye   


## get page space 
* greet
  - utter_greet
* get_page_space
  - action_get_page_space
  - utter_submit
* goodbye
  - utter_goodbye

## get page space 2
* greet
  - utter_greet
* get_page_space
  - utter_ask_page_id
  - action_get_page_space
  - utter_submit
* goodbye
  - utter_goodbye

# get page info by id
* greet
  - utter_greet
* get_page_info_by_id
  - action_get_page_info_by_id
  - utter_submit  
* goodbye
  - utter_goodbye

# get page info by id 2
* greet
  - utter_greet
* get_page_info_by_id
  - utter_ask_page_id
  - action_get_page_info_by_id
  - utter_submit  
* goodbye
  - utter_goodbye  


# get page info by title
* greet
  - utter_greet
* get_page_info_by_title
  - get_page_info_by_title_form
  - form{"name": "get_page_info_by_title_form"}  
  - form{"name": null}
  - utter_get_page_info_by_title_slot_values
  - utter_submit
*goodbye
  - utter_goodbye  

# export page as pdf 
* greet
  - utter_greet
* export_page_as_pdf
  - export_page_as_pdf_form
  - form{"name": "export_page_as_pdf_form"}
  - form{"name": null}
  - utter_export_page_as_pdf_slot_values
  - utter_submit  
* goodbye
  - utter_goodbye



## interactive_story_1
* greet
    - utter_greet
* create_space
    - create_space_form
    - form{"name": "create_space_form"}
    - slot{"requested_slot": "space"}
* form: greet

## interactive_story_2
* greet
    - utter_greet
* create_space{"space": "Physics"}
    - slot{"space": "Physics"}
    - create_space_form
    - form{"name": "create_space_form"}
    - slot{"space": "Physics"}
    - slot{"space": "Physics"}
    - slot{"requested_slot": "key"}
* form: space_key_entry{"key": "phy"}
    - slot{"key": "phy"}
    - form: create_space_form
    - slot{"key": "phy"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_create_space_slot_values
    - utter_submit

## interactive_story_1
* greet
    - utter_greet
* create_space
    - create_space_form
    - form{"name": "create_space_form"}
    - slot{"requested_slot": "space"}
* form: space_name_entry{"space": "Chemistry"}
    - slot{"space": "Chemistry"}
    - form: create_space_form
    - slot{"space": "Chemistry"}
    - slot{"requested_slot": "key"}
* form: space_key_entry{"key": "chemistry"}
    - slot{"key": "chemistry"}
    - form: create_space_form
    - slot{"key": "chemistry"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_create_space_slot_values
    - utter_submit

## interactive_story_1
* greet
    - utter_greet
* create_space{"space": "Biology", "key": "biology"}
    - slot{"key": "biology"}
    - slot{"space": "Biology"}
    - create_space_form
    - form{"name": "create_space_form"}
    - slot{"space": "Biology"}
    - slot{"key": "biology"}
    - slot{"space": "Biology"}
    - slot{"key": "biology"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_create_space_slot_values
    - utter_submit

## interactive_story_1
* greet
    - utter_greet
* create_space
    - create_space_form
    - form{"name": "create_space_form"}
    - slot{"requested_slot": "space"}
* form: space_name_entry{"space": "Dynamic"}
    - slot{"space": "Dynamic"}
    - form: create_space_form
    - slot{"space": "Dynamic"}
    - slot{"requested_slot": "key"}
* form: space_key_entry{"key": "dynamic"}
    - slot{"key": "dynamic"}
    - form: create_space_form
    - slot{"key": "dynamic"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_create_space_slot_values
    - utter_submit

## interactive_story_1
* greet
    - utter_greet
* create_space{"space": "Title", "key": "title"}
    - slot{"key": "title"}
    - slot{"space": "Title"}
    - create_space_form
    - form{"name": "create_space_form"}
    - slot{"space": "Title"}
    - slot{"key": "title"}
    - slot{"space": "Title"}
    - slot{"key": "title"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_create_space_slot_values
    - utter_submit

## interactive_story_1
* greet
    - utter_greet
* create_space{"space": "Time"}
    - slot{"space": "Time"}
    - create_space_form
    - form{"name": "create_space_form"}
    - slot{"space": "Time"}
    - slot{"space": "Time"}
    - slot{"requested_slot": "key"}
* form: space_name_entry{"key": "time"}
    - slot{"key": "time"}
    - form: create_space_form
    - slot{"key": "time"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_create_space_slot_values
    - utter_submit

## interactive_story_1
* greet
    - utter_greet
* create_space{"space": "Barca", "key": "barca"}
    - slot{"key": "barca"}
    - slot{"space": "Barca"}
    - create_space_form
    - form{"name": "create_space_form"}
    - slot{"space": "Barca"}
    - slot{"key": "barca"}
    - slot{"space": "Barca"}
    - slot{"key": "barca"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_create_space_slot_values
    - utter_submit
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* create_space{"space": "Shritej", "key": "shritej"}
    - slot{"key": "shritej"}
    - slot{"space": "Shritej"}
    - create_space_form
    - form{"name": "create_space_form"}
    - slot{"space": "Shritej"}
    - slot{"key": "shritej"}
    - slot{"space": "Shritej"}
    - slot{"key": "shritej"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_create_space_slot_values
    - utter_submit
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* create_space{"space": "Boat", "key": "boat"}
    - slot{"key": "boat"}
    - slot{"space": "Boat"}
    - create_space_form
    - form{"name": "create_space_form"}
    - slot{"space": "Boat"}
    - slot{"key": "boat"}
    - slot{"space": "Boat"}
    - slot{"key": "boat"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_create_space_slot_values
    - utter_submit
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* create_space{"space": "FuckOff", "key": "you"}
    - slot{"key": "you"}
    - slot{"space": "FuckOff"}
    - create_space_form
    - form{"name": "create_space_form"}
    - slot{"space": "FuckOff"}
    - slot{"key": "you"}
    - slot{"space": "FuckOff"}
    - slot{"key": "you"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_create_space_slot_values
    - utter_submit
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* get_page_space{"page_id": "5767184"}
    - slot{"page_id": "5767184"}
    - action_get_page_space
    - utter_submit
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* get_page_info_by_id{"page_id": "5767184"}
    - slot{"page_id": "5767184"}
    - action_get_page_info_by_id
    - utter_submit
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* get_page_info_by_id{"page_id": "5767184"}
    - slot{"page_id": "5767184"}
    - action_get_page_info_by_id
    - utter_submit
* goodbye
    - utter_goodbye
