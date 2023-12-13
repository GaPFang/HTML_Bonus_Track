import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import json
from time import sleep
import signal
import os
import sys

###############  variables  ###############
arguStre_A = 0.9
arguStre_B = 0.9
subject = 'Does technology strengthen connections between people?'

model_A = "gpt-3.5-turbo-16k"
frequency_penalty_A = 0
n_A = 1
presence_penalty_A = 0
temperature_A = 1
top_p_A = 1

model_B= "gpt-3.5-turbo-16k"
frequency_penalty_B = 0
n_B = 1
presence_penalty_B = 0
temperature_B = 1
top_p_B = 1
###########################################

prompts = []
prompt_index = 0
json_data = {
    "subject": subject,
    "Agent-A": {
        "model": model_A,
        "frequency_penalty": frequency_penalty_A,
        "n": n_A,
        "presence_penalty": presence_penalty_A,
        "temperature": temperature_A,
        "top_p": top_p_A
    },
    "Agent-B": {
        "model": model_B,
        "frequency_penalty": frequency_penalty_B,
        "n": n_B,
        "presence_penalty": presence_penalty_B,
        "temperature": temperature_B,
        "top_p": top_p_B
    }
}
global stop
stop = False

# scrape respnse from the website and save it to the file
login = "http://140.112.90.203:6464/login"
website = "http://140.112.90.203:6464/chat"
sess = requests.Session()
# sess.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
driver = webdriver.Chrome()
driver.get(login)

def init():
    script = "teamname = document.getElementById('teamname'); teamname.value = 't1509';pw = document.getElementById('passwd'); pw.value = '908c5e';pw.nextElementSibling.nextElementSibling.nextElementSibling.click();"
    driver.execute_script(script)
    driver.get(website)
    script = "text_area = document.getElementById('llm_config'); text_area.value = '" + json.dumps(json_data) + "';text_area.nextElementSibling.click();"
    driver.execute_script(script)

def waitResponse(): # True if the message is finished
    # while True:
    #     soup = bs(driver.page_source, 'html.parser')
    #     if soup.find('div', {'id': 'temp'}) is not None:
    #         break
    #     sleep(1)
    # while True:
    #     soup = bs(driver.page_source, 'html.parser')
    #     if soup.find('div', {'id': 'temp'}) is None:
    #         break
    #     sleep(1)
    while True:
        soup = bs(driver.page_source, 'html.parser')
        userinput = soup.find('textarea', {'id': 'userinput'})
        if userinput.disabled == True:
            break
        sleep(1)
    
def getMessage(agent): # get the message from the agentA or agentB
    soup = bs(driver.page_source, 'html.parser')
    res = soup.find_all('div', {'class': agent + 'message'})
    return res[-1].text

def replaceMessage(message): # replace the message
    if "`agentA-arguStre`" in message:
        message = message.replace("`agentA-arguStre`", str(arguStre_A))
    if "`agentB-arguStre`" in message:
        message = message.replace("`agentB-arguStre`", str(arguStre_B))
    if "`subject`" in message:
        message = message.replace("`subject`", subject)
    if "`copy and paste Agent-A's and Agent-B's ten topics.`" in message:
        res_A = getMessage('agentA')
        res_B = getMessage('agentB')
        # res_A = '1.' + res_A.split('1.', 1)[1]
        # segments = res_A.split('10.', 1)
        # res_A = segments[0] + '10.' + segments[1].split('.', 1)[0] + '.\n'
        # res_B = '1.' + segments[1].split('1.', 1)[1]
        # segments = res_B.split('10.', 1)
        # res_B = segments[0] + '10.' + segments[1].split('.', 1)[0] + '.'
        res = res_A + '\n' + res_B
        message = message.replace("`copy and paste Agent-A's and Agent-B's ten topics.`", res)
    if "`copy and paste Agent-B's and Agent-A's ten topics.`" in message:
        res_A = getMessage('agentA')
        res_B = getMessage('agentB')
        # res_B = '1.' + res_B.split('1.', 1)[1]
        # segments = res_B.split('10.', 1)
        # res_B = segments[0] + '10.' + segments[1].split('.', 1)[0] + '.\n'
        # res_A = '1.' + segments[1].split('1.', 1)[1]
        # segments = res_A.split('10.', 1)
        # res_A = segments[0] + '10.' + segments[1].split('.', 1)[0] + '.'
        res = res_B + '\n' + res_A
        message = message.replace("`copy and paste Agent-B's and Agent-A's ten topics.`", res)
    if "`copy and paste Agent-A's and Agent-B's five topics.`" in message:
        res_A = getMessage('agentA')
        res_B = getMessage('agentB')
        # res_A = '1.' + res_A.split('1.', 1)[1]
        # segments = res_A.split('5.', 1)
        # res_A = segments[0] + '5.' + segments[1].split('.', 1)[0] + '.\n'
        # res_B = '1.' + segments[1].split('1.', 1)[1]
        # segments = res_B.split('5.', 1)
        # res_B = segments[0] + '5.' + segments[1].split('.', 1)[0] + '.'
        res = res_A + '\n' + res_B
        message = message.replace("`copy and paste Agent-A's and Agent-B's five topics.`", res)
    if "`copy and paste Agent-B's and Agent-A's five topics.`" in message:
        res_A = getMessage('agentA')
        res_B = getMessage('agentB')
        # res_B = '1.' + res_B.split('1.', 1)[1]
        # segments = res_B.split('5.', 1)
        # res_B = segments[0] + '5.' + segments[1].split('.', 1)[0] + '.\n'
        # res_A = '1.' + segments[1].split('1.', 1)[1]
        # segments = res_A.split('5.', 1)
        # res_A = segments[0] + '5.' + segments[1].split('.', 1)[0] + '.'
        res = res_B + '\n' + res_A
        message = message.replace("`copy and paste Agent-B's and Agent-A's five topics.`", res)
    if "`copy and paste overlapping five topics`" in message:
        ##  I don't know how to do this ##
        print('I don\'t know how to do this:\n`copy and paste overlapping five topics`\n', file=sys.stderr)
        exit(0)
    if "`copy and paste Agent-A's debate topics.`" in message:
        res_A = getMessage('agentA')
        message = message.replace("`copy and paste Agent-A's debate topics.`", res_A)
    if "`copy and paste Agent-B's debate topics.`" in message:
        res_B = getMessage('agentB')
        message = message.replace("`copy and paste Agent-B's debate topics.`", res_B)
    if "`copy and paste Agent-A's debate topics, if existing.`" in message:
        res_A = getMessage('agentA')
        if 'I am ready to deliver my closing statements.' in res_A:
            message = message.replace("Agent-B, These are arguments from Agent-A:   `copy and paste Agent-A's debate topics, if existing.`", "")
        waitResponse()
        res_B = getMessage('agentB')
        if 'I am ready to deliver my closing statements.' not in res_B:
            prompt_index -= 2
        

    return message

def sendMessage(agent, message): # send the message to the agentA or agentB
    if agent == 'agentA':
        action = 'Agent-A'
    elif agent == 'agentB':
        action = 'Agent-B'
    message = replaceMessage(message)
    script = "text_area = document.getElementById('userinput'); text_area.value = '" + message + "';act = document.getElementById('action');act.value = '" + action + "';act.nextElementSibling.click();"
    driver.execute_script(script)
    return

def getPrompts(): # get the prompt from ChatGPT.md
    f = open('html.2023.bonusfinal-public/generation/ChatGPT.md', 'r')
    lines = f.readlines()
    f.close()
    for i in range(10, len(lines)):
        if '#' in lines[i] or lines[i][0] == '\n':
            continue
        else:
            newLine = ""
            while i < len(lines) and '#' not in lines[i] and lines[i][0] != '\n':
                newLine += lines[i].replace('\n', ' ')
                i += 1
            prompts.append(newLine)

def signal_handler(sig, frame): # Ctrl+C
    global stop
    stop = ~stop

signal.signal(signal.SIGUSR1, signal_handler)
f = open('pause', 'w')
f.write('#!/bin/bash\nkill -SIGUSR1 ' + str(os.getpid()))
f.close()

# main
if __name__ == '__main__':
    init()
    getPrompts()
    while prompt_index < len(prompts):
        while stop:
            sleep(1)
        sendMessage('agentA', prompts[prompt_index])
        waitResponse()
        sendMessage('agentB', prompts[prompt_index + 1])
        waitResponse()