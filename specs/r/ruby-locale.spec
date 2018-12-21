# vim: set ft=spec: -*- rpm-spec -*-
%def_without tests

%define pkgname ruby-locale

Name: %pkgname
Version: 2.1.2
Release: alt4.1

Summary: Pure ruby library which provides basic APIs for localization
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/locale/

BuildArch: noarch

Source: %pkgname-%version.tar
Patch1: ruby-locale-2.0.6-alt-Do-not-call-locale-charmap-if-LC_-variables-unset.patch
Patch2: ruby-locale-2.0.6-alt-Fix-Array-vs-String-clash.patch

BuildRequires: rpm-build-ruby ruby-stdlibs ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
Ruby-Locale is the pure ruby library which provides basic and general
purpose APIs for localization.

It aims to support all environments which ruby works and all kind of
programs (GUI, WWW, library, etc), and becomes the hub of other
i18n/l10n libs/apps to handle major locale ID standards.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch1 -p1
%patch2 -p1
%update_setup_rb

rm -f test/test_driver_jruby.rb
rm -f test/test_driver_win32.rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%check
%if_with tests
%ruby_test_unit -Ilib:test test
%endif

%files
%doc README.rdoc
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/locale/driver/win32*.rb
%rubygem_specdir/*

%files doc
%doc samples ChangeLog
%ruby_ri_sitedir/Locale*

%changelog
* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt4.1
- Rebuild for new Ruby autorequirements.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt4
- Use system way  of gemspec installation.
- Disable tests.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt3
- Return jruby driver.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt2.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt2
- Rebuild with Ruby 2.4.2

* Sun May 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- New version
- Package with gemspec

* Wed Dec 05 2012 Led <led@altlinux.ru> 2.0.6-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 2.0.6-alt1
- [2.0.6]

* Sun Apr 18 2010 Alexey I. Froloff <raorn@altlinux.org> 2.0.5-alt1
- [2.0.5]

* Thu Nov 19 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt4
- Ignore invalid LANGUAGE variable

* Tue Oct 27 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt3
- Fixed String vs. Array clash

* Thu Oct 15 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt2
- Fixed charset detection when LC_* variables unset

* Tue Oct 13 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.4-alt1
- [2.0.4]

* Wed May 06 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.1-alt1
- Built for Sisyphus

