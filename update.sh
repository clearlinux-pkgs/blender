#!/bin/bash
set -e -o pipefail

PKG=$(grep "PKG_NAME" Makefile | awk '{print $3}')

errexit() {
	local ret=1
	echo "Error: $1"
	if [[ -n "$2" ]]; then
		ret=2
	fi
	exit $ret
}

echo -n "Pulling package repo changes: "
git pull --ff-only

make -s update-versions
NEW_VERSION=$(perl -ne "m|/${PKG}-(\d+(?:\.\d+)+).*| && print \$1" Makefile | head -1)
NEW_VERSION_DIR=${NEW_VERSION}
CURRENT_VERSION="$(rpmspec --srpm -q --qf="%{VERSION}" $PKG.spec)"

echo "Our current version: ${CURRENT_VERSION}"
echo "New version:         ${NEW_VERSION}"

if [[ "$1" != "--force" ]]; then
	if [[ "${CURRENT_VERSION}" = "${NEW_VERSION}" ]]; then
		echo "Not rebuilding. Run the script directly with --force to override:"
		echo "$0 --force"
		exit
	fi
fi

# Update the version for source and archive tarballs in Makefile
echo "Updating Makefile."
perl -pi -e 's/('"${PKG}"'-(?:\w+-)?)\d+(?:\.\d+)+/${1}'${NEW_VERSION}'/g; s|(/)\d+(?:\.\d+)+(/)|${1}'${NEW_VERSION_DIR}'${2}|g' Makefile

# Remove archives from options.conf; otherwise autospec will fail
echo "Updating options.conf."
perl -pi -e 's/^(archives\s*=).*/$1/' options.conf

# Check whether anything changed. Should have been caught above, so this is
# probably a script failure.
if git diff-index --quiet HEAD --; then
	echo "Weird, nothing changed."
	exit 1
fi

# Download and cache the new tarballs, since they could take longer than
# autospec allows
echo "Downloading and caching the new tarballs to avoid autospec timeouts."
git diff Makefile | grep '^+' | grep -oE 'https?://(\S+)' | wget -N -i - || :

# Build the new version
echo "Running autospec."
make autospec

echo "Sending to Koji."
make koji-nowait
