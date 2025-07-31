## Test Automation Project
To ensure that the Insider homepage, navigation, and QA job listings function as expected.
The test validates that listings filtered by location and department are shown correctly and
that "View Role" redirects to the application form.

---

### Test Steps
1. Visit https://useinsider.com/ and check if the Insider homepage is successfully
opened.
2. Click the “Company” menu from the navigation bar, then select “Careers”. Verify
that the Careers page is opened and the following sections are visible: Locations,
Teams, and Life at Insider.
3. Go to https://useinsider.com/careers/quality-assurance/
Click “See all QA jobs”
Filter jobs by Location: Istanbul, Turkey and Department: Quality Assurance
Verify that job listings are displayed
4. For each listed job, check that:
○ The Position title contains “Quality Assurance”
○ The Department is “Quality Assurance”
○ The Location is “Istanbul, Turkey”
5. Click the “View Role” button for a job and confirm that it redirects to the Lever
application form page.
