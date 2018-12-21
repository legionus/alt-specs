%def_enable static
%def_without doc
%define sover 1

Name: audiofile
Version: 0.3.6
Release: alt3

Summary: Library to handle various audio file formats
License: LGPL
Group: System/Libraries
Url: http://www.68k.org/~michael/%name

# VCS https://github.com/mpruett/audiofile.git
Source: %url/%name-%version.tar
# newer pkg-config macros required
Source1: pkg.m4
Patch: %name-%version-%release.patch
Patch1: %name-0.3.6-alt-configure.patch

Requires: lib%name%sover = %version-%release

BuildRequires: gcc-c++ glibc-devel-static libalsa-devel
BuildPreReq: libflac-devel
%{?_with_doc:BuildRequires: asciidoc-a2x}

%package -n lib%name%sover
Summary: Shared library for %name
Group: System/Libraries

%package -n lib%name-devel
Summary: Includes and other files to develop %name applications
Group: Development/C
Requires: lib%name%sover = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel

%package -n lib%name-devel-static
Summary: Static libraries to develop %name applications
Group: Development/C
Requires: lib%name-devel = %version-%release

%description
The Audio File Library handles reading and writing audio files in many
common formats.

Key goals of the Audio File Library are file format transparency and data
format transparency. The same calls for opening a file, accessing and
manipulating audio metadata (e.g. sample rate, sample format, textual
information, MIDI parameters), and reading and writing sample data will
work with any supported audio file format. Likewise, the format of the
audio data presented to the application need not be tied to the format
of the data contained in the file.

The following file formats are currently supported:
* AIFF/AIFF-C
* WAVE
* NeXT .snd/Sun .au
* Berkeley/IRCAM/CARL Sound File
* Audio Visual Research
* Amiga IFF/8SVX
* Creative Voice File
* NIST SPHERE
* Core Audio Format

The following compression formats are currently supported:
* G.711 mu-law and A-law
* IMA ADPCM
* Microsoft ADPCM

%description -n lib%name%sover
This package contains the library needed to run programs dynamically
linked with audiofile.

%description -n lib%name-devel
Include files and other resources you can use to develop
%name applications.

%description -n lib%name-devel-static
Static libraries you can use to develop
%name applications.

%prep
%setup
%patch -p1
[ ! -d m4 ] && mkdir m4 && cp %SOURCE1 m4/
%patch1 -b .m4

%build
%autoreconf
%configure \
	--enable-largefile \
	%{?!_with_doc:--disable-docs} \
	%{subst_enable static}
# SMP-incompatible build (man pages)
%make_build || %make

%install
%makeinstall_std

%check
%make check

%files
%_bindir/sfconvert
%_bindir/sfinfo
%doc README ACKNOWLEDGEMENTS TODO NEWS NOTES

%files -n lib%name%sover
%_libdir/*.so.*
%if_with doc
%_man1dir/*
%endif

%files -n lib%name-devel
%_libdir/*.so
%_pkgconfigdir/*
%_includedir/*
%if_with doc
%_man3dir/*
%endif

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Thu Dec 06 2018 Michael Shigorin <mike@altlinux.org> 0.3.6-alt3
- E2K: no difference anymore
- A shot at SMP build

* Wed Mar 15 2017 Michael Shigorin <mike@altlinux.org> 0.3.6-alt2.1
- BOOTSTRAP: introduce doc knob (on by default)
- E2K: avoid lcc-unsupported option

* Sun Jan 29 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt2
- updated to 0.3.6-26-g6ac5a49
- %%check section

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.3.6-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Sep 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1
- Version 0.3.6

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3.2-alt3.qa1
- NMU: rebuilt for updated dependencies.

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt3
- Fixed build

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2
- Fixed RPATH

* Wed Nov 30 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Mon Sep 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt2
- Rebuilt for debuginfo

* Tue Nov 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.7-alt1
- Version 0.2.7

* Mon Jan 05 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.2.6-alt3
- Fix CVE-2008-5824.

* Sat Jan 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.2.6-alt2
- Added packager field.
- Build with largefile support.

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.6-alt1.1.1
- Rebuilt for new pkg-config dependencies.

* Mon Nov 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.6-alt1.1
- build static library (#5581).

* Sat Mar 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Mon Dec 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.5-alt1
- 0.2.5
- do not build lib%%name-devel-static subpackage by default.

* Thu Nov 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.4-alt2
- don't package .la files.

* Wed Nov 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Wed Nov 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.3-alt4
- Updated from cvs to make gstreamer, grecord, rezound huppy.

* Mon Oct 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.3-alt3
- Rebuild with gcc-3.2

* Sat Mar 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.3-alt2
- pkgconfig files added in lib%name-devel package.

* Tue Nov 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.2.3-alt1
- 0.2.3

* Wed Aug 29 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.2.2-alt1
- 0.2.2
- Added devel-static package

* Wed Feb 28 2001 Dmitry V. Levin <ldv@fandra.org> 0.2.1-ipl1mdk
- 0.2.1
- Libification.

* Fri Dec 01 2000 Dmitry V. Levin <ldv@fandra.org> 0.1.11-ipl2mdk
- RE adaptions.

* Mon Nov  6 2000 dam's <damien@mandrakesoft.com> 0.1.11-2mdk
- cosmetik changes.

* Sun Oct 29 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 0.1.11-1mdk
- new version aka shiny source.

* Fri Jul 21 2000 dam's <damien@mandrakesoft.com> 0.1.9-5mdk
- BM + macrozification

* Wed Jun 21 2000 dam's <damien@mandrakesoft.com> 0.1.9-4mdk
- mandrake release

* Wed Apr 12 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.1.9-3mdk
- new groups
- cleaned up specfile

* Wed Nov  3 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Update URL.
- (NMU)

* Fri Sep 24 1999 Axalon Bloodstone <axalon@linux-mandrake.com>
- 0.1.9

* Mon Jun 28 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Add the .m4 files in devel package.
- Last CVS version from Mon Jun 28 1999.

* Mon Jun 14 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- 0.1.7

* Fri Apr 23 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adpatations.
- We stripping with our macros ;-).

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- strip binaries before packaging

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- Version 0.1.6

* Sun Feb 21 1999 Michael Fulbright <drmike@redhat.com>
- Removed libtoolize from %build

* Wed Feb 3 1999 Jonathan Blandfor <jrb@redhat.com>
- Newer version with bug fix.  Upped release.

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- integrating into rawhide release at GNOME freeze

* Fri Nov 20 1998 Michael Fulbright <drmike@redhat.com>
- First try at a spec file

