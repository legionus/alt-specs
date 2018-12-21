# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt3.1
Name: fvwm-tcl
Summary: FVWM tcl package
Version: 1.2
#Release: alt3
License: GPL
Group: Graphical desktop/FVWM based

Url: http://vitus.wagner.pp.ru/software/tcl/tclfvwm.html

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: tclFvwm-%version.tar.gz

%description
%summary

%prep
%setup -n lib%name-%version

%build
%install
%makeinstall_std
%if "/usr/lib" != "%_libdir"
mkdir -p %buildroot%_libdir
mv %buildroot/usr/lib/* %buildroot%_libdir/
%endif

%files
%dir %_libdir/fvwm-tcl
%_libdir/fvwm-tcl/*

%changelog
* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2-alt3.1
- (AUTO) subst_x86_64.

* Mon Apr 27 2009 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt3
- add Url tag

* Fri Dec 05 2008 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt2
- fix build on x86_64
- spec cleanup

* Sun Mar 20 2005 Denis Smirnov <mithraen@altlinux.ru> 1.2-alt1
- build

