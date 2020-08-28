from slack_webhook import Slack

def slack_alert(file_name_unknown):
    slack = Slack(url='https://hooks.slack.com/services/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')
    slack.post(text = "Unknown Folder : " + file_name_unknown)
    #print('working')

def com_slack_alert(file_name_known):
    slack = Slack(url='https://hooks.slack.com/services/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')
    slack.post(text = "Successfully Done With : " + file_name_known)
