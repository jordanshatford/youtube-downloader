import type { UserConfig } from '@commitlint/types';

const configuration: UserConfig = {
  extends: ["@commitlint/config-conventional"],
  // Ignore dependabot commits (ref: https://github.com/dependabot/dependabot-core/issues/2445)
  ignores: [(commit) => /Signed-off-by: dependabot\[bot]/m.test(commit)]
}

export default configuration;
