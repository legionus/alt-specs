Name: nslint
Version: 3.1
Release: alt1

Summary: A DNS lint checker
License: BSD-style
Group: Networking/Other
Url: ftp://ftp.ee.lbl.gov

# %url/%name-%version.tar.gz
Source: nslint-%version.tar

%description
Performs consistency checks on DNS files.

%prep
%setup

%build
%configure
%make_build

%install
install -Dpm755 nslint %buildroot%_bindir/nslint
install -Dpm644 nslint.8 %buildroot%_man8dir/nslint.8

%files
%_bindir/*
%_man8dir/*
%doc README CHANGES

%changelog
* Fri Apr 19 2013 Dmitry V. Levin <ldv@altlinux.org> 3.1-alt1
- Updated to 3.1.

* Wed Apr 18 2007 Dmitry V. Levin <ldv@altlinux.org> 2.1a7-alt1
- Updated to 2.1a7.

* Wed Nov 20 2002 Dmitry V. Levin <ldv@altlinux.org> 2.1a3-alt2
- Rebuilt in new environment.

* Wed Mar 06 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.1a3-alt1
- 2.1a3

* Thu Mar 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.0.2-ipl1
- 2.0.2

* Sat Jan 20 2001 Dmitry V. Levin <ldv@fandra.org> 2.0.1-ipl2mdk
- RE adaptions.

* Sat Sep 02 2000 Giuseppe Ghib� <ghibo@mandrakesoft.com> 2.0.1-2mdk
- use of %%_bindir.

* Fri Sep 01 2000 Giuseppe Ghib� <ghibo@mandrakesoft.com> 2.0.1-1mdk
- initial release.
