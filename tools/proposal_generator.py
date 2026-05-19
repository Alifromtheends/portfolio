#!/usr/bin/env python3
"""
Freelance Proposal Generator
============================
Generates professional project proposals and simple contracts.
Use this to respond to client inquiries in under 2 minutes.

Usage:
    python3 proposal_generator.py

Then answer the prompts. The proposal saves as a .md file you can
send directly to clients or convert to PDF.
"""

import datetime
import os
import re


def slugify(text):
    return re.sub(r'[^\w]+', '-', text.lower()).strip('-')


def generate_proposal():
    print("═" * 50)
    print("  FREELANCE PROPOSAL GENERATOR")
    print("═" * 50)
    print()

    # Collect inputs
    client_name = input("Client name: ").strip()
    project_name = input("Project name/title: ").strip()
    scope = input("Project scope (1-2 sentences): ").strip()
    deliverables = input("Key deliverables (comma-separated): ").strip()
    timeline = input("Timeline (e.g., '2 weeks', 'March 15'): ").strip()
    price = input("Price (e.g., '2,500', '1,500/week'): ").strip()
    payment_terms = input("Payment terms [50/50]: ").strip() or "50/50"
    your_name = input("Your name [Ali Bulatsalamov]: ").strip() or "Ali Bulatsalamov"

    # Parse deliverables
    items = [d.strip() for d in deliverables.split(",") if d.strip()]
    deliverables_md = "\n".join(f"- {item}" for item in items)

    # Parse payment terms
    if payment_terms == "50/50":
        payment_text = "50% upfront to begin work, 50% upon completion"
    elif payment_terms == "100":
        payment_text = "100% upfront"
    elif payment_terms == "milestone":
        payment_text = "Payment per milestone, invoiced upon completion of each phase"
    else:
        payment_text = payment_terms

    today = datetime.date.today().strftime("%B %d, %Y")
    filename = f"proposal-{slugify(project_name)}-{today.replace(' ', '-').lower()}.md"

    proposal = f"""# Project Proposal: {project_name}

**Prepared for:** {client_name}  
**Prepared by:** {your_name}  
**Date:** {today}

---

## 1. Project Overview

{scope}

## 2. Deliverables

{deliverables_md}

## 3. Timeline

**Estimated completion:** {timeline}

A detailed milestone schedule will be shared upon project kickoff.

## 4. Investment

**Total project fee:** ${price}

**Payment terms:** {payment_text}

**Payment methods:** Bank transfer, PayPal, or Wise

## 5. What Happens Next

1. **Approve this proposal** — Reply with your approval or any revisions
2. **Sign & send deposit** — I'll send an invoice for the upfront payment
3. **Kickoff call** — 30-minute alignment call to confirm details
4. **Development begins** — You'll receive progress updates every 2-3 days

## 6. Terms

- **Revisions:** Includes up to 3 revision rounds per major deliverable
- **Communication:** Slack, Discord, or email — your choice
- **Code ownership:** Full source code ownership transfers upon final payment
- **Confidentiality:** All project details remain strictly confidential
- **Start date:** Within 48 hours of signed proposal + deposit

---

**Approved by:**

Client Name: _________________________ Date: _______________

{your_name}: _________________________ Date: _______________

---

*Questions? Reply to this proposal or email me directly.*
"""

    with open(filename, "w") as f:
        f.write(proposal)

    print()
    print("═" * 50)
    print(f"  ✓ Proposal saved: {filename}")
    print("═" * 50)
    print()
    print("You can:")
    print("  • Send the .md file directly to clients")
    print("  • Convert to PDF:  pandoc filename.md -o filename.pdf")
    print("  • Open in any text editor for tweaks")
    print()


def generate_contract():
    print("═" * 50)
    print("  FREELANCE CONTRACT GENERATOR")
    print("═" * 50)
    print()

    client_name = input("Client name: ").strip()
    project_name = input("Project name: ").strip()
    scope = input("Scope summary: ").strip()
    price = input("Total fee: ").strip()
    timeline = input("Timeline: ").strip()
    your_name = input("Your name [Ali Bulatsalamov]: ").strip() or "Ali Bulatsalamov"

    today = datetime.date.today().strftime("%B %d, %Y")
    filename = f"contract-{slugify(project_name)}-{today.replace(' ', '-').lower()}.md"

    contract = f"""# Freelance Services Agreement

**This Agreement is made on:** {today}

**Between:**
- **Contractor:** {your_name}
- **Client:** {client_name}

---

## 1. Services

Contractor agrees to provide the following services:

{scope}

## 2. Compensation

**Total Fee:** ${price}

**Payment Schedule:**
- 50% deposit upon signing this agreement
- 50% upon project completion and client approval

## 3. Timeline

**Project Duration:** {timeline}

Contractor will begin work within 48 hours of receiving the signed agreement and deposit.

## 4. Intellectual Property

Upon full payment, all work product, code, designs, and deliverables become the sole property of the Client. Contractor retains the right to display the work in their portfolio unless otherwise agreed in writing.

## 5. Revisions

This agreement includes up to 3 rounds of revisions per major deliverable. Additional revisions will be billed at the Contractor's standard hourly rate.

## 6. Termination

Either party may terminate this agreement with 7 days written notice. If terminated by Client after work has begun, Client pays for all work completed to date. If terminated by Contractor, all deposits and completed work fees are refunded pro-rata.

## 7. Confidentiality

Contractor agrees to keep all Client information, business details, and project specifics confidential. This obligation survives the termination of this agreement.

## 8. Limitation of Liability

Contractor's total liability shall not exceed the total fee paid under this agreement. Contractor is not liable for indirect, incidental, or consequential damages.

## 9. Governing Law

This agreement shall be governed by the laws of [State/Country].

## 10. Entire Agreement

This document constitutes the entire agreement between the parties and supersedes all prior negotiations, representations, and agreements.

---

**Client Signature:** _________________________ Date: _______________

**Contractor Signature:** {your_name} _________________________ Date: _______________
"""

    with open(filename, "w") as f:
        f.write(contract)

    print()
    print("═" * 50)
    print(f"  ✓ Contract saved: {filename}")
    print("═" * 50)
    print()


def main():
    print()
    print("Choose document type:")
    print("  1) Project Proposal (faster, friendlier)")
    print("  2) Simple Contract (more formal)")
    print()
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        generate_proposal()
    elif choice == "2":
        generate_contract()
    else:
        print("Invalid choice. Run again.")


if __name__ == "__main__":
    main()
