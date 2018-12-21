# vim: set ft=spec : -*- rpm-spec -*-

%define pkgname flexmock

Name: ruby-%pkgname
Version: 2.3.6
Release: alt1.1

Summary: Simple mock object library for Ruby unit testing
Group: Development/Ruby
License: MIT
Url: http://rubyforge.org/projects/flexmock/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

Source: %pkgname-%version.tar
Patch: ruby-flexmock-disable-nonworking-tests.patch

BuildArch: noarch

BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
FlexMock is a simple, but flexible, mock object library for Ruby unit
testing.

%package doc
Summary: Documentation files for %pkgname
Group: Documentation

%description doc
Documentation files for %pkgname

%prep
%setup -n %pkgname-%version
%patch -p1
# Remove experimental mocking by rails
rm -f lib/flexmock/rails.rb
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib -I. test/*.rb

%install
%ruby_install
%rdoc lib/

%files
%doc CHANGES README.md
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/FlexMock*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.6-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Oct 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.6-alt1
- New version

* Wed Sep 06 2017 Andrey Cherepanov <cas@altlinux.org> 2.3.5-alt1
- New version
- Remove experimental mocking by rails

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1.2
- Rebuild with Ruby 2.4.1

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.9.0-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Mar 22 2011 Andriy Stepanov <stanv@altlinux.ru> 0.9.0-alt1
- [0.9.0]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.6-alt1
- [0.8.6]

* Tue Aug 26 2008 Sir Raorn <raorn@altlinux.ru> 0.8.2-alt1
- Built for Sisyphus

