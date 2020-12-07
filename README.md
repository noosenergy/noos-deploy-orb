[![CircleCI](https://circleci.com/gh/noosenergy/noos-deploy-orb.svg?style=svg&circle-token=9f3de0b8378330e0e1ff6bb296f04e31eed67d77)](https://circleci.com/gh/noosenergy/noos-deploy-orb)

# Noos Deploy Orb

Custom CircleCI Orb for working with Docker and Helm CI/CD pipelines.

## Resources

[CircleCI Orb Registry Page](https://circleci.com/orbs/registry/orb/noosenergy/noos-deploy-orb) - The official registry page of this orb for all versions, executors, commands, and jobs described.

[CircleCI Orb Docs](https://circleci.com/docs/2.0/orb-intro/#section=configuration) - Docs for using and creating CircleCI Orbs.

[CI/CD Noos Deploy SDK](https://github.com/noosenergy/noos-deploy) - Software development kit for managing CI/CD pipelines, installed onto such a CircleCI Orb.

### How to Contribute

We welcome [issues](https://github.com/noosenergy/noos-deploy-orb/issues) to and [pull requests](https://github.com/noosenergy/noos-deploy-orb/pulls) against this repository!

### How to Publish
* Create and push a branch with your new features.
* When ready to publish a new production version, create a Pull Request from your _feature branch_ to `master`.
* Request manual approval to run the integration tests against your _feature branch_.
* Once your features have been merged, the final merge commit onto the `master` branch should be tagged as `<increment>-release-<version>` where:

| increment | version|
| ----------| -----------|
| major     | 1.0.0 incremented release|
| minor     | x.1.0 incremented release|
| patch     | x.x.1 incremented release|
