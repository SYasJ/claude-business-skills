# Video Prompt Spec

`video-prompt-spec`

## What this is for

Specify a video prompt for shots she can legally use, with no real-person clone.

## Scenario

Maya wants a 4-second opener of receipts landing on a counter. She does not want her face generated, and she does not want a store interior the tool might invent.

## Example data

```text
length: 4 seconds
shot: receipts drop onto a wood counter, top-down
no: face, store interior, logos, cloned voice
on-screen text: none in the generated shot
use: opener only, her channel
```

## Example outcome

**Video spec**
4 seconds. Top-down. Blank wood counter. Four blank receipts land. No text. No face. No aisle. No logo.

Reject the clip if a face, a readable brand, or a store aisle appears.
No voice in this clip. Her real read stays a separate file.
This spec does not ask a tool to copy a living person.
