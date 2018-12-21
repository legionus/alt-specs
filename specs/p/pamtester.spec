Name: pamtester
Version: 0.1.12
Release: alt1.qa2
License: GPL
Group: Accessibility
Summary: Utility for testing pluggable authentication modules (PAM) facility
Url: http://pamtester.sourceforge.net/

BuildRequires: pam-devel

Source: %name-%version.tar

%description
pamtester is a tiny utility program to test the pluggable authentication
modules (PAM) facility, which is a de facto standard of unified authentication
management mechanism in many unices and similar OSes including Solaris, HP-UX,
*BSD, MacOSX and Linux.

%prep
%setup

%build
%autoreconf
%configure
%make

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/pamtester
%_man1dir/pamtester.*

%changelog
* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.12-alt1.qa2
- NMU: added URL

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.12-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Jan 26 2011 Afanasov Dmitry <ender@altlinux.org> 0.1.12-alt1
- initial build
