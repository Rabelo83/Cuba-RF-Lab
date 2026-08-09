# Changelog

This project uses semantic engineering versioning.

## 0.1.0 - 2026-08-09

Status: research baseline

Created the initial repository structure, collaboration rules, project state, assumptions, decisions, open questions, starter research files, measurement template, and calculation scripts.

No antenna design is approved in this release.

Added a MkDocs-based GitHub Pages public documentation site with curated pages for project overview, SOPs, blueprint status, research, materials, data templates, collaboration, and site administration.

Adjusted the Pages strategy so the public branch-based GitHub Pages site serves committed MkDocs static output, matching the local MkDocs preview.

Added a bilingual `Keep It Simple` site section with plain-language pages for Track A phone-first architecture and Track B passive antenna/coupler experiments.

Updated collaborator instructions so future AI or human contributors know how the branch-based MkDocs Pages output is published and how to maintain the `Keep It Simple` section.

Added an antenna topology comparison framework, provisional pre-measurement ranking, net RF improvement rule, and candidate comparison CSV template. The LPDA is explicitly treated as one candidate, not the default or final antenna.

Documented the broader public-benefit mission: research and simulations must lead toward a solution useful for Cuban people during blackouts, with the lowest practical production cost, repairability, and real-world efficiency.

Propagated the public-production objective across requirements, research, routerless, coupler, simulation, calculation, testing, material, legal, CAD, image, data, result, and collaboration documentation. Updated antenna comparison weights so low production cost and Cuba-based fabrication/repairability carry stronger decision weight.

Added a Cuba material availability raw ledger and CSV template so local observations about materials, prices, sources, quality, substitutions, and confidence can be preserved as project data.

Changed the public display name to Cuba RF Lab and updated documentation links to the `Cuba-RF-Lab` repository path.

Documented the current temporary no-local-data constraint: owner-side RF measurements and material observations are unavailable in the current phase, so the project will proceed with public sources, manufacturer data, conservative assumptions, calculations, simulations, and sensitivity analysis until later field validation exists.

Added the first desktop public-source RF baseline: source-backed 900 MHz and 1800 MHz working bands, secondary 700/2100 MHz awareness, coax attenuation benchmarks, passive-coupler loss assumptions, and conservative link-budget scenarios comparing phone-at-RF-location against passive antenna/coax/coupler paths.
