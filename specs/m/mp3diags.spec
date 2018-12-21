Name: mp3diags
Version: 1.2.03
Release: alt2.1

Summary: Finds problems in MP3 files and helps the user fix many of them
License: GPLv2+
Group: File tools

URL: http://mp3diags.sourceforge.net/
Source: http://downloads.sourceforge.net/mp3diags/MP3Diags-%version.tar.gz
Source1: mp3diags.desktop

BuildRequires: gcc-c++ libqt4-devel
BuildRequires: boost-devel boost-program_options-devel

%description
Finds problems in MP3 files and helps the user to fix many of them using
included tools. Looks at both the audio part (VBR info, quality, normalization)
and the tags containing track information (ID3). Also includes a tag editor and
a file renamer.

%prep
%setup -n MP3Diags-%version

%build
%add_optflags -D_FILE_OFFSET_BITS=64
qmake-qt4
%make_build

%install
install -pD -m755 bin/MP3Diags %buildroot%_bindir/mp3diags
install -pD -m644 %_sourcedir/mp3diags.desktop %buildroot%_desktopdir/mp3diags.desktop
install -pD -m644 desktop/MP3Diags16.png %buildroot%_miconsdir/mp3diags.png
install -pD -m644 desktop/MP3Diags32.png %buildroot%_niconsdir/mp3diags.png
install -pD -m644 desktop/MP3Diags48.png %buildroot%_liconsdir/mp3diags.png

%files
%_bindir/*
%_desktopdir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*

%changelog
* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.03-alt2.1
- NMU: rebuilt with boost-1.67.0

* Wed Apr 18 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.03-alt2
- rebuilt with boost-1.66

* Sat Jul 30 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.03-alt1
- 1.2.03

* Thu Apr 07 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.02-alt1
- 1.2.02

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1.0.11.076-alt1.3.1
- rebuild with boost 1.57.0

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11.076-alt1.3
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11.076-alt1.2
- Rebuilt with Boost 1.52.0

* Fri Sep 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11.076-alt1.1
- Rebuilt with Boost 1.51.0

* Tue May 15 2012 Victor Forsiuk <force@altlinux.org> 1.0.11.076-alt1
- 1.0.11.076

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10.065-alt1.1
- Rebuilt with Boost 1.49.0

* Mon Jan 02 2012 Victor Forsiuk <force@altlinux.org> 1.0.10.065-alt1
- 1.0.10.065

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.09.063-alt1.1
- Rebuilt with Boost 1.48.0

* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 1.0.09.063-alt1
- 1.0.09.063

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.08.053-alt1.1
- Rebuilt with Boost 1.47.0

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 1.0.08.053-alt1
- 1.0.08.053

* Tue Mar 15 2011 Victor Forsiuk <force@altlinux.org> 1.0.07.052-alt2
- Rebuild with latest boost.

* Tue Jan 04 2011 Victor Forsiuk <force@altlinux.org> 1.0.07.052-alt1
- 1.0.07.052

* Fri Dec 17 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.06.051-alt1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Mon Jul 12 2010 Victor Forsiuk <force@altlinux.org> 1.0.06.051-alt1
- 1.0.06.051

* Fri Mar 19 2010 Victor Forsiuk <force@altlinux.org> 1.0.05.050-alt1
- 1.0.05.050

* Wed Mar 10 2010 Victor Forsiuk <force@altlinux.org> 1.0.04.049-alt1
- 1.0.04.049

* Fri Jan 29 2010 Victor Forsyuk <force@altlinux.org> 1.0.03.048-alt1
- 1.0.03.048

* Thu Jan 14 2010 Victor Forsyuk <force@altlinux.org> 1.0.02.047-alt1
- 1.0.02.047

* Sat Dec 12 2009 Victor Forsyuk <force@altlinux.org> 1.0.01.046-alt1
- Initial build.
