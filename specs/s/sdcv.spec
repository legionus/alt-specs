Name: sdcv
Version: 0.5.2
Release: alt1

Summary: A console version of StarDict the international dictionary

Group: System/Internationalization
License: GPLv2
Url: https://dushistov.github.io/sdcv/

Packager: Paul Wolneykien <manowar@altlinux.org>

Source: %name-%version.tar
Patch0: %name-t_interactive.patch
Patch1: %name-t_list.patch

BuildPreReq: rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake >= 2.8
BuildRequires: ctest >= 2.8
BuildRequires: jq
BuildRequires: zlib-devel
BuildRequires: libreadline-devel
BuildRequires: glib2-devel >= 2.6.1

%description
The console version of StarDict the cross-platform and international
dictionary.

%prep
%setup -q
# fix tests to run in isolated environment
%patch0 -p1
%patch1 -p1
# make output readable on dark terminals
sed -i 's/;34m/;36m/' src/libwrapper.cpp

%build
%cmake \
    -DENABLE_NLS=YES \
    -DWITH_READLINE=YES \
    -DBUILD_TESTS=YES

%cmake_build VERBOSE=1
%cmake_build VERBOSE=1 lang

%install
%cmakeinstall_std
%find_lang %name

%check
pushd BUILD
ctest  %_smp_mflags
popd

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_mandir/uk/man1/*

%changelog
* Fri Aug 31 2018 Andrew Savchenko <bircoph@altlinux.org> 0.5.2-alt1
- Version bump, upstream relocated.
- Enable tests.

* Thu Dec 12 2013 Paul Wolneykien <manowar@altlinux.org> 0.5.0-alt1
- Freshed up to v0.5.0 with the help of cronbuild and update-source-functions.

* Thu Dec 12 2013 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt1
- Freshed up to v0.4.2 with the help of cronbuild and update-source-functions.

