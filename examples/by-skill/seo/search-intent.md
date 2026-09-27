# Search Intent

`search-intent`

## What this is for

Say what the searcher is trying to do, from the query and the page the user has.

## Scenario

The query Diane cares about is 'furnace repair Airdrie'. The furnace page tells the shop's origin story and does not list the city, the phone, or what a repair visit includes.

## Example data

```text
query: furnace repair Airdrie
page: /services/furnace
page answers: how the shop started in 2014
searcher job: find someone who will come fix a furnace in Airdrie
phone on the home page: 403-555-0148
phone on this page: absent
```

## Example outcome

**Intent note**
Mismatch. The query asks for a repair in Airdrie. The page answers a brand story.

Do not stuff the query into the origin paragraph.
Add, if she can stand behind it: the city, the phone that is already on the home page, and what a repair visit includes. She has not written the visit scope. Leave that blank rather than inventing a promise.
Until those facts are on the page, this URL does not answer the query.
