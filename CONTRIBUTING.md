# Contributing Guidelines

Thank you for your interest in contributing to our project. Whether it's a bug report, new feature, correction, or additional
documentation, we greatly value feedback and contributions from our community.

Please read through this document before submitting any issues or pull requests to ensure we have all the necessary
information to effectively respond to your bug report or contribution.


## Reporting Bugs/Feature Requests

We welcome you to use the GitHub issue tracker to report bugs or suggest features.

When filing an issue, please check existing open, or recently closed, issues to make sure somebody else hasn't already
reported the issue. Please try to include as much information as you can. Details like these are incredibly useful:

* A reproducible test case or series of steps
* The version of our code being used
* Any modifications you've made relevant to the bug
* Anything unusual about your environment or deployment


## Contributing Code
The list below outlines the guidelines for submitting pull requests. Internal contributors adhere to these same guidelines when proposing changes, and we expect the same from community contributions:

1. The project is licensed under [MIT-0](https://github.com/aws/mit-0). Any code you submit will be released under this same license.

2. Code should adhere to the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide. However, if you're modifying an existing module and encounter discrepancies, prioritize consistency within the module.

3. While we value unit test coverage and code quality, we are not strictly enforcing them at this stage. However, as the project matures, you can expect these checks to be enforced and potentially become blockers for integrations. We encourage you to maintain high standards from the outset to ensure a smooth transition in the future.

4. Ensure you're working with the latest source from the `main` branch.
   
5. Before proposing changes, review open and recently merged pull requests to ensure the issue hasn't already been addressed.
   
6. If you're planning significant contributions, please open an issue for discussion beforehand. We value your time and wouldn't want it to go to waste.
   
7. Code should be compatible with Python 3.7 and newer versions.


### Prerequisite
As required by our security team, it's essential to install [git-secrets](https://github.com/awslabs/git-secrets) in your development environment. 
This prevents the inadvertent committing of credentials into the repository. Please follow the instructions [here](https://github.com/awslabs/git-secrets#installing-git-secrets) to install git-secretes.
If you have concerns regarding its requirement, kindly consult the maintainers. 


### Pull Request and Workflow
When making a contribution, please follow these guidelines:
 1. Fork the repository.
 2. Modify the code and please focus on the specific change you are contributing. If you also reformat all the code, it will be hard for us to focus on your change.
 3. Commit to your fork using clear commit messages following the below format: 

```bash
Short (50 characters or less) summary

After the 50 character summary and a blank line, you can include a body if necessary. Note that the 50 character summary does not end with any punctuation. Describe your changes in the imperative mood, e.g., "Add foo to bar", "Update foo component for bar", "Fix race condition for foo".

The body of the commit message can include:

* an explanation of the problem and what this change tries to solve.

* rationale behind the specific implementation

* alternatives considered and why they were discarded, if appropriate.

Please limit the line length in the body of a commit message to 80 characters or less.
```
 4. Ensure local tests pass. Send us a PR targeting the `main` branch.


 5. Your PR branch should be based off a recent commit of the main branch. Preferably the base commit for the PR should use the latest commit of main at the time the PR was created. This helps to ensure there are no merge conflicts or test failures when the PR is merged back to the develop branch.
 
 6. Make separate commits for logically separate changes. Avoid commits such as "update", "fix typo again", "more updates". Rebase your commits before submitting your PR to ensure they represent a logical change.
 
 7. Avoid merge commits in your PRs. If you want to pull in the latest changes from the main branch, rebase on top of the main branch instead of merging the main branch into your feature branch.

  8. Pay attention to any automated CI failures reported in the pull request, and stay involved in the conversation.

GitHub provides additional document on [forking a repository](https://help.github.com/articles/fork-a-repo/) and [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

### Example Git Workflow
```bash
# First, fork ELB-Doctor repository into your account.

# Clone the forked repository from your Github account and set up the remotes.
$ git clone https://github.com/<my-github-account>/elb-doctor
$ cd elb-doctor
$ git remote add upstream https://github.com/aws/elb-doctor.git
$ git fetch upstream
$ git merge upstream/main

# Set up the feature branch to make code changes
$ git checkout -b my-feature-branch

# Make the code change and add the change
$ git add path/to/the/file

# Make sure the commit message matches format described in the previous section
$ git commit -m "Add support for foo"

# Sync with the latest upstream changes before sending pull request: 
$ git fetch upstream
$ git rebase upstream/main

# When you're ready to send a PR, push the code back to origin in your account:
$ git push --set-upstream origin my-feature-branch

# Use the URL in the output to open a Pull request:
...
remote: Resolving deltas: 100% (57/57), completed with 4 local objects.
remote:
remote: Create a pull request for 'my-feature-branch' on GitHub by visiting:
remote:      https://github.com/<my-github-account>/elb-doctor/pull/new/my-feature-branch    <------ Open this URL in your browser
remote:
To https://github.com/<my-github-account>/elb-doctor
 * [new branch]      my-feature-branch -> my-feature-branch
...
```



## Finding contributions to work on
Looking at the existing issues is a great way to find something to contribute on. As our projects, by default, use the default GitHub issue labels (enhancement/bug/duplicate/help wanted/invalid/question/wontfix), looking at any 'help wanted' issues is a great place to start.


## Code of Conduct
This project has adopted the [Amazon Open Source Code of Conduct](https://aws.github.io/code-of-conduct).
For more information see the [Code of Conduct FAQ](https://aws.github.io/code-of-conduct-faq) or contact
opensource-codeofconduct@amazon.com with any additional questions or comments.


## Security issue notifications
If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our [vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/). Please do **not** create a public github issue.


## Licensing

See the [LICENSE](LICENSE) file for our project's licensing. We will ask you to confirm the licensing of your contribution.