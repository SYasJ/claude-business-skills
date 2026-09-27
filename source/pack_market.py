from load_cards import parse_cards

def pack(domain, text):
    return {"domain": domain, "skills": parse_cards(text)}

PACKS = [pack(
    {
        "id": "marketing",
        "title": "Marketing",
        "summary": "Positioning, campaigns, content, and claims that a company can actually support.",
        "keywords": ["marketing", "brand", "content", "campaign", "positioning"],
    },
    r'''
== positioning-statement | Positioning Statement ==
job: Write a positioning statement that names the buyer, the alternative, and the difference you can prove.
artifact: positioning statement
triggers:
  - positioning
  - positioning statement
  - who is this for
  - category message
inputs:
  - The primary buyer
  - The alternative they use today
  - The difference you can prove
  - Buyers you will not serve
steps:
  - Buyer: One primary buyer. A statement for everyone is a statement for no one.
  - Alternative: Include the status quo. Name a vendor only if the user supplied that competitor.
  - Difference: One difference that matters to the buyer's job and that the user can evidence.
  - Proof: The evidence sits next to the difference. If proof is missing, the positioning is a hypothesis.
  - Boundary: Who it is not for. That line protects sales from bad-fit deals.
  - Length: A short statement plus a paragraph. No manifesto.
anti:
  - Positioning for everyone.
  - A difference you cannot prove.
  - A category claim copied from a larger company.
example: A team says they are the 'AI platform for business' and cannot name the buyer or the alternative.
example_out: A statement aimed at one buyer, with the spreadsheet or incumbent they actually replace, and a hypothesis label if proof is thin.
related:
  - messaging-house
  - competitive-strategy

== messaging-house | Messaging House ==
job: Build a messaging house so headline, pillars, and proof do not contradict each other.
artifact: messaging house
triggers:
  - messaging house
  - message pillars
  - brand messages
  - what do we say
inputs:
  - The positioning
  - Three proof points
  - Objections sales hears
  - Claims that must not be made
steps:
  - Headline: One sentence from the positioning. If positioning is missing, do that first.
  - Pillars: Three pillars a buyer can remember. Each pillar has a customer benefit, not an internal project name.
  - Proof under each pillar: Only supplied proof. Empty proof means the pillar is not ready for a homepage.
  - Objection line: One honest response to the top objection, with no fake logos.
  - Words to avoid: A short list of hype and unsupported comparisons.
  - Channel note: What changes for a sales call versus a homepage, without changing the meaning.
anti:
  - Pillars with no proof.
  - Different claims in sales and on the site.
  - Internal jargon as a pillar.
example: The homepage says 'effortless' and sales says implementation takes six weeks.
example_out: A house that replaces 'effortless' with a truthful implementation claim and aligns both channels.
related:
  - positioning-statement
  - marketing-claims-review

== campaign-brief | Campaign Brief ==
job: Brief a campaign with one audience, one offer, one action, and a measurement plan.
artifact: campaign brief
triggers:
  - campaign brief
  - marketing campaign
  - campaign plan
  - launch campaign
inputs:
  - The audience
  - The offer
  - The action you want
  - Budget and channel constraints
steps:
  - One audience: Describe them by situation, not by a vague demographic alone.
  - One offer: What they get if they act. Multiple offers split the brief.
  - Insight: Why this audience would care now, using evidence the user has. Mark assumptions.
  - Channels: Only channels the team can staff. A channel list is not a plan.
  - Measurement: The action that counts, the baseline if known, and the date of the readout.
  - Claims: Point every factual claim at the claims review. Do not invent urgency.
anti:
  - Five audiences in one brief.
  - Vanity metrics as the goal.
  - Fake deadlines.
example: A team wants a campaign for 'awareness' with six channels and no offer.
example_out: A brief that forces one audience, one offer, staffed channels, and a readout date.
related:
  - marketing-experiment
  - creative-brief

== content-calendar | Content Calendar ==
job: Build a content calendar from buyer questions and capacity, not from a need to post daily.
artifact: content calendar
triggers:
  - content calendar
  - editorial calendar
  - what should we publish
  - content plan
inputs:
  - Buyer questions already heard
  - Capacity in pieces per week
  - Offers the content should support
  - Channels that are actually maintained
steps:
  - Questions first: List questions sales and support hear. Those outrank topic brainstorms.
  - Capacity: Plan only what the team can draft, review, and proof. A daily cadence they cannot review is a quality problem.
  - Mix: A simple mix of proof, teaching, and offer. Do not pretend a formula is science.
  - Owners and dates: Each piece has a drafter and a reviewer. No owner, no slot.
  - Repurpose: One strong piece can feed a short note. Do not plan seven original ideas if capacity is one.
  - Claims: Flag pieces that would need evidence the company does not have.
anti:
  - A daily calendar with one writer and no reviewer.
  - Topics with no buyer question behind them.
  - Unsourced statistics planned into posts.
example: A founder wants daily posts, and the only writer has four hours a week.
example_out: A calendar of one reviewed piece a week, based on real buyer questions, with repurposing instead of fake volume.
related:
  - seo-content-brief
  - newsletter-editor

== seo-content-brief | SEO Content Brief ==
job: Brief a page that answers a real query, with search intent and substantiation, without keyword stuffing.
artifact: search content brief
triggers:
  - SEO brief
  - content brief
  - rank for this keyword
  - search intent
inputs:
  - The query or topic
  - What the searcher is trying to do
  - Proof and sources the company has
  - The page's business job
steps:
  - Intent: State the job of the searcher. If the user only has a keyword and no intent, say the brief is incomplete.
  - Promise: The page answers that job in the title and the first screen. No bait headline.
  - Outline: Sections that answer the query, plus what you will not cover so the page stays focused.
  - Evidence: Facts need a source the user can point to. No invented statistics or fake reviews.
  - Internal path: Where the reader goes next if they are a fit. One path.
  - Measurement: The query and the on-page action, reviewed after publication. Rankings are not ordered into existence by repetition.
anti:
  - Keyword stuffing.
  - Invented data to look authoritative.
  - A brief that ignores intent.
example: A team wants a page targeting a high-volume keyword that does not match the product.
example_out: A brief that either resets the intent or recommends not writing the page, instead of stuffing the keyword.
related:
  - content-calendar
  - marketing-claims-review

== landing-page-cro | Landing Page Review ==
job: Review a landing page for clarity, proof, and the single action, without dark patterns.
artifact: landing page review
triggers:
  - landing page
  - conversion review
  - homepage critique
  - CRO review
inputs:
  - The page copy or a description
  - The audience
  - The action
  - Proof available
steps:
  - First screen: Can a stranger see who it is for, what it does, and what to do. If not, that is the finding.
  - One action: Competing buttons are a finding. Recommend a primary action.
  - Proof near claims: A claim without nearby proof is a rewrite, not a design tweak.
  - Friction: Forms ask only for what the next step needs. Do not ask for sensitive data to download a brochure.
  - Dark patterns: Refuse fake countdowns, hidden costs, and confirm-shaming. Offer an honest alternative.
  - Test: If the user wants a test, define one change and the success event. Do not test five things at once.
anti:
  - Fake scarcity.
  - A page with three primary actions.
  - Asking for payment card data in a contact form.
example: A page has a countdown timer that resets every visit and three equal buttons.
example_out: A review that removes the fake timer, picks one action, and pairs the main claim with real proof or deletes the claim.
related:
  - marketing-claims-review
  - marketing-experiment

== email-lifecycle | Email Lifecycle ==
job: Design a lifecycle email for one moment, with a true trigger, a useful message, and an honest unsubscribe path.
artifact: lifecycle email spec
triggers:
  - lifecycle email
  - onboarding email
  - nurture sequence
  - retention email
inputs:
  - The trigger event
  - The reader's job at that moment
  - The one action
  - What must be true in the product before sending
steps:
  - Trigger: The event is real and timely. Do not email because a quota of sends exists.
  - Usefulness: The message helps the reader do the next step. A logo refresh is not a reason to email.
  - One action: One link that matters.
  - Truth: Do not imply the reader did something they did not do.
  - Frequency: Where this mail sits among others, so you do not stack three asks in a day.
  - Consent: Include whatever opt-out the user says their policy requires. Do not help hide an unsubscribe.
anti:
  - Fake personalization.
  - Hidden unsubscribe.
  - An email with no trigger.
example: Marketing wants an 'we miss you' email to users who were never active, written as if they had a habit.
example_out: A spec that refuses the fake habit and either changes the trigger or stops the send.
related:
  - sales-email-sequence
  - customer-health-score

== brand-voice-guide | Brand Voice Guide ==
job: Write a short voice guide with examples of on-voice and off-voice lines for real situations.
artifact: brand voice guide
triggers:
  - brand voice
  - tone of voice
  - writing style guide
  - how we sound
inputs:
  - Audiences
  - Words they already like or hate
  - Situations: sales, support, incident, social
  - Claims that are off limits
steps:
  - Principles: Three principles, each with a meaning. 'Be human' alone is not a principle.
  - Examples: For each situation, an on-voice line and an off-voice line. Examples do the teaching.
  - Vocabulary: Words to prefer and words to avoid, including hype and internal jargon.
  - Hard moments: How the voice handles an outage or a mistake. Calm and specific, not cute.
  - Claims: The voice guide points to substantiation. Wit does not excuse a false claim.
  - Length: Short enough that writers will use it. A 40-page guide will be ignored.
anti:
  - Adjectives with no examples.
  - A cute voice for an incident.
  - Banning plain language in the name of brand.
example: The current guide says 'be bold' and writers are producing unsupported superlatives.
example_out: A guide that replaces 'be bold' with examples, and bans superlatives that lack proof.
related:
  - messaging-house
  - marketing-claims-review

== launch-plan | Launch Plan ==
job: Plan a launch as a coordinated set of proofs, enablement, and a rollback, not as a single announcement.
artifact: launch plan
triggers:
  - launch plan
  - product launch
  - go-live marketing
  - announcement plan
inputs:
  - What is actually shipping
  - The audience
  - The date
  - Risks and support readiness
steps:
  - Scope: Describe what a customer can do on launch day. Cut anything that is not ready from the announcement.
  - Audience and offer: Who is invited first, and what they are asked to do.
  - Enablement: Sales and support get the true scope, limits, and FAQ before the public post.
  - Proof: The story, screenshot, or customer quote that is approved. No placeholder quote.
  - Rollback: What you will say and do if the launch fails technically or the claim is wrong.
  - Readout: The date you will judge the launch against a pre-written success signal.
anti:
  - Announcing a feature that is not ready.
  - A fake customer quote.
  - No support briefing.
example: Marketing wants a public launch of a feature that still fails in the main browser.
example_out: A plan that holds the public claim, briefs support on the limit, and defines the rollback line.
related:
  - go-to-market-brief
  - launch-readiness

== customer-story | Customer Story ==
job: Draft a customer story only from approved facts and the customer's words.
artifact: customer story draft
triggers:
  - customer story
  - case study
  - testimonial
  - customer quote
inputs:
  - Approved facts and quotes
  - The customer's approval status
  - The outcome metrics they confirmed
  - What they refused to say
steps:
  - Permission: If the customer has not approved the story, draft it as internal only and say so.
  - Quote hygiene: Use their words. Do not polish a quote into a different claim.
  - Metrics: Only numbers they confirmed. A 'significant improvement' stays qualitative if no number exists.
  - Structure: Problem, what they did, what changed, and what did not change. Honesty includes limits.
  - No invention: Do not add a logo wall, a job title, or a company size they did not confirm.
  - Approval line: What the customer still needs to sign off before publication.
anti:
  - Invented quotes.
  - Metrics the customer did not confirm.
  - Publishing before approval.
example: A marketer wants a case study that says costs fell 40 percent, and the customer only said 'it saved us time'.
example_out: A draft that keeps the time quote, omits the percentage, and marks publication as blocked until approval.
related:
  - marketing-claims-review
  - customer-story

== webinar-run-of-show | Webinar Run of Show ==
job: Plan a webinar that teaches one job and makes one honest ask.
artifact: webinar run of show
triggers:
  - webinar plan
  - run of show
  - online event
  - workshop agenda
inputs:
  - The audience
  - The one teaching goal
  - Speakers
  - The ask
steps:
  - Promise: The title matches the content. No bait title.
  - Run of show: Timed blocks, including questions. A 40-minute monologue is a finding.
  - Proof: Slides use only approved numbers. Mark missing numbers as gaps.
  - Ask: One next step at the end. Do not pretend the session is free of an ask if it is not.
  - Roles: Host, speaker, and the person watching questions. A demo backup if live product is involved.
  - Follow-up: The email after the session restates the teaching point, not only the pitch.
anti:
  - A bait-and-switch title.
  - Unapproved metrics on slides.
  - No time for questions in a session that promised them.
example: A webinar titled as a practical workshop is planned as a 45-minute product pitch.
example_out: A run of show that either retitles the session or replaces half the pitch with the promised practice.
related:
  - campaign-brief
  - workshop-facilitation

== social-content-system | Social Content System ==
job: Set a social posting system that a real person can sustain, with review and no engagement bait.
artifact: social system
triggers:
  - social media plan
  - posting system
  - LinkedIn plan
  - content cadence
inputs:
  - Channels the company will actually maintain
  - Themes tied to buyer questions
  - Reviewer
  - Topics that are off limits
steps:
  - Channel choice: Keep a channel only if someone owns replies. An unowned channel is a reputation risk.
  - Themes: Three themes from real buyer questions. Not a meme strategy by default.
  - Cadence: A cadence the owner can review. Fewer posts, higher truth.
  - Review: Who checks claims before posting. Executives are not exempt from review.
  - Replies: How comments are handled, including criticism. No fake accounts and no bought engagement.
  - Stop list: No impersonation, no fake reviews, no scraped personal details.
anti:
  - Bought engagement.
  - Fake accounts.
  - A cadence nobody can review.
example: A founder wants two posts a day and has no reviewer for technical claims.
example_out: A system with a lower cadence, a named reviewer, and an explicit ban on fake engagement.
related:
  - content-calendar
  - brand-voice-guide

== paid-media-brief | Paid Media Brief ==
job: Brief paid media with an offer, an audience hypothesis, a spend cap, and a stop rule.
artifact: paid media brief
triggers:
  - paid media
  - ads brief
  - paid social
  - search ads brief
inputs:
  - The offer
  - The audience hypothesis
  - Spend cap
  - The conversion event that matters
steps:
  - Offer: The ad promises only what the landing page delivers. Mismatch is a finding.
  - Audience: A hypothesis, labeled as such. Do not invent performance data.
  - Creative claims: Every claim must be supportable. No fake urgency.
  - Measurement: The event that counts, and the minimum data needed before anyone declares a winner.
  - Stop rule: The spend or result that pauses the test. Hope is not a stop rule.
  - Landing page: Point to the page review if the page is not ready. Do not buy traffic to a confused page.
anti:
  - Ads that overpromise the page.
  - No stop rule.
  - Declaring a winner on a handful of clicks.
example: A team wants to scale spend after 12 clicks because one ad 'feels better'.
example_out: A brief with a stop rule and a minimum evidence line before scale, plus a claim check against the page.
related:
  - landing-page-cro
  - marketing-experiment

== abm-play | Account-Based Play ==
job: Design an account-based play for a short list of named accounts, with a reason for each account.
artifact: account-based play
triggers:
  - ABM
  - account based marketing
  - target account campaign
  - named accounts
inputs:
  - The named accounts and why they fit
  - The buyer role
  - The offer
  - Sales ownership
steps:
  - Short list: A handful of accounts with a fit reason. A thousand-account 'ABM' list is just a list.
  - Reason: Why this account, why now, from evidence the user has. Do not invent intent scores.
  - Offer: Something useful to that buyer's job, not a generic newsletter.
  - Sales pact: A named seller owns the follow-up. Marketing does not spray and disappear.
  - Personalization limits: Use public, relevant facts. No creepy personal details.
  - Readout: What will be reviewed after the plays run. Meetings accepted is a clearer signal than impressions.
anti:
  - Fake personalization.
  - A huge list with no seller owner.
  - Invented intent data.
example: Marketing built a 2,000-account ABM list from a bought spreadsheet and wants custom gifts for all of them.
example_out: A play that cuts to a short evidenced list, assigns sellers, and bans creepy personalization.
related:
  - account-plan
  - campaign-brief

== pr-pitch | PR Pitch ==
job: Draft a press pitch that has news, a real spokesperson, and no inflated claims.
artifact: press pitch
triggers:
  - press pitch
  - PR pitch
  - media pitch
  - reporter email
inputs:
  - The news
  - Why a reader would care
  - Spokesperson
  - Facts that can be checked
steps:
  - News test: What is new, and why now. A product description is not news by itself.
  - Reader: Which reporter's audience would care, in the user's words. Do not invent a relationship with a journalist.
  - Facts: Every number is checkable. Remove the rest.
  - Spokesperson: A named person who can speak on the record. No fake quotes.
  - Ask: A short interview or a factual briefing, not a demand for coverage.
  - Honesty: No embargo games the user does not understand, and no misleading exclusives.
anti:
  - Fake quotes.
  - Invented reporter relationships.
  - A pitch with no news.
example: A founder wants a pitch saying the company 'leads the market' with no data and no spokesperson.
example_out: A pitch that removes the leadership claim, requires a spokesperson, and states only checkable news.
related:
  - marketing-claims-review
  - corporate-narrative

== analyst-briefing | Analyst Briefing ==
job: Prepare an analyst or reviewer briefing that separates roadmap from shipped product.
artifact: analyst briefing notes
triggers:
  - analyst briefing
  - reviewer briefing
  - industry analyst prep
  - briefing notes
inputs:
  - The questions they are likely to ask
  - Shipped facts
  - Roadmap items that must be labeled
  - Proof
steps:
  - Shipped versus planned: Two lists. Never let planned items sit in the shipped list.
  - Proof pack: The metrics and customer evidence cleared for sharing.
  - Answers: Short answers to likely questions, including where the product is a poor fit.
  - Claims: Remove anything the claims review would block.
  - Follow-up: What you will send after, and what you will not send because it is unverified.
  - Tone: Brief and precise. No hype adjectives standing in for facts.
anti:
  - Roadmap presented as shipped.
  - Hiding the poor-fit segment.
  - Unverified metrics in the leave-behind.
example: A briefing deck shows a beta feature in the current architecture diagram with no label.
example_out: Notes that label the beta, move it out of the shipped list, and include the poor-fit segment.
related:
  - positioning-statement
  - marketing-claims-review

== marketing-attribution | Marketing Attribution Review ==
job: Review an attribution claim so the team does not confuse a tracking rule with causality.
artifact: attribution review
triggers:
  - marketing attribution
  - which channel works
  - multi-touch attribution
  - campaign ROI
inputs:
  - The attribution rule they use
  - The data they actually have
  - The decision they want to make
  - Known tracking gaps
steps:
  - Name the rule: First touch, last touch, or another rule they stated. A rule is not the truth.
  - Tracking gaps: What is untracked. Those gaps bound the claim.
  - Decision fit: Say whether the data can support the budget decision they want to make. If not, say what it can support.
  - Incrementality: If they have no holdout or other comparison, do not call a channel causal. Call it correlated under their rule.
  - Recommendation: A measurement improvement or a cautious budget test. Not a false ROI.
  - Language: Rewrite any sentence that says 'this channel created revenue' unless their design supports it.
anti:
  - Treating last touch as causality.
  - Ignoring untracked deals.
  - A false ROI number.
example: A team wants to cut content because last-touch credits it with little revenue, while sales says content starts most conversations.
example_out: A review that refuses the causal cut, names the tracking gap, and proposes a cleaner test.
related:
  - marketing-experiment
  - executive-insight

== offer-design | Offer Design ==
job: Design an offer with a clear value, a price logic the user supplied, and terms a customer can understand.
artifact: offer design
triggers:
  - design an offer
  - promotional offer
  - packaging offer
  - lead magnet review
inputs:
  - The audience
  - What they get
  - The price or exchange
  - Constraints from finance or delivery
steps:
  - Value: What the customer receives in concrete terms.
  - Exchange: What you ask in return: money, time, or a meeting. Say it plainly.
  - Eligibility: Who the offer is for and when it ends, if it ends. No fake end date.
  - Delivery: Confirm the team can fulfill it. Marketing cannot offer what delivery cannot do.
  - Terms: The conditions a reasonable customer must see before accepting.
  - Measurement: What acceptance means, and what would make you retire the offer.
anti:
  - Hidden conditions.
  - Fake end dates.
  - An offer operations cannot fulfill.
example: A campaign offers a free onboarding package that customer success says it cannot staff.
example_out: An offer that either cuts the promise or waits until staffing is real, with visible terms.
related:
  - pricing-packaging
  - campaign-brief

== community-program | Community Program ==
job: Design a community program with a member job-to-be-done, moderation, and no vanity member count.
artifact: community program brief
triggers:
  - community program
  - user group
  - community strategy
  - forum plan
inputs:
  - Why members would participate
  - Who will moderate
  - The offer to members
  - Topics that are out of bounds
steps:
  - Member job: What a member can do in the community that they cannot do alone. If the answer is 'hear from us', it is a newsletter, not a community.
  - Moderation: A named moderator and a simple code of conduct. No program without moderation.
  - Programming: A small rhythm of useful sessions. Do not promise daily activity you cannot host.
  - Measures: Quality of participation, not a vanity member total.
  - Safety: How harassment and spam are handled. No doxxing, no scraping members.
  - Honesty: Do not promise customers influence you will not give them.
anti:
  - A community that is only a broadcast channel.
  - No moderator.
  - Scraping member data for ads.
example: Leadership wants a community so marketing can email the members every day.
example_out: A brief that either redesigns it around a member job or calls it a newsletter, with moderation required for a real community.
related:
  - newsletter-editor
  - brand-voice-guide

== partner-co-marketing | Partner Co-Marketing ==
job: Plan a co-marketing activity with shared claims, shared approval, and no borrowed credibility.
artifact: co-marketing plan
triggers:
  - co-marketing
  - partner webinar
  - joint campaign
  - partner launch
inputs:
  - The partner and the joint offer
  - Approval path on both sides
  - Claims each side can make
  - The audience
steps:
  - Joint offer: What is actually being offered together. A logo swap is not a plan.
  - Claims: Each claim has an owner who can substantiate it. Neither side invents the other's metrics.
  - Approval: Both sides approve public copy. Build the time into the plan.
  - Audience: Whose audience is being asked, and whether that use is permitted. Do not assume list sharing is allowed.
  - Roles: Who builds, who speaks, who follows up.
  - Exit: What happens to leads and to the content after the event, in plain language.
anti:
  - Using a partner's logo without approval.
  - Inventing the partner's results.
  - Assuming you may email their list.
example: A team drafted a joint post that includes the partner's revenue and has not asked the partner.
example_out: A plan that strips the unapproved revenue claim and adds a written approval step before anything is published.
related:
  - pr-pitch
  - campaign-brief

== creative-brief | Creative Brief ==
job: Brief a designer or writer so they can make the piece without guessing the strategy.
artifact: creative brief
triggers:
  - creative brief
  - design brief
  - copy brief
  - brief a designer
inputs:
  - The audience and the action
  - The single message
  - Mandatories and brand limits
  - Examples of work they like or dislike
steps:
  - Job of the piece: What the reader should think, feel, or do. Pick the do.
  - Message: One message. Supporting points are labeled supporting.
  - Mandatories: Legal lines, logos, and words that must appear, supplied by the user. Do not invent legal lines.
  - Constraints: Format, size, and deadline.
  - References: What good looks like, and what to avoid, with a reason.
  - Done: How the draft will be judged, so review is not a taste lottery.
anti:
  - A brief that is a mood with no message.
  - Hidden mandatories that appear at the final review.
  - Invented legal disclaimers.
example: A designer received 'make it pop' and a deadline, with the offer still undecided.
example_out: A brief that blocks production until the offer and the single message are written.
related:
  - campaign-brief
  - design-handoff

== marketing-experiment | Marketing Experiment ==
job: Design a marketing experiment with a hypothesis, a single change, and a decision rule.
artifact: experiment brief
triggers:
  - marketing experiment
  - A/B test
  - growth test
  - what should we test
inputs:
  - The hypothesis
  - The single change
  - The event that measures it
  - The sample or spend available
steps:
  - Hypothesis: If we change X for audience Y, event Z will move, because of a reason you can state.
  - One change: Extra changes void the learning. Park them.
  - Decision rule: What result would scale, iterate, or stop the idea. Write it before the test.
  - Sample honesty: If the available traffic cannot support the decision, say the test will be directional only.
  - Ethics: No experiment that hides price, consent, or material terms.
  - Readout: A date and an owner. An unread test is a hobby.
anti:
  - Testing five changes at once.
  - A decision rule written after seeing the data.
  - Dark-pattern experiments.
example: A team wants to test a new headline, a new price, and a new form in one week and then 'see what happens'.
example_out: A brief with one change, a pre-written decision rule, and a note that the sample may only be directional.
related:
  - experiment-design
  - landing-page-cro

== newsletter-editor | Newsletter Editor ==
job: Edit a newsletter so each issue has one idea, true links, and a reason to exist.
artifact: newsletter edit
triggers:
  - edit a newsletter
  - newsletter review
  - email newsletter
  - company newsletter
inputs:
  - The draft
  - The reader
  - The one idea
  - Links and claims
steps:
  - Reason: Why this issue exists this week. If there is no reason, recommend skipping the send.
  - One idea: Cut items that do not serve it. A link dump is a finding.
  - Claims and links: Check that each link matches the description and each claim has a source. Do not invent a quote.
  - Subject line: It matches the content. No bait.
  - Skim: A reader on a phone can see the point in the first lines.
  - Ask: At most one ask, clearly marked.
anti:
  - A subject line that misleads.
  - Broken or misdescribed links left as an exercise.
  - A weekly send with nothing to say.
example: A draft newsletter has seven unrelated links and a subject line promising a major announcement that is not in the body.
example_out: An edit that either adds the real announcement or rewrites the subject, and cuts the issue to one idea.
related:
  - email-lifecycle
  - brand-voice-guide

== category-design | Category Narrative ==
job: Pressure-test a category narrative so it teaches the buyer a real shift, not a made-up adjective.
artifact: category narrative review
triggers:
  - category design
  - category narrative
  - create a category
  - market category
inputs:
  - The shift the buyer is experiencing
  - The old way
  - Evidence the shift is real
  - The company's right to speak
steps:
  - Shift: Describe the buyer's change in their language. A new adjective is not a category.
  - Old way: What they do today, fairly. Do not caricature customers.
  - Evidence: Signs the shift is happening outside the company's slide. If the only evidence is the slide, call it a hypothesis.
  - Right to speak: Why this company is a credible teacher of the shift. A narrative without credibility is an ad.
  - Language: A name the buyer can use in a meeting. If they would not say it, it is internal.
  - Restraint: Do not tell the team to 'own the category' as a fact. Recommend a teaching plan instead.
anti:
  - A coined adjective with no buyer shift.
  - Declaring category ownership.
  - Mocking the customer's current tools.
example: A startup wants to announce it created a new category because it added an AI button.
example_out: A review that rejects the announcement, restates the missing buyer shift, and proposes a hypothesis test instead.
related:
  - positioning-statement
  - corporate-narrative
'''
)]
