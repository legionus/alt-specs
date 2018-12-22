%define pkgname i18n
%def_disable tests

Name: ruby-%pkgname
Version: 1.1.1
Release: alt1

Summary: I18n and localization solution for Ruby
Group: Development/Ruby
License: MIT or Ruby
Url: https://github.com/svenfuchs/i18n

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup tzdata
%if_enabled tests
BuildRequires: ruby-activerecord ruby-activerecord-sqlite3-adapter ruby-activesupport ruby-mocha
%endif

%description
I18n and localization solution for Ruby.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version

%build
%update_setup_rb
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%check
%if_enabled tests
%ruby_vendor test/all.rb
%endif

%files
%doc README*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/I18n*

%changelog
* Sun Oct 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt2.3
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Sat Mar 22 2014 Led <led@altlinux.ru> 0.3.7-alt2.2
- add true to respond_to? for 1.9.3 compatibility
- enabled %%check

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.3.7-alt2.1
- Rebuilt with ruby-1.9.3-alt1
- disabled check

* Sat May 29 2010 Alexey I. Froloff <raorn@altlinux.org> 0.3.7-alt2
- Mask ActiveRecord dependency

* Sun Apr 25 2010 Alexey I. Froloff <raorn@altlinux.org> 0.3.7-alt1
- [0.3.7]

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 0.3.6-alt1
- [0.3.6]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.1.3-alt1
- [0.1.3]

* Tue Feb 03 2009 Sir Raorn <raorn@altlinux.ru> 0.1.2-alt1
- [0.1.2]

* Wed Nov 19 2008 Sir Raorn <raorn@altlinux.ru> 0.1.0-alt3
- Updated to [g3696c92] from git://github.com/svenfuchs/i18n

* Tue Nov 18 2008 Sir Raorn <raorn@altlinux.ru> 0.1.0-alt2
- Updated to [g0bafcb3] from git://github.com/mattetti/i18n.git

* Mon Nov 10 2008 Sir Raorn <raorn@altlinux.ru> 0.1.0-alt1
- Built for Sisyphus

