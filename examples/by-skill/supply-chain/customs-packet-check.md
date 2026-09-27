# Customs Packet Check

`customs-packet-check`

## What this is for

Check a shipment packet for the documents the user says the lane requires.

## Scenario

A packet for filters from Calgary to a US customer is missing the commercial invoice. A note in the folder suggests describing them as samples so the value line can be blank.

## Example data

```text
lane: Calgary to US customer, her required list
required: commercial invoice, packing list, COO if the customer asked
in the packet: packing list, no invoice, no COO ask on file
suggestion in the folder: call them samples
value on the PO: 40 filters, $18 each
who files: the forwarder, after her packet is complete
```

## Example outcome

**Packet check**
Hold. The commercial invoice is missing.
Do not describe the filters as samples. The PO says 40 filters at $18. A false description is not a fix.
COO: not required in her list for this shipment. Do not add one to look busy.
Who completes the invoice: Diane, then the forwarder files. This check is not a brokerage opinion.
