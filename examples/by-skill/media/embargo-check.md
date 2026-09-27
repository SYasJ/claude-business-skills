# Embargo Check

`embargo-check`

## What this is for

Check whether an embargo still applies and who agreed to it.

## Scenario

A utility release is embargoed until 10:00 ET Tuesday. The desk agreed in writing on Monday. It is 07:30 in Calgary on Tuesday. An editor wants to post now.

## Example data

```text
embargo: 10:00 ET, Tuesday 16 Sep 2026
desk agreed: yes, email 15 Sep 18:04
now: 07:30 America/Edmonton, Tuesday 16 Sep
ET offset they stated: ET is 2 hours ahead of MT
decision owner: Jonah Ellis
```

## Example outcome

**Embargo note**
Do not post.

07:30 MT is 09:30 ET. The embargo they agreed to lifts at 10:00 ET, which is 08:00 MT.
The desk agreed. Early is not available.
Owner: Jonah. Post at or after 08:00 MT if the story is ready, not before.
