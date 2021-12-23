#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : blender
Version  : 3.0.0
Release  : 58
URL      : https://download.blender.org/source/blender-3.0.0.tar.xz
Source0  : https://download.blender.org/source/blender-3.0.0.tar.xz
Summary  : A fully integrated 3D graphics creation suite
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause BSD-3-Clause-LBNL BSL-1.0 CC0-1.0 GPL-2.0 GPL-3.0 MIT
Requires: OpenColorIO
Requires: embree
Requires: oiio
Requires: python3
Requires: scene-alembic
Requires: yaml-cpp
BuildRequires : Imath-dev
BuildRequires : OpenColorIO-data
BuildRequires : OpenColorIO-dev
BuildRequires : SDL-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : bzip2-dev
BuildRequires : cmake
BuildRequires : desktop-file-utils
BuildRequires : doxygen
BuildRequires : eigen-dev
BuildRequires : embree-dev
BuildRequires : embree-lib
BuildRequires : extra-cmake-modules pkgconfig(OpenEXR)
BuildRequires : freeglut-dev
BuildRequires : freetype-dev
BuildRequires : git
BuildRequires : glew-dev
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : jemalloc-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : lzo-dev
BuildRequires : mesa-dev
BuildRequires : numpy-dev
BuildRequires : oiio-dev
BuildRequires : openal-soft-dev
BuildRequires : openexr-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glew)
BuildRequires : pkgconfig(glu)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xfixes)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(zlib)
BuildRequires : potrace-dev
BuildRequires : pugixml-dev
BuildRequires : pypi(phabricator)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : scene-alembic-dev
BuildRequires : tiff-dev
BuildRequires : xorgproto-dev
BuildRequires : zlib-dev
Patch1: 0001-Install-scripts-to-different-location.patch
Patch2: 0002-Install-blender-thumbnailer-to-scripts-directory.patch
Patch3: 0003-Install-to-unversioned-system-path.patch
Patch4: 0004-Install-blenderplayer-manpage.patch
Patch5: 0005-Install-internal-fonts-to-different-location.patch
Patch6: 0006-Install-locale-files-to-different-location.patch
Patch7: 0007-add-mime-file.patch
Patch8: 0008-cmake-Add-usr-to-Alembic-search-path.patch
Patch9: 0009-Fix-build-with-openexr-3.x.patch

%description
Blender is the free and open source 3D creation suite. It supports the entirety
of the 3D pipeline—modeling, rigging, animation, simulation, rendering,
compositing and motion tracking, video editing and 2D animation pipeline.

%prep
%setup -q -n blender-3.0.0
cd %{_builddir}/blender-3.0.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1638632863
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export FCFLAGS=$FFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%cmake .. -DBUILD_SHARED_LIBS:BOOL=OFF \
-DCMAKE_EXE_LINKER_FLAGS:STRING="-pie" \
-DCMAKE_INSTALL_PREFIX:PATH=/usr \
-DCMAKE_PREFIX_PATH=/usr/lib64 \
-DPYTHON_INCLUDE_DIRS=/usr/include/python$(pkg-config python3 --modversion) \
-DPYTHON_LIBPATH=/usr/lib \
-DPYTHON_LIBRARY=python$(pkg-config python3 --modversion) \
-DPYTHON_VERSION=$(pkg-config python3 --modversion) \
-DWITH_ALEMBIC:BOOL=ON \
-DWITH_AUDASPACE:BOOL=ON \
-DWITH_BUILDINFO:BOOL=ON \
-DWITH_CODEC_FFMPEG:BOOL=OFF \
-DWITH_CODEC_SNDFILE:BOOL=OFF \
-DWITH_CYCLES:BOOL=ON \
-DWITH_CYCLES_EMBREE=ON \
-DWITH_DOC_MANPAGE:BOOL=ON \
-DWITH_FFTW3:BOOL=ON \
-DWITH_IMAGE_OPENJPEG:BOOL=OFF \
-DWITH_INPUT_NDOF:BOOL=ON \
-DWITH_INSTALL_PORTABLE:BOOL=OFF \
-DWITH_JACK:BOOL=OFF \
-DWITH_JACK_DYNLOAD:BOOL=OFF \
-DWITH_LIBMV_SCHUR_SPECIALIZATIONS:BOOL=ON \
-DWITH_LLVM:BOOL=ON \
-DWITH_MEM_JEMALLOC:BOOL=OFF \
-DWITH_MOD_OCEANSIM:BOOL=ON \
-DWITH_OPENCOLLADA:BOOL=OFF \
-DWITH_OPENCOLORIO:BOOL=ON \
-DWITH_OPENIMAGEIO:BOOL=ON \
-DWITH_OPENVDB:BOOL=OFF \
-DWITH_PYTHON:BOOL=ON \
-DWITH_PYTHON_INSTALL:BOOL=OFF \
-DWITH_PYTHON_INSTALL_NUMPY=OFF \
-DWITH_PYTHON_INSTALL_REQUESTS:BOOL=OFF \
-DWITH_PYTHON_SAFETY:BOOL=ON \
-DWITH_SDL:BOOL=ON \
-DWITH_SDL_DYNLOAD:BOOL=ON \
-DWITH_SYSTEM_AUDASPACE:BOOL=OFF \
-DWITH_SYSTEM_EIGEN3:BOOL=ON \
-DWITH_SYSTEM_GLEW:BOOL=ON \
-DWITH_SYSTEM_LZO:BOOL=ON
make  %{?_smp_mflags}  -O
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
export FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export FCFLAGS=$FFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DBUILD_SHARED_LIBS:BOOL=OFF \
-DCMAKE_EXE_LINKER_FLAGS:STRING="-pie" \
-DCMAKE_INSTALL_PREFIX:PATH=/usr \
-DCMAKE_PREFIX_PATH=/usr/lib64 \
-DPYTHON_INCLUDE_DIRS=/usr/include/python$(pkg-config python3 --modversion) \
-DPYTHON_LIBPATH=/usr/lib \
-DPYTHON_LIBRARY=python$(pkg-config python3 --modversion) \
-DPYTHON_VERSION=$(pkg-config python3 --modversion) \
-DWITH_ALEMBIC:BOOL=ON \
-DWITH_AUDASPACE:BOOL=ON \
-DWITH_BUILDINFO:BOOL=ON \
-DWITH_CODEC_FFMPEG:BOOL=OFF \
-DWITH_CODEC_SNDFILE:BOOL=OFF \
-DWITH_CYCLES:BOOL=ON \
-DWITH_CYCLES_EMBREE=ON \
-DWITH_DOC_MANPAGE:BOOL=ON \
-DWITH_FFTW3:BOOL=ON \
-DWITH_IMAGE_OPENJPEG:BOOL=OFF \
-DWITH_INPUT_NDOF:BOOL=ON \
-DWITH_INSTALL_PORTABLE:BOOL=OFF \
-DWITH_JACK:BOOL=OFF \
-DWITH_JACK_DYNLOAD:BOOL=OFF \
-DWITH_LIBMV_SCHUR_SPECIALIZATIONS:BOOL=ON \
-DWITH_LLVM:BOOL=ON \
-DWITH_MEM_JEMALLOC:BOOL=OFF \
-DWITH_MOD_OCEANSIM:BOOL=ON \
-DWITH_OPENCOLLADA:BOOL=OFF \
-DWITH_OPENCOLORIO:BOOL=ON \
-DWITH_OPENIMAGEIO:BOOL=ON \
-DWITH_OPENVDB:BOOL=OFF \
-DWITH_PYTHON:BOOL=ON \
-DWITH_PYTHON_INSTALL:BOOL=OFF \
-DWITH_PYTHON_INSTALL_NUMPY=OFF \
-DWITH_PYTHON_INSTALL_REQUESTS:BOOL=OFF \
-DWITH_PYTHON_SAFETY:BOOL=ON \
-DWITH_SDL:BOOL=ON \
-DWITH_SDL_DYNLOAD:BOOL=ON \
-DWITH_SYSTEM_AUDASPACE:BOOL=OFF \
-DWITH_SYSTEM_EIGEN3:BOOL=ON \
-DWITH_SYSTEM_GLEW:BOOL=ON \
-DWITH_SYSTEM_LZO:BOOL=ON
make  %{?_smp_mflags}  -O
popd

%install
export SOURCE_DATE_EPOCH=1638632863
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/blender
cp %{_builddir}/blender-3.0.0/COPYING %{buildroot}/usr/share/package-licenses/blender/002c2409e6067c4266c849727f3fc57978f4a2b5
cp %{_builddir}/blender-3.0.0/doc/license/BSD-3-Clause-license.txt %{buildroot}/usr/share/package-licenses/blender/6167dbf96cbf9e18895b6d383f51844e5d110f55
cp %{_builddir}/blender-3.0.0/doc/license/GPL-license.txt %{buildroot}/usr/share/package-licenses/blender/83b54b10518c3d114a1ff5ea7e2653a20d9d3458
cp %{_builddir}/blender-3.0.0/doc/license/GPL3-license.txt %{buildroot}/usr/share/package-licenses/blender/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/blender-3.0.0/extern/audaspace/LICENSE %{buildroot}/usr/share/package-licenses/blender/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/blender-3.0.0/extern/ceres/LICENSE %{buildroot}/usr/share/package-licenses/blender/c2714fada57efd120de5f1229e46eaf87cf0a16e
cp %{_builddir}/blender-3.0.0/extern/cuew/LICENSE %{buildroot}/usr/share/package-licenses/blender/d2bf36877185a0d9b2baf0450ef8f0e01be1125d
cp %{_builddir}/blender-3.0.0/extern/draco/draco/LICENSE %{buildroot}/usr/share/package-licenses/blender/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/blender-3.0.0/extern/gflags/COPYING.txt %{buildroot}/usr/share/package-licenses/blender/b2d4ab17f1b8ef9e0646ba932dce81efe3b852ab
cp %{_builddir}/blender-3.0.0/extern/glew-es/LICENSE.txt %{buildroot}/usr/share/package-licenses/blender/0ca22faedb8ee495473a82c4d91452493b22ac9f
cp %{_builddir}/blender-3.0.0/extern/glew/LICENSE.txt %{buildroot}/usr/share/package-licenses/blender/0ca22faedb8ee495473a82c4d91452493b22ac9f
cp %{_builddir}/blender-3.0.0/extern/glog/COPYING %{buildroot}/usr/share/package-licenses/blender/43c9d4e201bf773d965455b593cd8a244d98564b
cp %{_builddir}/blender-3.0.0/extern/gmock/LICENSE %{buildroot}/usr/share/package-licenses/blender/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/blender-3.0.0/extern/gtest/LICENSE %{buildroot}/usr/share/package-licenses/blender/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/blender-3.0.0/extern/lzo/minilzo/COPYING %{buildroot}/usr/share/package-licenses/blender/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/blender-3.0.0/extern/mantaflow/LICENSE %{buildroot}/usr/share/package-licenses/blender/6596d7deb814bf619e0b2c0a7c29dbb3b9f8f43e
cp %{_builddir}/blender-3.0.0/extern/quadriflow/3rd/lemon-1.3.1/LICENSE %{buildroot}/usr/share/package-licenses/blender/b34f205f74c018d0d5b8c116015f58df92375a11
cp %{_builddir}/blender-3.0.0/extern/quadriflow/LICENSE.txt %{buildroot}/usr/share/package-licenses/blender/86241cf770af908f25bb6be748d736dda1e3cd44
cp %{_builddir}/blender-3.0.0/intern/numaapi/LICENSE %{buildroot}/usr/share/package-licenses/blender/50159ef1fd8035c7dd7e2e9aa9d6e34adc2eaf54
cp %{_builddir}/blender-3.0.0/release/datafiles/studiolights/matcap/license.txt %{buildroot}/usr/share/package-licenses/blender/faddfe17fb1306925298bb760341d43212999be4
cp %{_builddir}/blender-3.0.0/release/datafiles/studiolights/world/license.txt %{buildroot}/usr/share/package-licenses/blender/8e278c84a1bf9b2df9c1ee407349c4634f104777
cp %{_builddir}/blender-3.0.0/release/license/GPL-license.txt %{buildroot}/usr/share/package-licenses/blender/aa84cb217f40293d65b82d5b5947bd0c77e63fd3
cp %{_builddir}/blender-3.0.0/release/text/copyright.txt %{buildroot}/usr/share/package-licenses/blender/823ab2688ac7fe2082b9d53afd9ebb2122aeb337
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
## install_append content
# Fix any .py files with shebangs and wrong permissions.
find %{buildroot} -name "*.py" -perm 0644 -print0 | \
xargs -0r grep -lZ '^#!.*/usr' | xargs -0r chmod -v 0755;

# Mime support
dest=%{buildroot}/usr/share/mime/packages
mkdir -pv "$dest"
install -v -p -m 644 -t "$dest" ./blender.xml

# Install metainfo
dest=%{buildroot}/usr/share/metainfo
mkdir -pv "$dest"
install -v -p -m 644 -t "$dest" ./release/freedesktop/org.blender.Blender.appdata.xml

# Desktop icon
desktop-file-validate %{buildroot}/usr/share/applications/blender.desktop

# Localization
rm -vrf %{buildroot}/usr/share/locale/languages
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
