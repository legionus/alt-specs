Group: File tools
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           bcrypt
Version:        1.1
Release:        alt2_22
Summary:        File encryption utility

License:        BSD
URL:            http://%{name}.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         bcrypt-fencepost.patch
BuildRequires:  zlib-devel gcc

BuildRequires:  %{__perl}
Source44: import.info

%description
Bcrypt is a cross platform file encryption utility. Encrypted files are
portable across all supported operating systems and processors.
Passphrases must be between 8 and 56 characters and are hashed internally
to a 448 bit key. However, all characters supplied are significant. The
stronger your passphrase, the more secure your data.

In addition to encrypting your data, bcrypt will by default overwrite the
original input file with random garbage three times before deleting it in
order to thwart data recovery attempts by persons who may gain access to
your computer. Bcrypt uses the blowfish encryption algorithm published by 
Bruce Schneier in 1993.


%prep
%setup -q

%patch0 -p1 -b .fencepost

/usr/bin/perl -pi.orig -e 's|\/man/man1|\/share/man/man1|g' Makefile


%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
make install PREFIX="%{buildroot}%{_prefix}"


%files
%doc README
%doc --no-dereference LICENSE
%doc %{_mandir}/man1/bcrypt.1*
%{_bindir}/bcrypt

%changelog
* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_22
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_19
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_16
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_14
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_13
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_10
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_7
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_6
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_6
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_5
- initial release by fcimport

