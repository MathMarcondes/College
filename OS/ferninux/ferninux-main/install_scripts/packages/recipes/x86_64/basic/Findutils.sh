#!/bin/bash
# package recipe for ferninux build
# rename this file as foo-[cfg].sh

# arrays for download and build
unset DOWNLOAD_URLS
unset BUILD_DEPS
unset RUNTIME_DEPS
declare -A DOWNLOAD_URLS
declare -a BUILD_DEPS=()
declare -a RUNTIME_DEPS=()

# package details
MD5_SUM="4a4a547e888a944b2f3af31d789a1137"
DOWNLOAD_URLS[$MD5_SUM]="https://ftp.gnu.org/gnu/findutils/findutils-4.9.0.tar.xz"
SRC_COMPRESSED_FILE=$(basename ${DOWNLOAD_URLS[$MD5_SUM]})
SRC_FOLDER=${SRC_COMPRESSED_FILE%.*.*}

config_source_package(){
    ./configure --prefix=/usr --localstatedir=/var/lib/locate
}

build_source_package(){
    make $MAKEFLAGS
}

test_source_package(){
    chown -R tester .
    su tester -c "PATH=$PATH make check"
}

install_source_package(){
    make install
}
