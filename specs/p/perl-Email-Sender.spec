Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Email-Sender
Version:        1.300031
Release:        alt1_5
Summary:        A library for sending email
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Email-Sender
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Sender-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Email/Abstract.pm)
BuildRequires:  perl(Email/Address.pm)
BuildRequires:  perl(Email/Simple.pm)
BuildRequires:  perl(Errno.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Fcntl.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Path.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(IO/File.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(JSON.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(Module/Runtime.pm)
BuildRequires:  perl(Moo.pm)
BuildRequires:  perl(Moo/Role.pm)
BuildRequires:  perl(MooX/Types/MooseLike/Base.pm)
BuildRequires:  perl(Net/SMTP.pm)
BuildRequires:  perl(Net/SMTP/SSL.pm)
BuildRequires:  perl(Pod/Coverage/TrustPod.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Sub/Exporter.pm)
BuildRequires:  perl(Sub/Exporter/Util.pm)
BuildRequires:  perl(Sub/Override.pm)
BuildRequires:  perl(Sys/Hostname.pm)
BuildRequires:  perl(Test/MinimumVersion.pm)
BuildRequires:  perl(Test/MockObject.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Throwable/Error.pm)
BuildRequires:  perl(Try/Tiny.pm)
BuildRequires:  perl(warnings.pm)
Requires:       perl(Email/Abstract.pm) >= 3.006
Requires:       perl(Net/SMTP/SSL.pm)
Requires:       perl(Throwable/Error.pm) >= 0.200.003


Source44: import.info

%description
Email::Sender replaces the old and sometimes problematic Email::Send library,
which did a decent job at handling very simple email sending tasks, but was not
suitable for serious use, for a variety of reasons.

%prep
%setup -q -n Email-Sender-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 make test

%files
%doc Changes README
%doc --no-dereference LICENSE
%{perl_vendor_privlib}/Email*

%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.300031-alt1_5
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.300031-alt1_3
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.300031-alt1_2
- update to new release by fcimport

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.300031-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.300030-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.300030-alt1_1
- update to new release by fcimport

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.300030-alt1
- automated CPAN update

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.300028-alt1_2
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.300028-alt1_1
- update to new release by fcimport

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.300028-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.300027-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.300021-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.300021-alt1_1
- update to new release by fcimport

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.300021-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.300020-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.300016-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.300014-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.300012-alt1
- automated CPAN update

* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.300011-alt1
- automated CPAN update

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.300010-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.300006-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.120002-alt2_4
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.120002-alt2_2
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.120002-alt2_1
- moved to Sisyphus

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.120002-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.120001-alt1_1
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.110005-alt1_1
- fc import

