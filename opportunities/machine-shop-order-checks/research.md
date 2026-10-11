# Machine-shop order checks — research

Current claim assessment: 2026-10-10  
Scope: Small commercial machining/job shops receiving customer orders and drawings by email. Readable practitioner accounts mainly concern the US and English-speaking shops; no country-wide demand claim.

## C001

**Claim:** Some shops spend effort sorting drawing versions and receive inconsistent customer paperwork.

**Assessment and confidence:** Moderate confidence that these experiences occurred as reported; low confidence about their current frequency in the proposed small-shop segment. [E001](#e001) and [E002](#e002) are older original discussions. [E007](#e007) is a partially retrieved price-mismatch account, useful as a lead rather than decisive corroboration. No incident, identity, or financial loss was independently verified.

**Contrary evidence:** Replies to E001 describe satisfactory shared-folder procedures and existing software. E002's main incident involved an undocumented physical change: comparing supplied files cannot discover a change absent from all of them.

**Next check:** Obtain a recent order where checking the supplied quote, purchase order and drawing would actually have exposed the mistake before release. Determine who checked it, time spent, and who bore any rework cost.

## C002

**Claim:** A small, separate order-checking product has a reason to be purchased alongside existing shop software.

**Assessment and confidence:** Unresolved. Paperless Parts already extracts revisions and supports drawing comparison ([E003](#e003), [E004](#e004)); generic order discrepancy checking also exists ([E006](#e006)). Satisfactory manual procedures are a substantial alternative. The potential distinction is a focused check across an incoming customer PO, accepted quote and drawing, with little setup. That is an offer hypothesis, not a verified missing feature.

**Next check:** Ask shops to demonstrate their actual process and existing software. Compare the proposed report with their current checks and a relevant existing product. A lack of supplier-side support in one buyer-side tool would not establish an unmet market.

## C003

**Claim:** An initial version can be tested without replacing the shop's ERP or controlling machinery.

**Assessment and confidence:** Plausible design inference, untested. Start with uploaded PDFs and an explicit checklist for part number, revision, quantities, units, price and dates; show source locations and uncertain matches for a human reviewer. Exclude automatic production approval. Drawing interpretation requires a knowledgeable machining/quality reviewer; reliable field extraction and line matching require real samples.

**Delivery and costs:** PDF parsing/OCR, document matching, revision history, review UI, file storage and export are initial work. Onboarding includes customer aliases and shop-specific review rules. Founder support would handle poor scans, absent revision numbers, multi-part files, and incorrect matches. Hosting, storage, OCR/model usage, customer acquisition, insurance/contracts and expert review remain unpriced. No schedule or total-cost estimate is supported. Drawings may have customer-specific handling restrictions that must be established with the shop before use.

## C004

**Claim:** There is a workable payer, recurring use and customer-access route.

**Assessment and confidence:** Unresolved. Owner/general manager or operations/quality lead is a possible sponsor; purchasing authority was not verified. A per-shop subscription with an order allowance and optional setup is a proposed model, with no accepted price. Sporadic mistakes might support occasional checks or a service instead of a subscription.

**Access:** NTMA chapter listings are a discovery route ([E008](#e008)); neither introductions nor permission to inspect documents exists. Public association membership may skew toward larger shops.

## E001

**Origin:** [Organizing programs, setup sheets and prints for shop access](https://www.practicalmachinist.com/forum/threads/organizing-programs-set-up-sheets-and-prints-for-shop-access.320529/), Practical Machinist; conceptdevelopers and replies; original practitioner discussion.

**Report/context:** The author, located in Garland, Texas, describes multiple programs for a part and time spent searching a scattered server. Replies suggest controlled folders, revision identifiers, and CIMCO; some report satisfactory folder procedures. The account concerns production files more directly than incoming PO checks.

**Dates:** Event unknown; published 2016-05-19, replies through 2016-06-01; retrieved 2026-10-10.  
**Claims/limits:** C001–C003. Old, self-reported, and not purchase evidence. Replies quoting the author are not extra observations. Original account and relevant replies read.

## E002

**Origin:** [Undocumented revision change and rework](https://www.reddit.com/r/Machinists/comments/vrs1fh/measure_twice_cut_once_discover_massive/), r/Machinists; judgemeordont and replies; original practitioner discussion.

**Report/context:** The author reports cutting splines according to a supplied drawing, then discovering an undocumented metric change; the part could be reworked and the customer would pay again. Replies describe old drawings reaching vendors and other drawing conflicts. Geography of the main author is unverified.

**Dates:** Event unknown; exact publication date unknown in the opened page, indexed approximately 2022; retrieved 2026-10-10.  
**Claims/limits:** C001 and C003. The principal incident cannot be assumed preventable by document comparison. Not evidence that the shop lost the quoted amount or would buy software. Relevant replies and author's clarification read.

## E003

**Origin:** [Paperless Parts quote setup workflow](https://www.paperlessparts.com/product-update/new-quote-setup-workflow/), vendor documentation.

**Report/context:** Describes forwarding RFQs, extracting part/revision identifiers and quantities, and reviewing suggestions beside source files. This is an existing adjacent capability, not a tested full PO-to-quote audit.

**Dates:** Event not applicable; publication date unknown; retrieved 2026-10-10.  
**Claims/limits:** C002–C003. First-party advertised behavior; current plan eligibility and runtime performance untested.

## E004

**Origin:** [Paperless Parts PDF viewer brief](https://www.paperlessparts.com/wp-content/uploads/pdf-viewer-solutions-brief.pdf), two-page vendor PDF.

**Report/context:** Documents visual comparison between drawing versions and records a vendor-selected positive account from Kyra Tillman of BTM Industries about PDF-based use.

**Dates:** Event/testimonial date unknown; publication unknown; retrieved 2026-10-10.  
**Claims/limits:** C002. Existing capability and satisfaction counterexample; testimonial is vendor-selected and was not independently checked.

## E005

**Origin:** [Paperless Parts pricing request](https://www.paperlessparts.com/pricing/), vendor offer page.

**Report/context:** Pricing is requested from the vendor; no numeric list price was available in the retrieved page.

**Dates:** Offer/publication date unknown; retrieved 2026-10-10.  
**Claims/limits:** C002 and C004. Cannot infer affordability, minimum contract, or price advantage for a new offer.

## E006

**Origin:** [OrderDiff](https://www.orderdiff.com/), vendor product, pricing and FAQ.

**Report/context:** Buyer-side PO versus supplier-confirmation checks are advertised. The FAQ says PDF support is not yet available, despite broader file wording. The retrieved Buyer plan displays $29/month, 150 checks, tax added; currency is localized and the dollar's ISO currency was not established.

**Dates:** Offer/publication date unknown; retrieved 2026-10-10.  
**Claims/limits:** C002 and C004. Supports existence of a lightweight substitute; supplier-facing machining revisions and actual performance untested. Do not convert the displayed amount or describe this as verified USD.

## E007

**Origin:** [Customer sends order with wrong price](https://practicalmachinist.com/forum/threads/customer-sends-order-with-wrong-price.226167/), Practical Machinist; expanded original-source search excerpts.

**Report/context:** Excerpts describe repeat orders at an outdated price and replies suggesting attaching the latest quote. Full original account and resolution could not be read.

**Dates:** Event unknown; search identifies replies dated 2011-05-24; retrieved/attempted 2026-10-10.  
**Claims/limits:** C001, weak supplementary lead only. Direct opening failed with cache miss and www variant with 402 Payment Required. Original context is incomplete.

## E008

**Origin:** [NTMA members](https://ntma.org/ntma-member/) and [NJ/PA chapter member listings](https://ntma-njpa.com/member/), association discovery pages.

**Report/context:** Search returned named machining businesses and public company routes; direct openings failed. No contacts were selected or contacted.

**Dates:** Listing/publication dates unknown; retrieved/attempted 2026-10-10.  
**Claims/limits:** C004. Search-discovered access route only; current listings and buyer fit need verification.

## Research still needed

Recent mistakes detectable from supplied documents; actual review time; existing-software coverage and satisfaction; willingness to share examples; authority and accepted price; order volume and continued value; extraction accuracy and expert review costs. Runtime testing, supplier quotes and customer interviews were **not performed**. Access failures and searches are in the [scouting run](../../scouting-runs/2026-10-10-open-discovery.md#search-trail-and-coverage).
