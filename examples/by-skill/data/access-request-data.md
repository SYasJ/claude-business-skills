# Data Access Request

`access-request-data`

## What this is for

Triage an internal request for data the company already holds, against the approver they name.

## Scenario

An analyst asked Noah for the full tickets table, including home addresses, to 'get a feel for the voice'. Their policy says the privacy lead approves personal columns. That role is vacant.

## Example data

```text
asker: Sam Okonkwo, analyst
table: support.tickets
why: get a feel for the voice
columns requested: all
personal columns in the table: email, home address
approver in policy: privacy lead
privacy lead: vacant
Noah's authority: he cannot approve his own pipeline, and he is not the privacy lead
```

## Example outcome

**Access note**
Do not grant the full table.

The why is not a question the table can answer. Send it back.
If they return with a real question, drop email and home address unless the privacy lead approves. That role is vacant, so those columns wait.
Noah does not approve this. Seniority is not the approver.
A shared login is not an option in this note.
Next: Sam rewrites the why, or the request stays closed.
