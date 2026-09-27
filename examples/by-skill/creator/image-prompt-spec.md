# Image Prompt Spec

`image-prompt-spec`

## What this is for

Specify an image prompt from the shot the person can use, with no copied style and no real person's face.

## Scenario

Maya needs a thumbnail image for the faceless channel. She wants the counter and the receipts. She does not want a famous cook's face or a store logo.

## Example data

```text
use: thumbnail, her channel
must show: paper receipts on a wood counter, top-down, no face
must not show: a real person's face, a store logo, a copied lower-third
text in image: $52
style references: none she has rights to
```

## Example outcome

**Image spec**
Top-down wood counter. Four paper receipts. Black text "$52" on one corner. No face. No logo. No hands unless they are unspecified and not a real person.

Do not name another creator, a film, or a brand as the style.
If the tool adds a logo or a face, reject the image and say what it added.
Text check: the only number is $52, matching her food total.
