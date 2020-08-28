from slack_webhook import Slack

def slack_alert(file_name_unknown):
    slack = Slack(url='https://hooks.slack.com/services/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')
    slack.post(text = "Unknown Folder : " + file_name_unknown)
    #print('working')

def com_slack_alert(file_name_known):
    slack = Slack(url='https://hooks.slack.com/services/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')
    slack.post(text = "Successfully Done With : " + file_name_known)
