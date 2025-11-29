# python-intervals-icu-client Constitution

## Core Principles

### I. API-First, Upstream-True Client

The client MUST model the public Intervals.icu HTTP API as its source of truth.

- Public request/response models MUST reflect the upstream OpenAPI/JSON schema as closely as
	reasonably possible (field names, types, nullability, and documented defaults).
- Breaking server-side changes (removed fields, incompatible type changes, or changed semantics)
	MUST trigger a MAJOR version bump of this client once released.
- Additive upstream changes (new fields or non-breaking parameters) MUST result in MINOR version
	bumps when exposed in the library.
- The client MUST NOT introduce behavior that contradicts the documented server API (e.g., silently
	mutating parameters, hiding required fields, or fabricating responses).
- Where the upstream API is ambiguous, behavior MUST be documented explicitly in this client’s
	docstrings and/or `docs/` so that consumers know what to rely on.

Rationale: This library exists to make the Intervals.icu API easy and safe to use from Python while
remaining predictable when compared to upstream documentation.

### II. Typed, Documented Python Interface

The client surface MUST be Pythonic, typed, and discoverable.

- All public functions, methods, and data classes in `intervals_icu_client` MUST include type
	hints compatible with the supported Python versions.
- Public classes and functions MUST include concise docstrings that describe purpose, parameters,
	return values, and relevant error conditions.
- Synchronous HTTP usage is the default; if asynchronous interfaces are added, they MUST be clearly
	separated (e.g., `Async*` APIs or dedicated modules) and documented.
- Public API names MUST favor clarity over brevity and SHOULD generally mirror upstream concepts
	(Activities, Athletes, Gear, etc.).
- Backwards-incompatible renames of public symbols MUST be accompanied by deprecation shims when
	feasible and documented in the changelog.

Rationale: Strong typing and documentation improve IDE support, reduce integration mistakes, and
make it easier to upgrade the client safely.

### III. Test-First for Public Surface

Behavior of the public client API MUST be guarded by automated tests.

- Any new or modified public method, model, or configuration option MUST have at least one
	corresponding automated test (unit, functional, or integration) that fails before the
	implementation change and passes after it.
- Critical workflows (authentication, basic activity fetch/create/update flows, and error
	handling around network failures) MUST be covered by integration or functional tests under
	`tests/` or `test/`. `test` are generated tests from the openapi generator.
- Tests MUST be deterministic and avoid hard dependencies on external Intervals.icu instances
	unless explicitly marked as integration tests and documented.
- CI MUST run the project’s pytest suite (configured in `.vscode/settings.json`) for every change
	intended for release.

Rationale: As a client library, silent breakage harms end-user applications. Tests are the primary
guardrail against regressions.

### IV. Regenerate From Source of Truth

Generated code MUST be treated as a reproducible artifact, not hand-maintained business logic.

- Where OpenAPI or other schema-driven generation is used, the generation configuration and
	scripts (see `docs/_generate-client.md` and related tooling) MUST be kept in version control.
- Manual edits to generated files SHOULD be avoided; when unavoidable, they MUST be minimal,
	documented, and preferably applied via patches or post-processing steps instead of ad-hoc edits.
- Regeneration procedures MUST be documented so that maintainers can reproduce the client from a
	clean checkout.
- Differences between generated output and committed files SHOULD be explainable by intentional
	patches or configuration, not by unscripted local changes.

Rationale: Treating generation as a build step reduces drift from the upstream API and simplifies
maintenance.

### V. Simplicity, Readability, Least Surprise

The implementation and contribution workflow MUST prioritize simplicity and predictability.

- Code paths SHOULD be as small and explicit as possible: avoid unnecessary abstractions,
	inheritance hierarchies, and premature optimization.
- Public behaviors MUST avoid surprising side effects (e.g., implicit network calls on property
	access, global mutable state, or hidden retries) unless clearly documented.
- Error handling MUST prefer explicit exceptions over silent failure; mapping of HTTP errors to
	Python exceptions MUST be documented.
- Repository layout MUST remain straightforward: generated client package, tests, and supporting
	scripts/docs; avoid unrelated tooling or multi-project sprawl in this repository.

Rationale: This project is a thin client over an external API. Keeping it simple makes it easier
for users to reason about behavior and for maintainers to evolve it safely.

## Additional Constraints & Quality Bars

- **Supported Python versions**: The client MUST support the Python versions declared in
	`pyproject.toml`/`setup.cfg` and README. Dropping a supported Python version is a breaking
	change and MUST be accompanied by a MAJOR version bump and release notes.
- **Dependency discipline**: Runtime dependencies SHOULD be kept minimal and MUST be declared in
	`pyproject.toml`/`setup.cfg`. New dependencies MUST be justified (e.g., for HTTP, auth, or
	serialization capabilities that cannot be reasonably implemented in-house).
- **Docs alignment**: User-facing examples in `README.md` and `docs/` MUST compile logically with
	the current public API and configuration objects.
- **Security & secrets**: No hard-coded secrets or tokens may be committed. Examples MUST use
	environment variables (as in the README) for authentication.
- **Distribution**: Packaging metadata (version, classifiers, description) MUST reflect the actual
	supported API surface and stability. Pre-release or unstable areas SHOULD be clearly labeled in
	docs.

## Development Workflow & Review Gates

- **Specification-first for significant changes**: For major feature additions or large refactors,
	maintainers SHOULD capture intent using the SpecKit flow (`/speckit.specify`, `/speckit.plan`,
	`/speckit.tasks`) so that behavior and impact are explicit before heavy coding.
- **Constitution check in plans**: The "Constitution Check" section of `plan-template.md` MUST map
	proposed work back to these principles (API fidelity, typing & docs, testing discipline,
	regeneration model, simplicity). Any intentional deviations MUST be called out in the
	Complexity Tracking table along with justification.
- **Code review expectations**:
	- Reviewers MUST confirm that new or changed behavior is either covered by tests or explicitly
		scoped as non-production/stub work.
	- Reviewers MUST check that public API and docs stay aligned and that versioning impact is
		considered.
- **Tasks and implementation**: When using `/speckit.tasks` and `/speckit.implement`, tasks SHOULD
	be structured so that each user story or change set can be integrated and tested independently
	without breaking existing consumers.

## Governance

- **Authority of this document**: This constitution governs how the
	`python-intervals-icu-client` project is evolved. Where process documents, scripts, or templates
	conflict with this constitution, this document prevails until explicitly amended.
- **Amendment procedure**:
	- Substantive changes to principles or governance MUST be made in a dedicated pull request that
		clearly calls out the change and its impact.
	- The Sync Impact Report at the top of this file MUST be updated as part of any amendment,
		including version bump, changed sections, and any deferred TODOs.
	- Any change that relaxes testing discipline, API fidelity, or versioning rules MUST be treated
		as a MAJOR governance change and discussed explicitly in the PR description.
- **Versioning policy for this constitution**:
	- PATCH: Wording clarifications, typo fixes, and non-semantic edits.
	- MINOR: Adding new guidance that tightens quality bars without contradicting existing
		principles.
	- MAJOR: Removing or materially weakening a principle, or redefining versioning/testing
		expectations.
- **Compliance review**:
	- At minimum before each tagged library release, maintainers SHOULD verify that the changeset is
		consistent with the API-first, typed interface, and test-first principles.
	- Periodic review of this constitution (for example, quarterly or before large roadmap changes)
		is RECOMMENDED to keep it aligned with actual practice.

**Version**: 1.0.0 | **Ratified**: 2025-11-29; set by maintainer | **Last Amended**: 2025-11-29
