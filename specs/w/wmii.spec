# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt4.1
Name: wmii
Version: 3.9.2
#Release: alt4

Summary: Window manager improved 2
License: MIT
Group: Graphical desktop/Other

URL: http://wmii.suckless.org/
Source: %name-%version-%release.tar
Source1: wmiiloop

Requires: ixpc dmenu

BuildPreReq: libXt-devel libXft-devel libfreetype-devel libXext-devel
BuildPreReq: libXrandr-devel libXinerama-devel

%add_findreq_skiplist /etc/wmii/plan9port/wmiirc

%description
Wimp is dead!! - wmii is a dynamic window manager for X11.  It supports
classic and dynamic window management with extended keyboard, mouse, and
filesystem based remote control.  It replaces the workspace paradigm with
a new tagging approach.

%prep
%setup -n %name-%version-%release

%build
%make_build LIBX11="-lX11 -ldl"

#gcc %optflags -DVERSION=\"%version-%release\" -Iinclude cmd/wmii/*.c cmd/util.c -o wmii -lX11 -lixp -lm
#gcc %optflags cmd/wmii9menu.c -o wmii9menu -lX11

%install
make install DESTDIR=%buildroot

%if "%_libexecdir" != "%_libdir"
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/*.so %buildroot%_libdir/
%endif

#install -pD -m755 wmii %buildroot%_bindir/wmii
#install -pD -m755 wmii9menu %buildroot%_bindir/wmii9menu
#install -pD -m755 cmd/wmiir.sh %buildroot%_bindir/wmiir
#install -pD -m755 cmd/wmiistartrc.sh %buildroot%_bindir/wmiistartrc
#install -pD -m755 cmd/wmiiloop.awk %buildroot%_bindir/wmiiloop
install -pD -m755 %SOURCE1 %buildroot%_bindir/wmiiloop

%define wmiidir /etc/wmii

#install -pD -m755 rc/wmiirc.sh %buildroot%wmiidir/wmiirc
#install -pD -m755 rc/welcome.sh %buildroot%wmiidir/welcome

#mkdir -p %buildroot%_man1dir
#install -p -m744 man/wmii*.1 %buildroot%_man1dir/

install -pD -m644 img/wmii.png %buildroot%_niconsdir/wmii.png
mkdir -p %buildroot/etc/X11/wmsession.d
cat >%buildroot/etc/X11/wmsession.d/11wmii <<EOF
NAME=wmii
ICON=%_niconsdir/wmii.png
DESC=%summary
EXEC=%_bindir/wmii
SCRIPT:
exec %_bindir/wmii
EOF

%files
%doc DISTRIBUTORS NEWS NOTES TODO
%doc %_docdir/%name
%config %wmiidir/
%_bindir/*
%_man1dir/*
%_libdir/*.so
%config /etc/X11/wmsession.d/11wmii
%_niconsdir/wmii.png

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.9.2-alt4.1
- (AUTO) subst_x86_64.

* Fri Jan 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt4
- Fixed build with make 3.82

* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt3
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.2-alt2.1
- Rebuild with Python-2.7

* Wed Jul 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt2
- Restored %_bindir/wmiiloop

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.2-alt1
- Version 3.9.2

* Sat Feb 06 2010 Repocop Q. A. Robot <repocop@altlinux.org> 3.7-alt0.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for wmii
  * postclean-05-filetriggers for spec file

* Tue Apr 03 2007 Alexey Tourbin <at@altlinux.ru> 3.7-alt0.1
- imported sources from suckless.org mercurial repo into git
- updated to most recent snapshot and set version to 3.7
- wmiirc: changed default MODKEY from Alt to Win
- wmiirc: changed default terminal emulator form xterm to xvt

* Sun Jun 18 2006 Alexey Tourbin <at@altlinux.ru> 3.1-alt1
- initial revision
- sync debian wmii_3.0-1.diff.gz
- wmiirc: 
  + always regenerate proglist
  + changed /tmp/ns.$USER.$DISPLAY to ${TMPDIR:-/tmp}/ns.$USER.$DISPLAY
