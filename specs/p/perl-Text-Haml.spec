# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Text-Haml
%define upstream_version 0.990118

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    Haml Perl implementation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(Data/Section/Simple.pm)
BuildRequires: perl(Digest/MD5.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(File/Basename.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(IO/File.pm)
BuildRequires: perl(Module/Build/Tiny.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(URI/Escape.pm)
BuildRequires: perl(Test/More.pm)
BuildArch:  noarch
Source44: import.info

%description
the Text::Haml manpage implements Haml the
http://haml-lang.com/docs/yardoc/file.HAML_REFERENCE.html manpage
specification.

the Text::Haml manpage passes specification tests written by Norman Clarke
http://github.com/norman/haml-spec and supports only cross-language Haml
features. Do not expect Ruby specific things to work.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Build.PL --install_path bindoc=%_man1dir --installdirs=vendor
./Build

%check
./Build test

%install
./Build install --destdir=%buildroot
rm -f %{buildroot}/%{perl_vendor_privlib}/Text/README.pod

%files
%doc Changes LICENSE META.json META.yml 
%{perl_vendor_privlib}/*


%changelog
* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.990118-alt1_2
- update by mgaimport

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.990118-alt1_1
- update by mgaimport

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.990118-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.990117-alt1_2
- update by mgaimport

* Sat May 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.990117-alt1_1
- update by mgaimport

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.990117-alt1
- automated CPAN update

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.990116-alt1_6
- update by mgaimport

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.990116-alt1_5
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.990116-alt1_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.990116-alt1_2
- update by mgaimport

* Thu May 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.990116-alt1_1
- update by mgaimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.990115-alt1_1
- update by mgaimport

* Fri Oct 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.990111-alt1
- automated CPAN update

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.990110-alt1
- automated CPAN update

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.990109-alt1_2
- update by mgaimport

* Wed Sep 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.990109-alt1_1
- update by mgaimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.990109-alt1
- automated CPAN update

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.990108-alt1_1
- build for Sisyphus

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.990107-alt1_1
- converted for ALT Linux by srpmconvert tools

