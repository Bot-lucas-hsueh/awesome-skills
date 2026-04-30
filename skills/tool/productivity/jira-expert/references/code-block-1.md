# jql Example

```
-- Complex filter: Issues assigned to me in current sprint
project = ENG AND sprint IN openSprints() AND assignee = currentUser() ORDER BY priority DESC

-- Epics with incomplete stories
project = ENG AND issuetype = Epic AND "Epic Status" != Done AND issueFunction in linkedIssuesOf("issue IN issuesInEpics()")

-- Issues updated in last week by specific user
project = ENG AND updatedBy(username) >= -7d AND updatedBy(username) <= 0d ORDER BY updated DESC

-- Stories with story points not estimated
project = ENG AND issuetype = Story AND "Story Points" IS EMPTY AND sprint IN openSprints()

-- Blocked issues across projects
project IN (ENG, DATA, PLATFORM) AND status = Blocked ORDER BY updated DESC

-- Issue velocity: completed stories per sprint
issuetype = Story AND status = Done AND sprint IN closedSprints() AND assignee = currentUser()
ORDER BY sprint DESC

-- Cross-project search with labels
labels IN (urgent, security) ORDER BY created DESC

-- Issues due this week
duedate <= 7d AND duedate >= 0d AND status NOT IN (Done, Closed) ORDER BY duedate ASC

-- Parent epic progress
issueFunction in linkedIssuesOf("key = ENG-123") AND issuetype IN (Story, Bug, Task)

-- Recently resolved with comments
status CHANGED TO Done AFTER -30d AND commentCount > 0 ORDER BY resolved DESC
```
