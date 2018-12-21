%define rname extra-cmake-modules

%ifarch e2k
%add_python_req_skip clang
%endif

Name: extra-cmake-modules
Version: 5.53.0
Release: alt1

Group: Development/Other
Summary: Additional modules for CMake build system
License: BSD
Url: http://community.kde.org/KDE_Core/Platform_11/Buildsystem/FindFilesSurvey

BuildArch: noarch

Requires: cmake clang-devel

Source: %name-%version.tar
Patch1: alt-find-qcollectiongenerator.patch
Patch2: alt-fix-python-install-dirs.patch
Patch3: alt-find-clang-library.patch

# Automatically added by buildreq on Thu Nov 17 2016 (-bi)
# optimized out: bzr cmake-modules fontconfig libqt4-clucene libqt4-core libqt4-devel libqt4-gui libqt4-help libqt4-network libqt4-sql libqt4-sql-sqlite policycoreutils python-base python-module-4Suite-XML python-module-IPy python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cssselect python-module-docutils python-module-enum34 python-module-google python-module-httplib2 python-module-imagesize python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mimeparse python-module-numpy python-module-pyasn1 python-module-pygobject3 python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-slip python-module-snowballstemmer python-module-sphinx python-module-twisted-core python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base rpm-build-python3 ruby xz
#BuildRequires: cmake ctags dblatex gyp libicu56 openbabel python-module-BeautifulSoup python-module-Pillow python-module-Reportlab python-module-alabaster python-module-bzr-fastimport python-module-cups python-module-ecdsa python-module-ed25519 python-module-html5lib python-module-nss python-module-polib python-module-pyExcelerator python-module-pycrypto python-module-pygraphviz python-module-pyparsing python-module-sphinx_rtd_theme python-modules-tkinter python3-dev rpm-build-gir ruby-stdlibs time
BuildRequires(pre): rpm-build-ubt
BuildRequires: cmake qt5-tools qt5-tools-devel
BuildRequires: /usr/bin/sphinx-build rpm-build-python


%description
Additional modules for CMake build system needed by KDE Frameworks.

%prep
%setup
%patch1 -p1
%patch2 -p1
#%patch3 -p1

%ifarch e2k
# lcc doesn't support these as of 1.21.20
sed -i -r 's, (-fno-operator-names|-Wvla),,' kde-modules/KDECompilerSettings.cmake
%endif

%build
%cmake \
    -DBUILD_TESTING:BOOL=FALSE \
    #
#    -DBUILD_QTHELP_DOCS:BOOL=TRUE \
%cmake_build

%install
%cmakeinstall_std

%files
%_datadir/ECM
%doc README.rst COPYING-CMAKE-SCRIPTS
%doc %_docdir/ECM
%doc %_man7dir/*

%changelog
* Tue Dec 11 2018 Sergey V Turchin <zerg@altlinux.org> 5.53.0-alt1
- new version

* Mon Nov 12 2018 Sergey V Turchin <zerg@altlinux.org> 5.52.0-alt1
- new version

* Wed Oct 17 2018 Sergey V Turchin <zerg@altlinux.org> 5.51.0-alt1
- new version

* Mon Sep 10 2018 Sergey V Turchin <zerg@altlinux.org> 5.50.0-alt1%ubt
- new version

* Tue Aug 21 2018 Sergey V Turchin <zerg@altlinux.org> 5.49.0-alt1%ubt
- new version

* Thu Jul 19 2018 Sergey V Turchin <zerg@altlinux.org> 5.48.0-alt1%ubt
- new version

* Fri Jun 15 2018 Sergey V Turchin <zerg@altlinux.org> 5.47.0-alt1%ubt
- new version

* Mon May 14 2018 Sergey V Turchin <zerg@altlinux.org> 5.46.0-alt1%ubt
- new version

* Fri May 04 2018 Sergey V Turchin <zerg@altlinux.org> 5.45.0-alt1%ubt
- new version

* Tue Mar 20 2018 Sergey V Turchin <zerg@altlinux.org> 5.44.0-alt1%ubt
- new version

* Mon Mar 19 2018 Oleg Solovyov <mcpain@altlinux.org> 5.42.0-alt3%ubt
- find clang library

* Mon Mar 05 2018 Oleg Solovyov <mcpain@altlinux.org> 5.42.0-alt2%ubt
- fix install dirs for python bindings

* Thu Jan 18 2018 Sergey V Turchin <zerg@altlinux.org> 5.42.0-alt1%ubt
- new version

* Tue Dec 12 2017 Sergey V Turchin <zerg@altlinux.org> 5.41.0-alt1%ubt
- new version

* Tue Nov 21 2017 Sergey V Turchin <zerg@altlinux.org> 5.40.0-alt1%ubt
- new version

* Tue Oct 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.39.0-alt1%ubt
- new version

* Tue Sep 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.38.0-alt1%ubt
- new version

* Thu Aug 24 2017 Sergey V Turchin <zerg@altlinux.org> 5.37.0-alt2%ubt
- fix requires

* Wed Aug 16 2017 Sergey V Turchin <zerg@altlinux.org> 5.37.0-alt1%ubt
- new version

* Mon Jul 10 2017 Sergey V Turchin <zerg@altlinux.org> 5.36.0-alt1%ubt
- new version

* Thu Jun 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.35.0-alt1%ubt
- new version

* Fri May 19 2017 Sergey V Turchin <zerg@altlinux.org> 5.34.0-alt1%ubt
- new version

* Mon Apr 17 2017 Sergey V Turchin <zerg@altlinux.org> 5.33.0-alt1%ubt
- new version

* Wed Mar 29 2017 Sergey V Turchin <zerg@altlinux.org> 5.32.0-alt1%ubt
- new version

* Mon Feb 13 2017 Sergey V Turchin <zerg@altlinux.org> 5.31.0-alt1%ubt
- new version

* Wed Feb 08 2017 Sergey V Turchin <zerg@altlinux.org> 5.30.0-alt1%ubt
- new version

* Tue Dec 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.29.0-alt1%ubt
- new version

* Fri Nov 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt0.M80P.1
- build for M80P

* Wed Nov 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.28.0-alt1
- new version

* Thu Oct 13 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt0.M80P.1
- build for M80P

* Tue Oct 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.27.0-alt1
- new version

* Mon Sep 12 2016 Sergey V Turchin <zerg@altlinux.org> 5.26.0-alt1
- new version

* Mon Aug 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.25.0-alt1
- new version

* Mon Jul 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.24.0-alt1
- new version

* Tue Jun 28 2016 Sergey V Turchin <zerg@altlinux.org> 5.23.0-alt1
- new version

* Fri May 20 2016 Sergey V Turchin <zerg@altlinux.org> 5.22.0-alt1
- new version

* Mon Apr 18 2016 Sergey V Turchin <zerg@altlinux.org> 5.21.0-alt1
- new version

* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 5.20.0-alt1
- new version

* Tue Feb 16 2016 Sergey V Turchin <zerg@altlinux.org> 5.19.0-alt1
- new version

* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- new version

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- new version

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Mon Sep 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- new version

* Wed Aug 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Mon May 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt0.1
- test

* Fri Jan 16 2015 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt0.1
- initial build
