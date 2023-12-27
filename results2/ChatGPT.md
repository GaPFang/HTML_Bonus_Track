# multi-agents version

## Configuration

- GPT-3.5 and GPT-4. **WARNING!** OpenAI charges us for GPT-4.
- Argument strength of `agentA-arguStre` Agent-A and `agentB-arguStre` Agent-B.
- `subject` e.g., "Should we regulate the use of large language models in education and research?"

## (Sec 2) Play the role in SocraSynth
### A
I’m organizing a committee to engage in debates on various subjects. As the moderator, I will introduce a subject for you, Agent A, and another participant, Agent B, to debate. Agent A, you will advocate in favor of the issue, so please prepare evidence to strengthen your argument. On a scale from 0 to 1, where 0 denotes complete agreement and 1 indicates a devil’s advocate stance, your argument strength is rated at `agentA-arguStre`.
### B
I’m organizing a committee to engage in debates on various subjects. As the moderator, I will introduce a subject for you, Agent B, and another participant, Agent A, to debate. Agent B, you will oppose in favor of the issue, so please prepare evidence to strengthen your argument. On a scale from 0 to 1, where 0 denotes complete agreement and 1 indicates a devil’s advocate stance, your argument strength is rated at `agentB-arguStre`.

## Announce the subject of the debate
### A
Agent-A, we are in the process of selecting a suitable subject for debate. What do you think of “`subject`” as a balanced subject for our debate contest?
### B
Agent-B, we are in the process of selecting a suitable subject for debate. What do you think of “`subject`” as a balanced subject for our debate contest?

## Propose ten topics or issues for debate
### A
Agent-A, could you please suggest various ten topics or themes for the above debate subject?
Print the ten topics with item list.
### B
Agent-B, could you please suggest various ten topics or themes for the above debate subject?
Print the ten topics with item list.

## Review the lists and reduce the topics to five
### A
Agent-A, you and Agent-B proposed ten topics:
`copy and paste Agent-A's and Agent-B's ten topics.`

Please review the lists and reduce the topics to five.
### B
Agent-B, you and Agent-A proposed ten topics:
`copy and paste Agent-B's and Agent-A's ten topics.`

Please review the lists and reduce the topics to five.

## identify and refine the list of five to be somehow overlapping
### A
Agent-A, you and Agent-B reduced the topics to five:
`copy and paste Agent-A's and Agent-B's five topics.`

Please identify and refine the list of five to be somehow overlapping.  
### B
Agent-B, you and Agent-A reduced the topics to five:
`copy and paste Agent-A's and Agent-B's five topics.`

Please identify and refine the list of five to be somehow overlapping.

## Agent A invites feedback from Agent B. Agent A invites feedback from Agent B. The agents then collaboratively reach consensus on the topics or themes to be discussed.
### A
Agent-A, you and Agent-B proposed five debate topics:
`copy and paste Agent-A's and Agent-B's debate topics.`

Please review these debate topics, reduce them to five debate topics, provide concerns, the center, and the focus of the debate topics, and invite feedback from Agent B.
### Loop (B, A, ...)
Agent-B, Agent-A request you to review these debate topics:
`copy and paste Agent-A's debate topics.`

Please review these debate topics and provide concerns, the center, and the focus of the debate topics.

## (Sec 3) Debate, loop with three rounds in SocraSynth
### A (The 1st round, Agent A’s Opening Remarks)
Agent-A, as the proponent of the subject “`subject`”, you advocate the debate topics, so please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 indicating a confrontational approach and 0 signifying a conciliatory stance, your argument strength is rated at `agentA-arguStre`. Now, please provide your arguments on the five debate topics.
### B (The 1st round, Agent B’s Counter Arguments)
Agent-B, as the opponent of the subject “`subject`”, you oppose the debate topics, so please prepare evidence to strengthen your argument. On a value that ranges from 0 to 1, with 1 indicating a confrontational approach and 0 signifying a conciliatory stance, your argument strength is rated at `agentB-arguStre`. 
These are arguments from Agent-A:
`copy and paste Agent-A's debate topics.`

Please articulate counter-arguments to the points made by Agent A.
### A (The 2nd & 3rd & 4th rounds, Agent A’s Arguments)
These are counter-arguments from Agent-B:
`copy and paste Agent-B's debate topics.`

Please articulate arguments against the points made by Agent B.
### B (The 2nd & 3rd & 4th rounds, Agent B’s Counter Arguments)
These are arguments from Agent-A:
`copy and paste Agent-A's debate topics.`

### A (The 2nd & 3rd & 4th rounds, Agent A’s Arguments)
These are counter-arguments from Agent-B:
`copy and paste Agent-B's debate topics.`

Please articulate arguments against the points made by Agent B.
### B (The 2nd & 3rd & 4th rounds, Agent B’s Counter Arguments)
These are arguments from Agent-A:
`copy and paste Agent-A's debate topics.`

### A (The 2nd & 3rd & 4th rounds, Agent A’s Arguments)
These are counter-arguments from Agent-B:
`copy and paste Agent-B's debate topics.`

Please articulate arguments against the points made by Agent B.
### B (The 2nd & 3rd & 4th rounds, Agent B’s Counter Arguments)
These are arguments from Agent-A:
`copy and paste Agent-A's debate topics.`

## Confirm that they have exhaustively presented their arguments and counterarguments
### A (End or continue.)
Agent-A, These are arguments from Agent-B:
`copy and paste Agent-B's debate topics.`

It's time to close the debate. As the proponent of the subject “`subject`”, you advocate the debate topics, so please provide the conclusions of your argument. We will have a grading later, so please demonstrate as clearly as possible. Answer with the following form:
[debate topic1]:
- your argument on the topic
[debate topic2]:
- your argument on the topic
...
[debate topic5]:
- your argument on the topic
conclusion:
- your conclusion
### B (End or continue.)
Agent-B, These are arguments from Agent-A:
  `copy and paste Agent-A's debate topics, if existing.`

It's time to close the debate. As the opponent of the subject “`subject`”, you oppose the debate topics, so please provide the conclusions of your counter-argument. We will have a grading later, so please demonstrate as clearly as possible. Answer with the following form:
[debate topic1]:
- your argument on the topic
[debate topic2]:
- your argument on the topic
...
[debate topic5]:
- your argument on the topic
conclusion:
- your conclusion
