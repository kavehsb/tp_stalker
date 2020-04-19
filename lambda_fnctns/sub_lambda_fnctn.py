import json
import re
import pandas as pd

# This code assumes the BlobServiceClient is already created

# event needs to pass both userphonenum and usertopicsel
def sub_lambda(event, context): 
    userPhoneNum = event['num']
    userTopicSel = event['select']
    
    # Apparently this creates a Connection Link string
    collection_link = database_link + '/colls/' + 'HDIcontainer'

    # Validates phone number
    checkNum = re.search("\+1\d{10}", userPhoneNum)

    # There's one topic, so it's likely this selection line can be tossed out
    topicSelection = {'TODO1', 'TODO2', 'TODO3'}

    if userTopicSel not in topicSelection: 
        # Gateway returns an HTTP 400 error (badrequest)
        raise Exception('badrequest')
        return False

    if not checkNum: 
        # Gateway returns a HTTP 400 error
        raise Exception('badrequest')
        return False
    else: 
        # create a dictionary row entry
        data_dict = userPhoneNum + " " + userTopicSel
        # convert dictionary to JSON object
        data_dict = json.dumps(data_dict)
        insert_data = client.UpsertItem(collection_link,json.loads(data_dict))
        # needs a catcher in HTML JavaScript or something to print based on Boolean return
        return True
