#set_automake_version 1.11

Name: cdcd
Version: 0.6.6
Release: alt6.git20140208.1
Summary: Command Driven CD player
License: %gpl2plus
Group: Sound
URL: http://libcdaudio.sourceforge.net/
# git://git.code.sf.net/p/libcdaudio/cdcd
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: glib2-devel libcdaudio-devel libreadline-devel
BuildPreReq: libsocket-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
%name takes a different approach from conventional console (or X) based
CD players, in that it doesn't keep with the display-oriented paradigm.
Conventional computer-based CD players resemble traditional physical CD
players. This is fine, if your user interface consists of 10 buttons.
However, computers have keyboards, so why not use them? Besides, it's
certainly a waste of a console or an xterm to have a traditional CD
player open anyway.
%name works in two ways, accepting commands directly off the command
line or in a query mode similar to other UNIX programs. To pass a
command to %name, simply run %name with the command as the arguement
(e.g. %name play). This is great for using cron and %name together to
make a CD alarm clock. Or, you can run %name without arguments and you
will be given the %name command prompt.


%prep
%setup


%build
%define _optlevel s
%add_optflags -D_GNU_SOURCE
%autoreconf
%configure
%make_build
bzip2 --best --force --keep ChangeLog


%install
%make_install DESTDIR=%buildroot install

# menu
install -d %buildroot%_desktopdir
iconv -f cp1251 -t utf-8 > %buildroot%_desktopdir/%name.desktop <<__MENU__
[Desktop Entry]
GenericName=Command Driven CD player
GenericName[ru]=��-������������� � ��������� �����������
GenericName[uk]=��-��������� � ��������� ����������
Name=%name
Exec=%name
Icon=cdaudio_unmount
Type=Application
Terminal=true
Categories=AudioVideo;Audio;Player;ConsoleOnly;
__MENU__


%files
%doc README NEWS AUTHORS ChangeLog.*
%_bindir/*
%_infodir/*
%_man1dir/*
%_desktopdir/*


%changelog
* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt6.git20140208.1
- NMU: added BR: texinfo

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt6.git20140208
- Snapshot from git

* Wed Nov 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt5.qa3
- Fixed build

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.6-alt5.qa2
- NMU: rebuilt for debuginfo.

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.6.6-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for cdcd
  * postclean-05-filetriggers for spec file

* Sat Dec 27 2008 Led <led@altlinux.ru> 0.6.6-alt5
- cleaned up spec

* Sat Aug 09 2008 Led <led@altlinux.ru> 0.6.6-alt4
- fixed %name.desktop
- fixed License

* Tue Mar 04 2008 Led <led@altlinux.ru> 0.6.6-alt3
- fixed %name.desktop

* Thu Sep 20 2007 Led <led@altlinux.ru> 0.6.6-alt2
- fixed %name.desktop

* Wed Jun 14 2006 Led <led@altlinux.ru> 0.6.6-alt1
- initial build
- removed libcurses checking with %name-0.6.6-curses.patch
