Name: razor
Version: 2.85
Release: alt4.2

Summary: Spam detection and filtering network
License: Artistic 2.0
Group: Networking/Mail

URL: http://razor.sourceforge.net/
Source: http://download.sourceforge.net/razor/razor-agents-%version.tar.bz2
Patch: razor-agents-2.85-alt-perl-5.22-fix.patch

Requires: perl-Razor = %version-%release

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Digest-SHA1 perl-URI perl-devel perl-podlators

%description
Vipul's Razor is a distributed, collaborative, spam detection, reporting, and
filtering network. The primary focus of the system is to identify and remove an
email spam before its injection and processing is complete.

%package -n perl-Razor
Summary: Perl modules for Razor
Group: Development/Perl

%description -n perl-Razor
Perl modules for Razor.

%prep
%setup -n razor-agents-%version
%patch -p1

%build
mkdir -p blib/man5
%perl_vendor_build INSTALLMAN1DIR=%_man1dir INSTALLMAN5DIR=%_man5dir

%install
%perl_vendor_install

%files
%doc FAQ README SERVICE_POLICY
%_bindir/*
%_man1dir/*
%_man5dir/*

%files -n perl-Razor
%perl_vendor_archlib/Razor2
%perl_vendor_autolib/Razor2

%changelog
* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.85-alt4.2
- Fix build documentation.

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.85-alt4.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.85-alt4.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.85-alt4.1
- rebuild with new perl 5.22.0

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.85-alt4
- bugfix for perl 5.22

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.85-alt3.1
- rebuild with new perl 5.20.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 2.85-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 2.85-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 2.85-alt1.2
- rebuilt for perl-5.14

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 2.85-alt1.1
- rebuilt with perl 5.12

* Thu Feb 11 2010 Victor Forsiuk <force@altlinux.org> 2.85-alt1
- 2.85

* Wed Jun 06 2007 Victor Forsyuk <force@altlinux.org> 2.84-alt1
- 2.84

* Mon Jun 05 2006 Victor Forsyuk <force@altlinux.ru> 2.82-alt1
- 2.82

* Tue Apr 18 2006 Victor Forsyuk <force@altlinux.ru> 2.81-alt1
- 2.81

* Thu Oct 27 2005 Victor Forsyuk <force@altlinux.ru> 2.77-alt1
- 2.77

* Wed Jul 13 2005 Victor Forsyuk <force@altlinux.ru> 2.75-alt1
- 2.75

* Fri Jun 17 2005 Victor Forsyuk <force@altlinux.ru> 2.72-alt1
- Initial build.
