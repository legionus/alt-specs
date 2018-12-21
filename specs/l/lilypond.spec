%define _unpackaged_files_terminate_build 1

%define ver_major 2.18
%define ver_minor 2
%define _lily_dir %_datadir/%name/%version
%define _texmf %_datadir/texmf

Name: lilypond
Version: %ver_major.%ver_minor
Release: alt1

Group: Publishing
Summary: A program for printing sheet music
License: GPLv3
Url: http://www.lilypond.org

Source: %name-%version.tar.gz
Source1: russian-lirycs-test.ly

Requires: ghostscript

BuildRequires: gcc-c++ emacs emacs-devel flex fontconfig-devel fontforge guile-devel
BuildRequires: help2man libfreetype-devel libpango-devel makeinfo python-devel texlive

%package -n emacs-mode-%name
Summary: Major mode for editing GNU LilyPond music scores 
Group: Editors
BuildArch: noarch
Requires: %name = %version-%release

%package -n emacs-mode-%name-el
Summary: The Emacs Lisp sources for bytecode included in emacs-mode-%name
Group: Development/Other
BuildArch: noarch
Requires: emacs-mode-%name = %version-%release

%description
LilyPond is a music typesetter. It produces beautiful sheet music using
a high level description file as input. Lilypond is part of the GNU
project. This package contains the utilities for converting the music
source (.ly) files into printable output.

%description -n emacs-mode-%name
emacs-mode-%name provides syntax coloring, inserting tags,
PS-compilation, PS-viewing and MIDI-play.
All Emacs Lisp code is byte-compiled, install emacs-mode-%name-el for sources.

%description -n emacs-mode-%name-el
emacs-mode-%name-el contains the Emacs Lisp sources for the bytecode
included in the emacs-mode-%name package, that extends the Emacs editor.
You need to install emacs-mode-%name-el only if you intend to modify any of the
emacs-mode-%name code or see some Lisp examples.

%prep
%setup
subst 's|package_infodir = $(infodir)/$(package)|package_infodir = $(infodir)|' config.make.in

%build
%configure \
	--with-ncsb-dir=/usr/share/fonts/type1/urw \
	--disable-documentation

%make_build

%install
%makeinstall_std
help2man %buildroot%_bindir/lilypond > %buildroot%_man1dir/lilypond.1

# install russian-lirycs-test.ly
%__install -m644 %SOURCE1 .

# Install Emacs-mode files 
%__mkdir_p %buildroot/%_emacs_sitestart_dir
%__mv %buildroot%_emacslispdir/%name-init.el %buildroot%_emacs_sitestart_dir/
for i in %buildroot%_emacslispdir/%{name}*.el; do
%byte_compile_file $i
done

#FIXME:msp:
# These files cannot pass verify-info check;
%__rm -f %buildroot%_infodir/lilypond* %buildroot%_infodir/music*

%find_lang %name

%files -f %name.lang
%_bindir/*
%_libdir/%name
%_datadir/%name
#%_infodir/*
%_man1dir/*
%doc AUTHORS.txt COPYING DEDICATION HACKING INSTALL.txt LICENSE LICENSE.DOCUMENTATION LICENSE.OFL NEWS.txt README.txt ROADMAP
%doc russian-lirycs-test.ly

%files -n emacs-mode-%name
%config(noreplace) %_emacs_sitestart_dir/%name-init.el
%_emacslispdir/%{name}*.elc

%files -n emacs-mode-%name-el
%_emacslispdir/%{name}*.el

%changelog
* Wed Nov 28 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.18.2-alt1
- rebuilt with guile22

* Mon Aug 13 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.18.2-alt0.3
- Updated build dependencies

* Mon Jul 31 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.18.2-alt0.2
- Updated build dependencies

* Thu Nov 06 2014 Michael Pozhidaev <msp@altlinux.ru> 2.18.2-alt0.1
- New version: 2.18.2

* Thu Jan 02 2014 Michael Pozhidaev <msp@altlinux.ru> 2.18.0-alt0.1
- New version: 2.18.0

* Sat Dec 07 2013 Michael Pozhidaev <msp@altlinux.ru> 2.16.0-alt0.2
- %autoreconf added to fix compilation errors

* Sat Oct 06 2012 Michael Pozhidaev <msp@altlinux.ru> 2.16.0-alt0.1
- New version

* Wed Jul 18 2012 Michael Pozhidaev <msp@altlinux.ru> 2.14.2-alt2
- emacs23 req changed to emacs24

* Fri Jan 06 2012 Michael Pozhidaev <msp@altlinux.ru> 2.14.2-alt1
- New version

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.12.3-alt1.1
- Rebuild with Python-2.7

* Sat Nov 13 2010 Michael Pozhidaev <msp@altlinux.ru> 2.12.3-alt1
- New version: 2.12.3
- Fix compilation error with gcc4.5
- New packager
- Temporarily disabled lilypond-tex subpackage
- Temporarily disabled lilypond-doc subpackage

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.12.2-alt1.1

* Sun Jul 19 2009 Michael Pozhidaev <msp@altlinux.ru> 2.12.2-alt1
- New version 2.12.2
- Applied patch for gcc4.4 compilation

* Thu Apr 23 2009 Michael Pozhidaev <msp@altlinux.ru> 2.12.1-alt3
- lilypond-tex became noarch (after at@ incoming checking fixes)

* Thu Apr 16 2009 Michael Pozhidaev <msp@altlinux.ru> 2.12.1-alt2
- All TeX files moved into subpackage to reduce dependencies of main rpm
- Some spec cleanup

* Sun Mar 15 2009 Michael Pozhidaev <msp@altlinux.ru> 2.12.1-alt1
- New version
- Removed explicit scrollkeeper calls
- Removed explicit dependence to tetex for emacs-mode-lilypond

* Fri Jan 02 2009 Michael Pozhidaev <msp@altlinux.ru> 2.11.61-alt2
- Fixed info files installation

* Fri Oct 17 2008 Michael Pozhidaev <msp@altlinux.ru> 2.11.61-alt1
- New version

* Sun Mar 02 2008 Ilya Mashkin <oddity@altlinux.ru> 2.11.0-alt2
- rebuild 2.11.0 with python 2.5.1

* Mon Dec 04 2006 Ildar Mulyukov <ildar@altlinux.ru> 2.11.0-alt1
- 2.11.0, packager change
- removed patches
- tear off russian patches, updated russian-lirycs-test.ly
- removed shell initscripts - not needed now
- fixed info files/layouts
- docs building disabled

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.0-alt0.7.1
- Rebuilt with libstdc++.so.6.

* Fri Aug 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt0.7
- fixed %%install.

* Mon Jun 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt0.6
- fixed russian lirycs support (close #4450). Thanks to Ruslan Gordeev.
  See /usr/share/doc/lilypond-%version/russian-lirycs-test.ly for example.

* Wed Apr 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt0.5
- 2.2.0

* Thu Feb 26 2004 Dmitry V. Levin <ldv@altlinux.org> 2.0.1-alt0.5.1
- Fixed ghostscript dependencies.
- Removed libintl-devel dependencies.

* Sun Dec 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt0.5
- 2.0.1

* Thu Sep 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.0-alt0.5
- 2.0.0

* Wed Jul 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.6.11-alt0.5
- 1.6.11

* Wed Mar 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.6.8-alt0.5
- 1.6.8

* Sat Dec 07 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.6.6-alt0.2
- Rebuild with new TeX.

* Wed Oct 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.6.6-alt0.1
- 1.6.6

* Tue May 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.4.13-alt1
- 1.4.13 

* Thu Apr 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.4.12-alt3
- rebuild with new autotrace

* Tue Mar 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.4.12-alt2
- emacs-mode-%%{name}* packages.
- new buildrequires

* Sun Mar 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.4.12-alt1
- 1.4.12
- stepmake patch removed, not needed more.
- makedocs patch. (fix building docs with python2.2)

* Fri Jan 25 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.4.9-alt2
- Cleanups

* Fri Nov 30 2001 Yuri N. Sedunov <aris@altlinux.ru> 1.4.9-alt1
- Updated to 1.4.9

* Thu Nov 16 2001 Yuri N. Sedunov <aris@altlinux.ru> 1.4.8-alt3
- Spec cleanup.

* Thu Nov 15 2001 Yuri N. Sedunov <aris@altlinux.ru> 1.4.8-alt2
- configure with --datadir=%_datadir/%name

* Tue Nov 13 2001 Yuri N. Sedunov <aris@altlinux.ru> 1.4.8-alt1
- First build for Sisyphus
