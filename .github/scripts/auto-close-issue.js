const fs = require('fs');
const path = require('path');

module.exports = async ({ github, context }) => {
  const membersPath = path.join(process.env.GITHUB_WORKSPACE, '.github', 'config', 'members.json');
  const MEMBERS = JSON.parse(fs.readFileSync(membersPath, 'utf-8'));
  console.log(`참가자 목록: ${MEMBERS.join(', ')}`);

  const pr = context.payload.pull_request;
  const body = pr.body || '';

  const issueLineMatch = body.match(/^issue:\s*(.+)$/im);
  if (!issueLineMatch) {
    console.log("Error: Can't find issue numbers from PR");
    return;
  }

  const issueNumbers = [...issueLineMatch[1].matchAll(/#(\d+)\b/g)]
    .map(m => parseInt(m[1]));
  if (issueNumbers.length === 0) {
    console.log("Error: Can't find issue numbers from issue line");
    return;
  }
  console.log(`connected Issue: ${issueNumbers.map(n => '#' + n).join(', ')}`);

  for (const issueNum of issueNumbers) {
    const timeline = await github.paginate(
      github.rest.issues.listEventsForTimeline,
      {
        owner: context.repo.owner,
        repo: context.repo.repo,
        issue_number: issueNum,
        per_page: 100,
      }
    );

    const linkedPRNumbers = [
      ...new Set(
        timeline
          .filter(e => e.event === 'cross-referenced' && e.source?.issue?.pull_request)
          .map(e => e.source.issue.number)
      )
    ];

    if (linkedPRNumbers.length === 0) {
      console.log(`Issue #${issueNum}: There's no connected PR. continue`);
      continue;
    }

    const results = await Promise.all(
      linkedPRNumbers.map(async num => {
        const { data } = await github.rest.pulls.get({
          owner: context.repo.owner,
          repo: context.repo.repo,
          pull_number: num,
        });
        return {
          number: num,
          author: data.user.login,
          merged: data.merged,
        };
      })
    );

    const mergedAuthors = results.filter(r => r.merged).map(r => r.author);
    const notSubmitted = MEMBERS.filter(m => !mergedAuthors.includes(m));

    if (notSubmitted.length === 0) {
      await github.rest.issues.update({
        owner: context.repo.owner,
        repo: context.repo.repo,
        issue_number: issueNum,
        state: 'closed',
      });

      await github.rest.issues.createComment({
        owner: context.repo.owner,
        repo: context.repo.repo,
        issue_number: issueNum,
        body: `모든 참가자의 PR이 merge되었습니다. Issue를 자동으로 닫습니다.`
      });
      console.log(`Issue #${issueNum} closed`);
    } else {
      console.log(`Issue #${issueNum}: 미완료 멤버 ${notSubmitted.join(', ')} 있음, 대기`);
    }
  }
};
