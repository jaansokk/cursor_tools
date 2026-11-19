# Web Design Checklist

A comprehensive checklist for creating user-centered, accessible, performant web interfaces.

---

## User-Centric Design

### Before Design
- [ ] Defined target user personas based on real data
- [ ] Identified primary user goals (what they want to accomplish)
- [ ] Mapped user journey from entry to conversion
- [ ] Researched competitor interfaces
- [ ] Gathered cross-functional input (UX, dev, sales, support)

### During Design
- [ ] Every major element serves a clear user need
- [ ] Content hierarchy matches user priorities
- [ ] Navigation reflects user mental models
- [ ] Error states guide users toward resolution
- [ ] Empty states provide helpful direction

---

## Information Hierarchy

### Visual Hierarchy
- [ ] Most important information is immediately visible
- [ ] Headlines grab attention before body text
- [ ] CTAs stand out from surrounding content
- [ ] Color, size, and position guide the eye naturally
- [ ] Whitespace creates clear groupings

### Content Structure
- [ ] Text is chunked into short, scannable paragraphs
- [ ] Bullet points used for lists and key information
- [ ] Headings accurately describe content below
- [ ] Important content is above the fold
- [ ] Progressive disclosure for complex information

---

## Navigation

### Primary Navigation
- [ ] Main nav limited to 5-7 items maximum
- [ ] Menu labels are clear and descriptive
- [ ] Current page is visually indicated
- [ ] Logo links to homepage
- [ ] Navigation is consistent across all pages

### Wayfinding
- [ ] Breadcrumbs for deep page structures
- [ ] Search functionality available site-wide
- [ ] Footer navigation for secondary links
- [ ] Clear back/escape paths from any page
- [ ] 404 page helps users find their way

### Mobile Navigation
- [ ] Hamburger menu or tab bar for mobile
- [ ] Touch targets are minimum 44×44px
- [ ] Navigation is reachable with one hand
- [ ] Important actions aren't hidden in menus

---

## Calls to Action

### Visibility
- [ ] Primary CTA is immediately visible above the fold
- [ ] CTAs have strong visual contrast
- [ ] Whitespace isolates CTAs from surrounding content
- [ ] Secondary CTAs are visually subordinate

### Copy
- [ ] Action-oriented language ("Get Started" not "Submit")
- [ ] First-person phrasing where appropriate ("Get My Free Trial")
- [ ] Specificity about what happens next
- [ ] Urgency or value proposition when relevant

### Placement
- [ ] Primary CTA in hero section
- [ ] CTAs repeated on long pages
- [ ] Relevant CTAs on internal pages
- [ ] Sticky CTA for critical conversions

---

## Typography & Readability

### Font Selection
- [ ] Body text uses highly readable font (not decorative)
- [ ] Display font has distinctive character
- [ ] Font pairing creates visual interest without conflict
- [ ] Maximum 2-3 font families used

### Text Styling
- [ ] Body text minimum 16px (1rem)
- [ ] Line height 1.5-1.7 for body text
- [ ] Maximum line length ~70 characters
- [ ] Sufficient paragraph spacing
- [ ] Text contrast ratio minimum 4.5:1

### Hierarchy
- [ ] Clear distinction between heading levels
- [ ] Consistent heading styles throughout
- [ ] Labels are distinguishable from body text
- [ ] Data uses appropriate monospace styling

---

## Visual Design

### Color
- [ ] Color palette limited to 3-5 colors
- [ ] One primary accent color
- [ ] Semantic colors for status (success, warning, error)
- [ ] Color is not the only indicator of meaning
- [ ] Sufficient contrast between all elements

### Consistency
- [ ] Consistent spacing system throughout
- [ ] Unified border radius approach
- [ ] Single depth strategy (borders OR shadows)
- [ ] Consistent icon style
- [ ] Reusable component patterns

### Branding
- [ ] Brand colors used consistently
- [ ] Logo placement follows conventions
- [ ] Visual style matches brand personality
- [ ] Tone is consistent across all copy

---

## Responsive Design

### Layout
- [ ] Mobile-first CSS approach
- [ ] Flexible grid system
- [ ] Content reflows naturally at breakpoints
- [ ] No horizontal scrolling at any viewport
- [ ] Critical content visible on all devices

### Touch
- [ ] Touch targets minimum 44×44px
- [ ] Adequate spacing between interactive elements
- [ ] No hover-dependent interactions on mobile
- [ ] Swipe gestures where appropriate

### Testing
- [ ] Tested on actual mobile devices
- [ ] Tested across major browsers
- [ ] Tested at common breakpoints (320, 375, 768, 1024, 1440)
- [ ] Tested in both orientations

---

## Performance

### Images
- [ ] Images compressed (WebP format preferred)
- [ ] Responsive images with srcset
- [ ] Lazy loading for below-fold images
- [ ] Appropriate image dimensions (not oversized)
- [ ] Alt text for all images

### Code
- [ ] CSS minified for production
- [ ] JavaScript deferred for non-critical scripts
- [ ] Unused CSS/JS removed
- [ ] Fonts subset if possible
- [ ] Third-party scripts audited

### Infrastructure
- [ ] CDN configured
- [ ] GZIP/Brotli compression enabled
- [ ] Browser caching configured
- [ ] Critical CSS inlined

### Metrics
- [ ] Largest Contentful Paint < 2.5s
- [ ] First Input Delay < 100ms
- [ ] Cumulative Layout Shift < 0.1
- [ ] Time to Interactive < 3.8s

---

## Accessibility (WCAG 2.1 AA)

### Perceivable
- [ ] All images have descriptive alt text
- [ ] Videos have captions
- [ ] Color contrast minimum 4.5:1 for text
- [ ] Text can be resized to 200% without loss
- [ ] No information conveyed by color alone

### Operable
- [ ] All functionality accessible via keyboard
- [ ] Focus states visible on all interactive elements
- [ ] No keyboard traps
- [ ] Skip links available
- [ ] Sufficient time for time-limited interactions

### Understandable
- [ ] Language attribute set on HTML
- [ ] Form inputs have associated labels
- [ ] Error messages are clear and helpful
- [ ] Consistent navigation across pages
- [ ] Instructions don't rely solely on sensory characteristics

### Robust
- [ ] Valid, semantic HTML
- [ ] ARIA labels where needed
- [ ] Tested with screen reader
- [ ] Custom controls have appropriate roles

---

## Trust & Credibility

### Social Proof
- [ ] Customer testimonials with names/photos
- [ ] Client logos (B2B)
- [ ] Case studies with specific results
- [ ] Star ratings and review counts
- [ ] User-generated content where appropriate

### Security
- [ ] SSL certificate (HTTPS)
- [ ] Security badges near checkout
- [ ] Clear privacy policy linked
- [ ] Trust badges for payments
- [ ] Contact information easily findable

### Transparency
- [ ] Pricing clearly visible
- [ ] No hidden fees or surprises
- [ ] Clear return/refund policies
- [ ] About page with real people
- [ ] Physical address if applicable

---

## Forms

### Design
- [ ] Form fields have visible labels
- [ ] Required fields clearly marked
- [ ] Inline validation with helpful messages
- [ ] Error states are clear and actionable
- [ ] Success confirmation after submission

### UX
- [ ] Minimal fields (only ask what's necessary)
- [ ] Logical field order
- [ ] Appropriate input types (email, tel, etc.)
- [ ] Autofill supported
- [ ] Progress indicator for multi-step forms

### Conversion
- [ ] Guest checkout option for e-commerce
- [ ] Save progress option for long forms
- [ ] Clear privacy statement
- [ ] Social login options where appropriate

---

## SEO

### Technical
- [ ] Unique, descriptive title tags (50-60 chars)
- [ ] Meta descriptions (150-160 chars)
- [ ] Proper heading hierarchy (one H1 per page)
- [ ] XML sitemap submitted
- [ ] Robots.txt configured

### Content
- [ ] Content addresses user search intent
- [ ] Keywords used naturally in content
- [ ] Internal linking to related content
- [ ] Alt text includes relevant keywords
- [ ] URLs are clean and descriptive

### Structure
- [ ] Schema markup implemented
- [ ] Canonical URLs set
- [ ] Mobile-friendly confirmed
- [ ] Page speed optimized
- [ ] Core Web Vitals passing

---

## Launch Checklist

### Pre-Launch
- [ ] All links tested and working
- [ ] Forms submitted and verified
- [ ] 404 page created
- [ ] Favicon and app icons added
- [ ] Open Graph/social meta tags set
- [ ] Analytics installed and verified
- [ ] Backup system configured

### Post-Launch
- [ ] Monitor for 404 errors
- [ ] Check analytics data flowing
- [ ] Submit sitemap to Google Search Console
- [ ] Test all user flows end-to-end
- [ ] Set up ongoing monitoring

---

## Continuous Improvement

### Analytics
- [ ] Track key conversion events
- [ ] Monitor bounce rates by page
- [ ] Analyze user flow through site
- [ ] Set up goal tracking
- [ ] Review regularly (weekly/monthly)

### Testing
- [ ] A/B test key pages and CTAs
- [ ] Gather user feedback via surveys
- [ ] Conduct usability testing periodically
- [ ] Monitor heatmaps and session recordings
- [ ] Iterate based on data
