#!/usr/bin/env python3
"""Generates the static pages for onekcpropertygroup.com from a shared shell."""

import os

SITE = "One KC Property Group, LLC"
EMAIL = "support@onekcpropertygroup.com"
PHONE = "(913) 608-7312"
PHONE_TEL = "+19136087312"

BRAND_MARK = """<svg class="brand-mark" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="One KC Property Group">
        <defs>
          <linearGradient id="okcMark" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#5fb0f2"/>
            <stop offset="55%" stop-color="#2f8ae4"/>
            <stop offset="100%" stop-color="#0f5aa8"/>
          </linearGradient>
        </defs>
        <path d="M24 3.2 46 20.4v21.2a3.2 3.2 0 0 1-3.2 3.2H5.2A3.2 3.2 0 0 1 2 41.6V20.4Z" fill="url(#okcMark)"/>
        <path d="M24 3.2 46 20.4H2Z" fill="#ffffff" opacity=".16"/>
        <circle cx="24" cy="25.4" r="4.3" fill="#ffffff"/>
        <path d="M22.1 28.4h3.8l1.1 8.4a1 1 0 0 1-1 1.1h-4a1 1 0 0 1-1-1.1Z" fill="#ffffff"/>
      </svg>"""

FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 48 48'%3E"
    "%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='1' y2='1'%3E"
    "%3Cstop offset='0%25' stop-color='%235fb0f2'/%3E"
    "%3Cstop offset='100%25' stop-color='%230f5aa8'/%3E"
    "%3C/linearGradient%3E%3C/defs%3E"
    "%3Cpath d='M24 3.2 46 20.4v21.2a3.2 3.2 0 0 1-3.2 3.2H5.2A3.2 3.2 0 0 1 2 41.6V20.4Z' fill='url(%23g)'/%3E"
    "%3Ccircle cx='24' cy='25.4' r='4.3' fill='%23fff'/%3E"
    "%3Cpath d='M22.1 28.4h3.8l1.1 8.4a1 1 0 0 1-1 1.1h-4a1 1 0 0 1-1-1.1Z' fill='%23fff'/%3E"
    "%3C/svg%3E"
)

NAV = [
    ("index.html", "Home"),
    ("requirements.html", "Application Requirements"),
    ("faq.html", "FAQ"),
    ("about.html", "About Us"),
    ("contact.html", "Contact"),
]


def shell(page_file, title, description, body):
    nav_items = "\n".join(
        '        <li><a href="{href}"{cls}>{label}</a></li>'.format(
            href=href,
            cls=' class="active"' if href == page_file else "",
            label=label,
        )
        for href, label in NAV
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | One KC Property Group</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title} | One KC Property Group">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#eff7fe">
<link rel="stylesheet" href="styles.css?v=2">
<link rel="icon" href="{FAVICON}">
</head>
<body>

<div class="topbar">
  <div class="wrap">
    <span><a href="mailto:{EMAIL}">{EMAIL}</a></span>
    <span><a href="tel:{PHONE_TEL}">{PHONE}</a></span>
  </div>
</div>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">
      {BRAND_MARK}
      <span class="brand-text">
        <span class="brand-name">One KC Property Group</span><br>
        <span class="brand-sub">Kansas City Rentals</span>
      </span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="main-nav">Menu</button>
    <nav class="main-nav" id="main-nav">
      <ul>
{nav_items}
      </ul>
    </nav>
  </div>
</header>

{body}

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h4>One KC Property Group</h4>
        <p style="margin:0">A family-owned property management company serving the Kansas City metro since 2020.</p>
      </div>
      <div>
        <h4>Pages</h4>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="requirements.html">Application Requirements</a></li>
          <li><a href="faq.html">FAQ</a></li>
          <li><a href="about.html">About Us</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> {SITE}. All rights reserved.</span>
      <span class="eho">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>
        Equal Housing Opportunity
      </span>
    </div>
  </div>
</footer>

<script>
  document.getElementById('year').textContent = new Date().getFullYear();
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('main-nav');
  toggle.addEventListener('click', function () {{
    var open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }});
</script>

</body>
</html>
"""


# --------------------------------------------------------------------------
# Page bodies
# --------------------------------------------------------------------------

HOME = f"""
<div class="hero">
  <div class="wrap">
    <h1>Quality rental homes across the Kansas City metro.</h1>
    <p>One KC Property Group is a family-owned property management company. We keep our
    process simple and our expectations clear, so you know exactly what it takes to
    qualify before you apply.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="requirements.html">Application Requirements</a>
      <a class="btn btn-ghost" href="contact.html">Contact Us</a>
    </div>
  </div>
</div>

<section>
  <div class="wrap">
    <h2>Everything you need before you apply</h2>
    <p class="lede">Our requirements are published up front &mdash; income, credit, pets, deposits
    and the reasons an application can be denied. Read through before submitting so there
    are no surprises.</p>
    <div class="cards">
      <div class="card">
        <h3>Application Requirements</h3>
        <p>Application fee, proof of income, credit score bands, rental history, security
        deposit, pets, renters insurance and disqualifying factors.</p>
        <a href="requirements.html">View requirements &rarr;</a>
      </div>
      <div class="card">
        <h3>Frequently Asked Questions</h3>
        <p>How long review takes, why there is an application fee, deposits, move-in
        walkthroughs and what condition the home will be in.</p>
        <a href="faq.html">Read the FAQ &rarr;</a>
      </div>
      <div class="card">
        <h3>About Us</h3>
        <p>A family-owned business since 2020, managing homes for local owners and renting
        to residents across the metro.</p>
        <a href="about.html">Learn about us &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2>The short version</h2>
    <div class="cards cards-4">
      <div class="card">
        <span class="stat">$44</span>
        <h3>Per applicant</h3>
        <p>Non-refundable application fee, due at submission. Everyone 18 or older applies
        separately. No administration or lease preparation fees.</p>
      </div>
      <div class="card">
        <span class="stat">3&times; rent</span>
        <h3>Income requirement</h3>
        <p>Verifiable gross household income must be at least three times the monthly rent,
        supported by paystubs, bank statements or tax returns.</p>
      </div>
      <div class="card">
        <span class="stat">600+</span>
        <h3>Credit score</h3>
        <p>Scores from 600&ndash;639 may be considered with a double deposit. Below 600 is
        disqualified.</p>
      </div>
      <div class="card">
        <span class="stat">12 months</span>
        <h3>Minimum lease</h3>
        <p>A longer term may be presented for leases starting in winter months. Lease terms
        are non-negotiable.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <h2>Questions about a property?</h2>
    <p>Reach out and we will get back to you. We are happy to walk you through the
    application process before you pay a fee.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="mailto:{EMAIL}">Email Us</a>
      <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{PHONE}</a>
    </div>
  </div>
</section>
"""


REQUIREMENTS = """
<div class="page-head">
  <div class="wrap">
    <h1>Application Requirements</h1>
    <p>Please read these requirements in full before submitting an application. Application
    fees are non-refundable.</p>
  </div>
</div>

<section>
  <div class="wrap content">

    <div class="block">
      <h2>Application Fee</h2>
      <ul>
        <li>Each application must be submitted with a <strong>non-refundable</strong>
        application fee, which is due at the time of submission.</li>
        <li><strong>$44.00</strong> application fee per person.</li>
        <li>Separate applications must be filled out for each occupant 18 years of age or older.</li>
        <li>There are no additional fees, such as administration or lease preparation fees.</li>
      </ul>
    </div>

    <div class="block">
      <h2>Proof of Income</h2>
      <p>To qualify, the household must have a verifiable gross income equal to or greater
      than <strong>3 times</strong> the monthly rent.</p>
      <p>The following are required with your application:</p>
      <ul>
        <li>Two (2) most recent paystubs, or two (2) most recent bank statements.</li>
        <li>If self-employed, last 2 years of tax returns (business &amp; personal).</li>
        <li>Copy of a valid government-issued photo ID.</li>
      </ul>
      <div class="note"><strong>Note:</strong> If other income is used for qualification
      purposes &mdash; such as but not limited to investments, pension, Social Security,
      retirement, alimony, child support or maintenance &mdash; supporting documentation such
      as account statements, divorce decrees or court orders must be provided.</div>
    </div>

    <div class="block">
      <h2>Credit Score</h2>
      <p>To qualify, residents must have a minimum credit score of <strong>600</strong>.</p>
      <table class="credit">
        <thead>
          <tr><th>Score</th><th>Outcome</th></tr>
        </thead>
        <tbody>
          <tr><td>400&ndash;599</td><td>Disqualified</td></tr>
          <tr><td>600&ndash;639</td><td>Considered with stipulations (double deposit)</td></tr>
          <tr><td>640&ndash;700</td><td>Considered</td></tr>
          <tr><td>700+</td><td>Highly considered</td></tr>
        </tbody>
      </table>
    </div>

    <div class="block">
      <h2>Rental History Verification</h2>
      <p>Previous landlord contact information is required. Failure to provide valid contact
      information may void the rental application.</p>
    </div>

    <div class="block">
      <h2>Security Deposit</h2>
      <ul>
        <li>A security deposit is not collected if the application is denied.</li>
        <li>The standard security deposit is equal to one month of rent and is required
        within <strong>48 hours</strong> of application approval.</li>
        <li>The security deposit is not considered rent, nor does it apply toward the rent at
        the first or the last month of the lease.</li>
        <li>All monies due must be collected prior to move-in unless otherwise agreed to in
        writing.</li>
        <li><strong>Tenant is required to move in within 25 days after signing the lease.</strong></li>
      </ul>
    </div>

    <div class="block">
      <h2>Pets</h2>
      <p><strong>Two pet maximum</strong> on any One KC Property Group managed property.</p>
      <p>Pet deposits are non-refundable up to $500. <strong>Any portion of the pet deposit
      exceeding $500 is refundable.</strong></p>
      <div class="pet-grid">
        <div class="pet">
          <strong>Dog over 35 lbs</strong>
          <span>$500 pet deposit (non-refundable)</span>
          <span>$50 monthly pet rent</span>
        </div>
        <div class="pet">
          <strong>Dog under 35 lbs</strong>
          <span>$300 pet deposit (non-refundable)</span>
          <span>$30 monthly pet rent</span>
        </div>
        <div class="pet">
          <strong>Cat</strong>
          <span>$250 pet deposit (non-refundable)</span>
          <span>$25 monthly pet rent</span>
        </div>
      </div>
      <h3>Service or Support Animal</h3>
      <p>We are happy to accept service and emotional support animals with proper
      documentation. All deposits and fees will be waived.</p>
    </div>

    <div class="block">
      <h2>Renters Insurance Requirements</h2>
      <p>Tenant is required to maintain renter&rsquo;s insurance, including general liability
      coverage in an amount not less than <strong>$100,000</strong>, at all times during the
      term of the lease and any renewal terms.</p>
    </div>

    <div class="block">
      <h2>Reasons for Disqualification</h2>
      <p>In addition to the application requirements listed above, your application is subject
      to denial if any of the following has happened to you in the past:</p>
      <ul>
        <li>Eviction within the past 5 years.</li>
        <li>Criminal, sex offense, and terrorist database check: we check these databases for
        all occupants over 18. We do not rent to any person required to register as a sex
        offender. Criminal backgrounds involving violent crimes, sex offenses and/or domestic
        violence and/or involving the possession or distribution of weapons are all grounds
        for denial of an application. An exception may be made for type and/or age of offense
        &mdash; please provide details at the time of application.</li>
        <li>Registered sex offender, or persons required to be registered as a sex offender.</li>
        <li>Unpaid debt or collection from a bank, lender, collection agency, previous property
        owner, manager or landlord-type agency as reported on the applicant&rsquo;s credit
        bureaus or otherwise disclosed.</li>
      </ul>
    </div>

    <div class="block">
      <h2>Other Things to Consider Before Applying</h2>
      <ul>
        <li>We require a minimum 12-month lease. In winter months a longer lease term may be
        presented.</li>
        <li>Application fees are non-refundable.</li>
        <li>We may conduct a periodic walkthrough of the interior and exterior of the property,
        which will be documented with photographs and shared with the property&rsquo;s landlord.</li>
        <li><strong>Late fees are non-negotiable and non-refundable. A $50.00 late fee is
        charged on the 5th, plus $5.00 each day after.</strong></li>
        <li>The terms of the lease are non-negotiable.</li>
        <li>Multiple applications may be received. We will not accept applications on a
        property that has already received a security deposit. If you were able to apply, the
        property was still available at that time. If multiple applications are received, all
        applications will be presented to the property owner for approval or denial. In all
        scenarios, you will be notified regardless of the outcome.</li>
      </ul>
    </div>

    <div class="block">
      <h2>Non-Discrimination Statement</h2>
      <p>One KC Property Group does not discriminate in the rental, lease, or negotiation for
      real property based on race, color, religion, sex, national origin, familial status, or
      handicap, and shall comply with all federal, state, and local laws concerning
      discrimination.</p>
      <p>One KC Property Group and the owners reserve the right to deny an applicant based on
      management or owner discretion so long as it is for a non-discriminatory reason.</p>
    </div>

  </div>
</section>

<section class="cta">
  <div class="wrap">
    <h2>Still have questions?</h2>
    <p>Our FAQ covers the review timeline, deposits, move-in walkthroughs and more.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="faq.html">Read the FAQ</a>
      <a class="btn btn-ghost" href="contact.html">Contact Us</a>
    </div>
  </div>
</section>
"""


FAQ = """
<div class="page-head">
  <div class="wrap">
    <h1>Frequently Asked Questions</h1>
    <p>Answers to the questions we hear most often from applicants and residents.</p>
  </div>
</div>

<section>
  <div class="wrap content">

    <details class="faq" open>
      <summary>How long does the application reviewing process take?</summary>
      <div class="answer">
        <p>The application reviewing process typically takes 2&ndash;3 business days after a
        completed application submission.</p>
      </div>
    </details>

    <details class="faq">
      <summary>Why is there an application fee?</summary>
      <div class="answer">
        <p>The application fee covers the cost of the credit report, background check, and
        income and employment verification. The screening process is handled by Stessa, and
        the application fee is paid directly to Stessa. We do not receive any portion of this
        fee.</p>
      </div>
    </details>

    <details class="faq">
      <summary>How much is the security deposit?</summary>
      <div class="answer">
        <p>The standard security deposit is equal to one month of rent and is required within
        48 hours of approval.</p>
        <p>All deposits and the first month&rsquo;s rent, or prorated rent, must be collected
        prior to move-in unless otherwise agreed to in writing.</p>
      </div>
    </details>

    <details class="faq">
      <summary>Will the move-in condition be documented?</summary>
      <div class="answer">
        <p>Yes. We will complete a move-in walkthrough at the time of your move-in. Photos and
        videos will be taken and shared with you. You may note any additional items and submit
        them within two weeks of your move-in date.</p>
      </div>
    </details>

    <details class="faq">
      <summary>Will the owner do any updating or extra cleaning before I move in?</summary>
      <div class="answer">
        <p>Each home is professionally cleaned before move-in and rented in &ldquo;as-is&rdquo;
        condition. The property will be in the same condition as shown during your viewing.
        Cosmetic repairs or updates are not included. Any maintenance concerns noticed at
        move-in can be submitted through the maintenance portal for review.</p>
      </div>
    </details>

    <details class="faq">
      <summary>Are there any additional monthly fees, such as a tenant benefit package, annual renewal fee, or administrative fee?</summary>
      <div class="answer">
        <p>No, we do not charge any additional fees unless they are outlined in the lease.</p>
      </div>
    </details>

  </div>
</section>

<section class="cta">
  <div class="wrap">
    <h2>Didn&rsquo;t find your answer?</h2>
    <p>Send us a note and we will get back to you.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="contact.html">Contact Us</a>
      <a class="btn btn-ghost" href="requirements.html">Application Requirements</a>
    </div>
  </div>
</section>
"""


ABOUT = """
<div class="page-head">
  <div class="wrap">
    <h1>About Us</h1>
    <p>A family-owned property management company serving the Kansas City metro since 2020.</p>
  </div>
</div>

<section>
  <div class="wrap content">
    <h2>Family owned since 2020</h2>
    <p class="lede">One KC Property Group, LLC is a family-owned and operated property
    management company. We started in 2020 with a straightforward idea: manage rental homes
    the way we would want our own managed &mdash; carefully, honestly, and without the
    surprise fees that have become common in this industry.</p>

    <p>Because we are family run, the person you speak with is the person handling your home.
    We keep our portfolio at a size we can genuinely stay on top of, which means applications
    get reviewed quickly, maintenance requests reach a real person, and owners hear from us
    before there is a problem rather than after.</p>

    <h3>How we work</h3>
    <div class="cards">
      <div class="card">
        <h3>Clear expectations</h3>
        <p>Our full application requirements are published on this site. You will know whether
        you qualify before you pay an application fee.</p>
      </div>
      <div class="card">
        <h3>No surprise fees</h3>
        <p>No administration fees, no lease preparation fees, and no monthly tenant benefit
        packages or renewal fees beyond what is written in your lease.</p>
      </div>
      <div class="card">
        <h3>Documented condition</h3>
        <p>Every home is professionally cleaned before move-in, and we complete a documented
        walkthrough with photos and video that we share with you.</p>
      </div>
      <div class="card">
        <h3>Fair housing</h3>
        <p>We comply with all federal, state and local fair housing laws and do not
        discriminate in the rental, lease or negotiation for real property.</p>
      </div>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <h2>Looking for a home, or need a manager for yours?</h2>
    <p>We would be glad to hear from you either way.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="contact.html">Get in touch</a>
    </div>
  </div>
</section>
"""


CONTACT = f"""
<div class="page-head">
  <div class="wrap">
    <h1>Contact Us</h1>
    <p>Questions about an application, a property, or managing your rental home? Reach out
    and we will get back to you.</p>
  </div>
</div>

<section>
  <div class="wrap content">
    <div class="contact-grid">
      <div class="contact-item">
        <div class="label">Email</div>
        <div class="value"><a href="mailto:{EMAIL}">{EMAIL}</a></div>
      </div>
      <div class="contact-item">
        <div class="label">Phone</div>
        <div class="value"><a href="tel:{PHONE_TEL}">{PHONE}</a></div>
      </div>
      <div class="contact-item">
        <div class="label">Service area</div>
        <div class="value">Kansas City metro</div>
      </div>
    </div>

    <h2 style="margin-top:46px">Before you contact us</h2>
    <p>Many questions are already answered on our
    <a href="requirements.html">Application Requirements</a> and
    <a href="faq.html">FAQ</a> pages &mdash; including application fees, income and credit
    requirements, pet policy, deposits and move-in timelines.</p>

    <div class="note">
      <strong>Applying for a home?</strong> Please read the application requirements in full
      first. Application fees are non-refundable, and each occupant 18 or older must submit a
      separate application.
    </div>
  </div>
</section>
"""


PAGES = [
    ("index.html", "Home", "One KC Property Group, LLC — a family-owned property management company renting quality homes across the Kansas City metro since 2020.", HOME),
    ("requirements.html", "Application Requirements", "Application fee, income, credit score, rental history, security deposit, pet policy and renters insurance requirements for One KC Property Group rentals.", REQUIREMENTS),
    ("faq.html", "FAQ", "Frequently asked questions about applying to rent a home with One KC Property Group, including review times, fees, deposits and move-in.", FAQ),
    ("about.html", "About Us", "One KC Property Group is a family-owned property management company serving the Kansas City metro since 2020.", ABOUT),
    ("contact.html", "Contact", "Contact One KC Property Group, LLC by email or phone about rental applications and property management in the Kansas City metro.", CONTACT),
]

out = os.path.dirname(os.path.abspath(__file__))

for filename, title, desc, body in PAGES:
    with open(os.path.join(out, filename), "w", encoding="utf-8") as fh:
        fh.write(shell(filename, title, desc, body))
    print("wrote", filename)

with open(os.path.join(out, "CNAME"), "w", encoding="utf-8") as fh:
    fh.write("onekcpropertygroup.com\n")
print("wrote CNAME")

with open(os.path.join(out, ".nojekyll"), "w", encoding="utf-8") as fh:
    fh.write("")
print("wrote .nojekyll")
