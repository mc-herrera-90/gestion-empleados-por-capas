#!/usr/bin/env bash
set -euo pipefail

VERSION="${1:-${GITHUB_REF##*/}}"
REPO="${GITHUB_REPOSITORY}"

echo "Creando release $VERSION"

gh release create "$VERSION" dist/*.whl dist/*.tar.gz \
  --repo "$REPO" \
  --title "Release $VERSION" \
  --notes "Release generado automáticamente desde CI/CD"

gh release edit "$VERSION" --draft=false --repo "$REPO"
