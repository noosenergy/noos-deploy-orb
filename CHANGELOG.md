# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2020-12-07
### Added
 - Initial release.
 - Common CI/CD tasks for basic Docker and Helm workflows.

## [0.0.2] - 2020-12-07
### Added
 - Enforce git tag filtering on all CircleCI jobs.

## [0.0.3] - 2020-12-07
### Changed
 - Split testing from publishing workflow.

## [0.1.1] - 2020-12-07
### Changed
 - Fix missing token on Helm build job.

## [0.1.2] - 2020-12-08
### Added
 - Common CI/CD tasks for basic Python workflows.

## [0.1.3] - 2020-12-10
### Added
 - Common CI/CD tasks for basic Terraform workflows.

## [0.1.4] - 2020-12-10
### Added
 - Standard example workflow with Python jobs.
### Changed
 - Pass build arguments into the Docker build job.

## [0.1.5] - 2020-12-17
### Changed
 - Bump `noos-ci` CLI version to v0.0.4.

## [0.1.6] - 2020-12-24
### Changed
 - Bump Helm CLI to v3.4.2.
 - Bump Helm CircleCI Orb to v1.1.2

## [0.1.7] - 2021-01-05
### Changed
 - Switch from `noos-ci` to `noos-inv` CI/CD SDK.
 - Bump `noos-tf` CLI version to v0.0.5.
 - Bump `noos-inv` CLI version to v0.0.5.
### Added
 - Pass install arguments for the Python venv installation.

## [0.1.8] - 2021-01-05
### Changed
 - Bump `pipenv` CLI version to v20.11.4.
 - Bump `poetry` CLI version to v1.1.4.

## [0.1.9] - 2021-01-06
### Changed
 - Bump Python version to v3.8.6.
