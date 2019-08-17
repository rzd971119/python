from train_data import interprete
INIT=0
CHOOSE_CURRENCY=1
SEARCH=2
policy={
        (INIT,"currency_search"):(CHOOSE_CURRENCY,"what's the currency you want to search"), #ask the currency's kind
        (INIT,"help"):(INIT,"I can search for the information about currency rate on the base of USD"), #help the user to understand the use of robot
        (CHOOSE_CURRENCY,"specify_currency"):(SEARCH,"OK,I'm doing ,just wait for a second please"), 
        (CHOOSE_CURRENCY,"help"):(CHOOSE_CURRENCY,"you need to tell me what's currency you want to know about,I can show you a list of currency I can help you:\n China:CHY\n Malaysia:MYR\n Canda:CAD\n Switzerland:CHF\n Japan:JPY\n Taiwan:TWD"),#list the currency's code
        (SEARCH,"currency_search"):(SEARCH,"OK,just a few seconds"),
        (SEARCH,"goodbye"):(INIT,"I hope my help is usful") # wait for the next consultion
        }
interpreter=interprete()
def respond(policy,state,message):
    intent=interpreter.parse(message)["intent"]["name"]
    (new_state,response)=policy[(state,intent)]
    return new_state,response
def send_message(policy,state,message):
     print("USER : {}".format(message))
     new_state, response = respond(policy, state, message)
     print("BOT : {}".format(response))
     return new_state
state=INIT
def send_messages(message,state,Policy=policy):
    new_state,response=respond(policy,state,message)
    return new_state, response

