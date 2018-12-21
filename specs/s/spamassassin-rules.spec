Name: spamassassin-rules
Version: 3.4.1
Release: alt1

Summary: Rules for SpamAssassin
License: Apache License v2.0
Group: Networking/Mail

URL: http://spamassassin.org/
Source: http://www.apache.org/dist/spamassassin/source/Mail-SpamAssassin-rules-%version.r1675274.tgz

BuildArch: noarch

# We should require package that contains /usr/share/spamassassin (as we put files in this directory)
# Note this reason here to correctly change requirement in case of package rearrangements.
Requires: perl-Mail-SpamAssassin >= 3.4.1
Conflicts: perl-Mail-SpamAssassin < 3.4.1

%description
This package contains the default packaged rules for SpamAssassin.

%prep
%setup -c -T -n %name-%version -a0

%build

%install
install -d %buildroot%_datadir/spamassassin
install -pm644 *.cf %buildroot%_datadir/spamassassin

%files
%_datadir/spamassassin

%changelog
* Sun Nov 15 2015 Sergey Y. Afonin <asy@altlinux.ru> 3.4.1-alt1
- 3.4.1 (r1675274)

* Thu Jun 19 2014 Sergey Y. Afonin <asy@altlinux.ru> 3.4.0-alt1
- 3.4.0 (r1565117)

* Sat Jul 23 2011 Victor Forsiuk <force@altlinux.org> 3.3.2-alt1
- 3.3.2

* Fri Oct 08 2010 Victor Forsiuk <force@altlinux.org> 3.3.1-alt1
- 3.3.1

* Wed Mar 03 2010 Victor Forsiuk <force@altlinux.org> 3.3.0-alt1
- Initial build.
