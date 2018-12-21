# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname tmail

Name: ruby-%pkgname
Version: 1.2.3.1
Release: alt3.6

Summary: Mail handling library for Ruby
License: GPL
Group: Development/Ruby
URL: http://tmail.rubyforge.org/

BuildArch: noarch

BuildRequires: rpm-build-ruby ruby-racc ruby-test-unit ruby-tool-rdoc ruby-tool-setup ruby-iconv

# http://rubyforge.org/frs/?group_id=4512
Source: %pkgname-%version.tar
Patch: %name-%version-%release.patch

%description
TMail is mail handling library for Ruby. TMail can extract data from mail,
and write data to mail following by RFC procedures.

%package doc
Summary: Documentation files for %name
Group: Development/Documentation

%description doc
Documentation files for %name.


%prep
%setup -q -n %pkgname-%version
%patch -p1
%update_setup_rb

# leftovers of indeterminate origin
rm -f lib/tmail/require_arch.rb
# will regenerate
rm -f lib/tmail/parser.rb
# epic fail
rm -f test/test_encode.rb


%build
%ruby_config --without-ext
%ruby_build
cd lib/tmail
%make_build parser.rb


%install
%ruby_install
%rdoc lib/


%check
#%%ruby_test_unit test

%files
%doc CHANGES LICENSE NOTES README
%ruby_sitelibdir/*

%files doc
%doc sample
%ruby_ri_sitedir/TMail*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.3.1-alt3.6
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Fri Mar 21 2014 Led <led@altlinux.ru> 1.2.3.1-alt3.5
- revert to use iconv for all Ruby versions
- enabled %%check

* Sat Mar 15 2014 Led <led@altlinux.ru> 1.2.3.1-alt3.4
- disabled %%check

* Sat Mar 15 2014 Led <led@altlinux.ru> 1.2.3.1-alt3.3
- don't use iconv for ruby > 1.9.3

* Sat Mar 15 2014 Led <led@altlinux.ru> 1.2.3.1-alt3.2
- fixed tests

* Tue Dec 04 2012 Led <led@altlinux.ru> 1.2.3.1-alt3.1
- Rebuilt with ruby-1.9.3-alt1

* Sun Jan 02 2011 Alexey I. Froloff <raorn@altlinux.org> 1.2.3.1-alt3
- Fix tests

* Sun May 31 2009 Alexey I. Froloff <raorn@altlinux.org> 1.2.3.1-alt2
- Use ruby-based scanner module
- Rebuilt for Ruby 1.9

* Tue Jul 08 2008 Sir Raorn <raorn@altlinux.ru> 1.2.3.1-alt1
- [1.2.3.1]

* Tue Apr 01 2008 Sir Raorn <raorn@altlinux.ru> 1.2.2-alt1
- [1.2.2]

* Mon Dec 03 2007 Sir Raorn <raorn@altlinux.ru> 1.2.0-alt1
- [1.2.0]
- Added RI documentation
- Updated buildrequires
- Updated requires

* Wed Apr 28 2004 Sir Raorn <raorn@altlinux.ru> 0.10.8-alt1
- New version

* Mon Jul 07 2003 Alexander Bokovoy <ab@altlinux.ru> 0.10.6-alt3
- Rebuild against Ruby 1.8-alt3
- FIxed:
    + ruby-tmail should not probide RACC, it is already in Ruby 1.8
    + Documentation is included

* Thu Jan 30 2003 Kachalov Anton <mouse@altlinux.ru> 0.10.6-alt2
- buildreq

* Tue Dec 10 2002 Kachalov Anton <mouse@altlinux.ru> 0.10.6-alt1
- new version

