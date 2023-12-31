import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from time import sleep
import signal
import os
import sys
import argparse

###############  variables  ###############
arguStre_A = 0.9
arguStre_B = 0.9
subject = ''
# subject = 'Does Pokemon Go do more good than harm to our society?'

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
haveWaited = False
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
global pause
pause = False
global res_A
res_A = ""
global res_B
res_B = ""

# scrape respnse from the website and save it to the file
login = "http://140.112.90.203:6464/login"
website = "http://140.112.90.203:6464/chat"
sess = requests.Session()
# sess.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
driver = webdriver.Chrome()
driver.get(login)

def init():
    script = """
        teamname = document.getElementById('teamname');
        teamname.value = 't1509';
        pw = document.getElementById('passwd');
        pw.value = '908c5e';
        pw.nextElementSibling.nextElementSibling.nextElementSibling.click();
    """
    driver.execute_script(script)
    driver.get(website)
    script = """
        text_area = document.getElementById('llm_config');
        text_area.value = '""" + json.dumps(json_data) + """';
        text_area.nextElementSibling.click();
    """
    driver.execute_script(script)

def waitResponse(): # True if the message is finished
    while True:
        soup = bs(driver.page_source, 'html.parser')
        if soup.find('div', {'id': 'temp'}) is not None:
            break
        sleep(1)
    while True:
        soup = bs(driver.page_source, 'html.parser')
        if soup.find('div', {'id': 'temp'}) is None:
            break
        sleep(1)
    
def getMessage(agent): # get the message from the agentA or agentB
    soup = bs(driver.page_source, 'html.parser')
    res = soup.find_all('div', {'class': agent + 'message'})
    return res[-1].text

def getAllMessages(output_file_name): # get all the messages
    soup = bs(driver.page_source, 'html.parser')
    res = soup.find_all('div', {'class': ['agentAmessage', 'agentBmessage', 'userAmessage']})
    fd = open(output_file_name + '.txt', 'w')
    for i in range(len(res)):
        fd.write(res[i].text)
    fd.close()

def replaceMessage(message): # replace the message
    global res_A
    global res_B
    if "`agentA-arguStre`" in message:
        message = message.replace("`agentA-arguStre`", str(arguStre_A))
    if "`agentB-arguStre`" in message:
        message = message.replace("`agentB-arguStre`", str(arguStre_B))
    if "`subject`" in message:
        message = message.replace("`subject`", subject)
    if "`copy and paste Agent-A's and Agent-B's ten topics.`" in message:
        res = res_A + '\n' + res_B
        message = message.replace("`copy and paste Agent-A's and Agent-B's ten topics.`", res)
    if "`copy and paste Agent-B's and Agent-A's ten topics.`" in message:
        res = res_B + '\n' + res_A
        message = message.replace("`copy and paste Agent-B's and Agent-A's ten topics.`", res)
    if "`copy and paste Agent-A's and Agent-B's five topics.`" in message:
        res = res_A + '\n' + res_B
        message = message.replace("`copy and paste Agent-A's and Agent-B's five topics.`", res)
    if "`copy and paste Agent-B's and Agent-A's five topics.`" in message:
        res_A = getMessage('agentA').replace('\n', ' ').replace('\t', '')
        res_B = getMessage('agentB').replace('\n', ' ').replace('\t', '')
        res = res_B + '\n' + res_A
        message = message.replace("`copy and paste Agent-B's and Agent-A's five topics.`", res)
    if "`copy and paste Agent-A's Agent-B's perspectives of five topics.`" in message:
        res = res_A + '\n' + res_B
        message = message.replace("`copy and paste Agent-A's Agent-B's perspectives of five topics.`", res)
    if "`copy and paste Agent-B's Agent-A's perspectives of five topics.`" in message:
        res = res_B + '\n' + res_A
        message = message.replace("`copy and paste Agent-B's Agent-A's perspectives of five topics.`", res)
    if "`copy and paste Agent-A's and Agent-B's debate topics.`" in message:
        res = res_B + '\n' + res_A
        message = message.replace("`copy and paste Agent-A's and Agent-B's debate topics.`", res)
    if "`copy and paste Agent-A's debate topics.`" in message:
        res_A = getMessage('agentA')
        message = message.replace("`copy and paste Agent-A's debate topics.`", res_A)
    if "`copy and paste Agent-B's debate topics.`" in message:
        res_B = getMessage('agentB')
        message = message.replace("`copy and paste Agent-B's debate topics.`", res_B)
    if "`copy and paste Agent-A's debate topics, if existing.`" in message:
        res_A = getMessage('agentA')
        message = message.replace("`copy and paste Agent-A's debate topics, if existing.`", res_A)
    return message.replace('\n', ' ').replace('"', '').replace('\'', '').replace('\t', '')

def sendMessage(agent, message): # send the message to the agentA or agentB
    if agent == 'agentA':
        action = 'Agent-A'
    elif agent == 'agentB':
        action = 'Agent-B'
    message = replaceMessage(message)
    # print(message)
    script = """
        text_area = document.getElementById('userinput');
        text_area.value = '""" + message + """';
        act = document.getElementById('action');
        act.value = '""" + action + """';
        act.nextElementSibling.click();
    """
    driver.execute_script(script)
    return

def getPrompts(): # get the prompt from ChatGPT.md
    f = open('html.2023.bonusfinal-public/generation/ChatGPT.md', 'r')
    lines = f.readlines()
    f.close()
    i = 10
    while i < len(lines):
        if '#' in lines[i] or lines[i][0] == '\n':
            i += 1
            continue
        else:
            newLine = ""
            while i < len(lines) and '#' not in lines[i]:
                if lines[i][0] == '\n':
                    i += 1
                    continue
                newLine += lines[i].replace('\n', ' ')
                i += 1
            prompts.append(newLine)

def signal_handler(sig, frame): # pause the program
    global pause
    pause = ~pause

signal.signal(signal.SIGUSR1, signal_handler)
f = open('pause', 'a')
os.chmod('pause', 0o700)
f.truncate(0)
f.write('#!/bin/bash\nkill -SIGUSR1 ' + str(os.getpid()))
f.close()

# main
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='name of the subject')
    parser.add_argument('subject', help='debate subject')
    parser.add_argument('-c', '--close_directly', action='store_true', help="If specified, the program won't wait for input when it end.")
    args = parser.parse_args()
    output_file_name = args.name
    subject = args.subject
    init()
    getPrompts()
    while prompt_index < len(prompts):
        while pause:
            sleep(1)
        sendMessage('agentA', prompts[prompt_index])
        waitResponse()
        sendMessage('agentB', prompts[prompt_index + 1])
        waitResponse()
        res_A = getMessage('agentA')
        res_B = getMessage('agentB')
        prompt_index += 2
    getAllMessages(output_file_name)
    print("A's response:")
    print(res_A)
    print("B's response:")
    print(res_B)
    with open(output_file_name+'_final_res.txt', 'w') as file:
        file.write("A's response:\n")
        file.write(res_A)
        file.write('\n')
        file.write("B's response:\n")
        file.write(res_B)
        file.write('\n')
    if not args.close_directly:
        input('press enter to exit...')
