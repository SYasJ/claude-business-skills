---
name: video-storyboard
description: "Write a shot-by-shot visual storyboard for a video, naming what is on screen, the motion, and the audio for each shot. Use when the user mentions storyboard, video storyboard, shot list, scene by scene video, or asks for a video storyboard. Creator, social, and prompting skill by Yasir Jilani."
license: MIT
compatibility: Agent Skills standard. No network access, extra packages, or credentials required.
metadata:
  author: Yasir Jilani
  version: "1.0.0"
  domain: creator
---

# Video Storyboard

Write a shot-by-shot visual storyboard for a video, naming what is on screen, the motion, and the audio for each shot.

## When to use this skill

Use this skill when the user:

- storyboard
- video storyboard
- shot list
- scene by scene video
- visual script
- shot breakdown

## When not to use this skill

- The user wants a different domain's specialist skill.
- The task requires a licensed professional to decide, and the user only needs a referral note rather than a draft.
- The request asks you to deceive, evade a control, or hide material facts.

## Professional boundary

Creator work must be original and honest. Do not copy another person's script, footage, voice, or caption. Do not invent metrics, fake engagement, or undisclosed sponsorships. Do not impersonate a real person. Prompt skills must not weaken safety rules.

## Operating boundaries

- Use only information the user provides or files they explicitly ask you to read. Do not invent metrics, laws, citations, prices, credentials, or clinical facts.
- Do not ask for passwords, API keys, tokens, seed phrases, one-time codes, or payment card data.
- Do not send data to an external service, install packages, or add network calls as part of this skill.
- Separate facts, assumptions, and recommendations. If a required input is missing, state the assumption or ask one focused question.
- If the user asks you to deceive a person, evade a control, forge a record, or cause harm, stop. Offer a legitimate alternative.
- Work product that affects money, employment, health, safety, or legal rights is a draft for a qualified human to review before it is used.

## Inputs to collect

- The video topic and goal
- The intended length
- The narration or script if they have it
- The style and on-screen text they want

## Workflow


### 1. Step 1

Break the video into scenes and each scene into shots. One shot = one camera moment.
### 2. For each shot

describe what the viewer sees (on-screen elements, text overlays, B-roll), the motion (pan, zoom, static, transition), and the audio (VO line, music cue, silence).
### 3. Step 3

Sync each shot to the narration or talking point it covers. A storyboard not tied to the VO cannot be edited.
### 4. Step 4

Flag shots that require footage the creator does not have, and suggest an alternative (B-roll, screen recording, graphic).
### 5. Step 5

Note the estimated duration per shot so the total stays in range.
### 6. Step 6

Do not claim a shot is achievable if it requires licensed footage, a real person's likeness, or a location the creator has not mentioned.

## Output

Deliver a **video storyboard**.

- Purpose of this video storyboard, in two sentences.
- Facts the user supplied, listed separately from assumptions.
- The work itself, in the structure the workflow names.
- Open questions, risks, and the single next action with an owner.
- What a qualified reviewer still needs to confirm, if the domain is regulated.

## Quality bar

- Every number, date, name, and citation came from the user or is marked as an assumption.
- The artifact can be used without reading this skill again.
- Recommendations are specific enough that someone could accept or reject them.
- Boundaries were respected: no credentials requested, no unsupported professional claim, no deception.

## Example

### Scenario

Maya Brooks, creator at Weeknight Table in Calgary, needs a video storyboard by 30 September 2026. A creator wants a 60-second explainer video about compound interest with five scenes.

### Example data

```text
From: Maya Brooks, creator
Organization: Weeknight Table, Calgary
Date: 14 September 2026
Needed by: 30 September 2026

A creator wants a 60-second explainer video about compound interest with five scenes.

owned file: dated
someone else's script: not in the folder
paid: only if stated
export: only if attached
```

### Example outcome

**Video storyboard**
To: Maya Brooks, creator, Weeknight Table
Date: 14 September 2026

**Decision**
A 6-shot storyboard: title card (3s), problem scene with animated coins (12s), formula graphic with VO (15s), growth chart B-roll (10s), three examples on screen (12s), CTA with subscribe text (8s). Each shot includes the VO line, on-screen text, and transition.

**From the file**
- owned file: dated
- someone else's script: not in the folder
- paid: only if stated
- export: only if attached

Nothing in this draft was added from outside that file.
Next: Maya Brooks by 30 September 2026. This is not a sign-off.

## Anti-patterns

- A storyboard for someone else's footage
- A shot list with no audio note
- Timings that add up to more than the target length

## Related skills

- `youtube-video-outline`
- `instagram-story-sequence`
- `video-prompt-spec`
