# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Apache2/Const.pm) perl(Apache2/RequestIO.pm) perl(Apache2/RequestRec.pm) perl(Apache2/RequestUtil.pm) perl(Exporter.pm) perl(FindBin.pm) perl(SOAP/Lite.pm) perl(SOAP/Transport/HTTP.pm) perl(base.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global perlname Apache2-SOAP

Name:      perl-Apache2-SOAP
Version:   0.73
Release:   alt2
Summary:   A replacement for Apache::SOAP designed to work with mod_perl 2

Group:     Development/Other
License:   GPL-1.0-or-later or Artistic
URL:       http://search.cpan.org/dist/Apache2-SOAP/
Source:    http://search.cpan.org/CPAN/authors/id/R/RK/RKOBES/%{perlname}-%{version}.tar.gz
Patch0:	   perl-Apache2-SOAP-drop-apache1-requires.patch

BuildArch: noarch

BuildRequires: rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: apache2-mod_perl-devel





%description
This Apache Perl module provides the ability to add support for SOAP
(Simple Object Access Protocol) protocol with easy configuration
(either in .conf or in .htaccess file). This functionality should
give you lightweight option for hosting SOAP services and greatly
simplify configuration aspects. This module inherites functionality
from SOAP::Transport::HTTP2::Apache component of SOAP::Lite module.


%prep
%setup -q -n %{perlname}-%{version}
%patch0 -p2


%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make_build


%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';' -print
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';' -print
chmod -R u+rwX,go+rX,go-w %{buildroot}/*


%files
%doc Changes README
%{perl_vendor_privlib}/Apache2
%{perl_vendor_privlib}/SOAP/Transport/HTTP2.pm


%changelog
* Fri Sep 29 2017 Anton Farygin <rider@altlinux.ru> 0.73-alt2
- drop Apache1 requires

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_22
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_21
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_20
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_19
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_15
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_14
- update to new release by fcimport

* Sun Apr 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1_13
- fixed build

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- automated CPAN update

* Mon Dec 15 2008 Lebedev Sergey <barabashka@altlinux.org> 0.72-alt3.1
- moved back noarch, removed empty dir perl_vendor_autolib/Apache2*

* Mon Dec 15 2008 Lebedev Sergey <barabashka@altlinux.org> 0.72-alt3
- removed noarch from package due to perl_vendor_autolib/Apache2

* Mon Dec 15 2008 Lebedev Sergey <barabashka@altlinux.org> 0.72-alt2
- fixed ownership viloation 

* Sun Apr 06 2008 Sir Raorn <raorn@altlinux.ru> 0.72-alt1
- first build for ALT Linux Sisyphus

