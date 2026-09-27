# Pricing Page Note

`pricing-page-note`

## What this is for

Check a pricing page against the plans and the limits they actually enforce.

## Scenario

The public page says Pro includes unlimited exports. The product blocks an export at 5,000 rows. Jonah can edit the page. There is no competitor price in the file.

## Example data

```text
plan: Pro
page: unlimited exports
product: blocks at 5000 rows
discount on the page: none
editor: Jonah Park
competitor price: not in the file
```

## Example outcome

**Page note**
Change 'unlimited exports' to 5,000 rows. The product blocks there.
Do not add a competitor's price. None is in the file.
No discount line. None was set.
Editor: Jonah. The page and the product have to match before the next ad runs.
