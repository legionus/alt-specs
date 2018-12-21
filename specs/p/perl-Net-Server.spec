BuildRequires: perl-podlators
%define _unpackaged_files_terminate_build 1
%define module  Net-Server

Name: perl-%module
Version: 2.009
Release: alt1

Summary: Net::Server - Extensible, general Perl server engine
License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/%module/

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/R/RH/RHANDOM/%{module}-%{version}.tar.gz

BuildRequires: perl-devel perl-IO-Multiplex perl-Net-SSLeay perl(Log/Log4perl.pm) perl(Pod/Man.pm)
Requires: perl-IO-Multiplex perl-Net-SSLeay
# hack around broken requires in perl-ARCv2
Provides: perl(Net/Server/PreFork.pm) = %version

%description
Net::Server is an extensible, class oriented module written in perl
and intended to be the back end layer of internet protocol servers.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %name


%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes examples
%perl_vendor_privlib/Net/*.pm
%perl_vendor_privlib/Net/*.pod
%perl_vendor_privlib/Net/Server

%files scripts
%_bindir/*
%_man1dir/*


%changelog
* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.009-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.008-alt2
- added compat provides

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 2.008-alt1
- automated CPAN update

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 2.007-alt2
- fixed build

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.007-alt1
- automated CPAN update

* Thu Sep 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.006-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.99-alt1.1
- rebuilt with perl 5.12

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1
- automated CPAN update

* Mon Oct 06 2008 Alexey Shabalin <shaba@altlinux.ru> 0.97-alt2
- fixed files list for sisyphus_check

* Thu Sep 20 2007 Alexey Shabalin <shaba@altlinux.ru> 0.97-alt1
- new version 0.97

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 0.96-alt1
- new version 0.96

* Thu Feb 01 2007 Alexey Shabalin <shaba@altlinux.ru> 0.94-alt1
- new version 0.94

* Mon Apr 17 2006 Alexey Shabalin <shaba@altlinux.ru> 0.93-alt1
- new version 0.93

* Thu Dec 08 2005 Alexey Shabalin <shaba@altlinux.ru> 0.90-alt1
- new version 0.90

* Mon Jun 27 2005 Alexey Shabalin <shaba@altlinux.ru> 0.88-alt1
- Update Net-Server-0.88
- add Requires: perl-IO-Multiplex (#7205)

* Thu Feb 17 2005 Alexey Shabalin <shaba@altlinux.ru> 0.87-alt2
- rebuild with rpm-build-perl-0.5.1-alt2

* Wed Mar 17 2004 Alexey Shabalin <shaba@altlinux.ru> 0.87-alt1
- Update Net-Server-0.87

* Tue Dec 02 2003 Alexey Shabalin <shaba@altlinux.ru> 0.86-alt0.1
- First release for ALT Linux 

