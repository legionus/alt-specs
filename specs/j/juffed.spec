Name:		juffed
Version:	0.10
Release:	alt2
License:	GPL
Group:		Editors
Summary:	Simple tabbed text editor

Source:		%name-%version.tar
Patch1:		%name-%version-fedora-cmake.patch

BuildRequires: gcc-c++ cmake libqt4-devel libqscintilla2-qt4-devel chrpath

Provides:   %name-plugins = %EVR
Obsoletes:  %name-plugins < %EVR

%package devel
Summary:	Includes for juffed
Group:		Development/KDE and QT
Requires:	%name = %EVR
BuildArch:	noarch

%description
Simple tabbed text editor with syntax highlighting for C++, Python,
HTML, PHP, XML, TeX, Makefiles, ini-files and patch-files

%description	devel
%{summary}
See http://code.google.com/p/juffed-plugins/wiki/JuffEd_Plugins_Tutorial for details.

%prep
%setup
%patch1 -p1

%build
%cmake \
	-DQSCINTILLA_NAMES=qscintilla2_qt4 \

%cmake_build VERBOSE=1

%install
%cmakeinstall_std
chrpath -d %buildroot%_bindir/%name
chrpath -d %buildroot%_libdir/libjuff.so
mkdir -p %buildroot/%_libdir/%name/plugins

%files
%doc COPYING ChangeLog README
%_bindir/%name
%_libdir/libjuff.*
%_libdir/libjuffed-engine-qsci.so*
%dir %_datadir/%name
%_datadir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins
%_desktopdir/%name.desktop
%_datadir/pixmaps/%name.png

%files devel
%_includedir/%name

%changelog
* Tue May 15 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10-alt2
- Fixed build with current toolchain.

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10-alt1.4
- Rebuilt with qscintilla2 2.10.1.

* Tue Jul 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10-alt1.3
- Update spec to build with new toolchain

* Tue Apr 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.2
- Rebuilt with qscintilla2 2.9

* Sat Nov 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.1
- Rebuilt with qscintilla2 2.8

* Wed Jul 31 2013 Andrey Cherepanov <cas@altlinux.org> 0.10-alt1
- New version
- Main package includes juffed-plugins and therefore obsoletes separate package

* Fri Dec 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt5.qa2
- Rebuilt with new qscintilla2

* Fri Sep 21 2012 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.1-alt5.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * vendor-tag for juffed-debuginfo
  * vendor-tag for juffed
  * vendor-tag for juffed-devel

* Wed Mar 21 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt5
- Consider %%optflags (thanks sbolshakov@)

* Thu Jan 12 2012 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt4
- Remove standard library path from library RPATH

* Mon Jul 25 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt3
- Rebuild for qscintilla2

* Tue Jan 18 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt2
- juffed-devel should be .noarch.rpm

* Mon Jan 17 2011 Andrey Cherepanov <cas@altlinux.org> 0.8.1-alt1
- Version 0.8.1
- Move plugins to _libdir/juffed/plugins

* Mon Jan 17 2011 Andrey Cherepanov <cas@altlinux.org> 0.8-alt1
- Initial build in Sisyphus

